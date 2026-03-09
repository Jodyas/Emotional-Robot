# Main GUI — CaP Robot System
# 使用 tkinter 建立三區塊介面：指令輸入、步驟展示、程式碼展示
# 背景執行緒處理 LLM 呼叫和 PyBullet 模擬，避免 GUI 卡頓

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import json

from config import OPENAI_API_KEY, MODEL
from planner import TaskPlanner
from code_generator import CodeGenerator
from pybullet_env import PyBulletEnv


# ──────────────────────────────────────────
#  Color scheme & fonts
# ──────────────────────────────────────────
BG_DARK      = "#1e1e2e"   # 深藍背景
BG_PANEL     = "#2a2a3e"   # 面板背景
BG_INPUT     = "#12121f"   # 輸入框背景
ACCENT_BLUE  = "#7aa2f7"   # 藍色強調
ACCENT_GREEN = "#9ece6a"   # 綠色（成功）
ACCENT_RED   = "#f7768e"   # 紅色（錯誤）
ACCENT_GOLD  = "#e0af68"   # 金色（標題）
TEXT_MAIN    = "#cdd6f4"   # 主要文字
TEXT_DIM     = "#6c7086"   # 次要文字

FONT_TITLE   = ("Segoe UI", 13, "bold")
FONT_LABEL   = ("Segoe UI", 10)
FONT_MONO    = ("Consolas", 9)
FONT_STATUS  = ("Segoe UI", 9, "italic")
FONT_BTN     = ("Segoe UI", 10, "bold")


class CaPGUI:
    """
    CaP Robot System 主視窗。
    佈局：
      頂部  — 指令輸入 + 情緒選擇 + Run 按鈕
      中間  — 左：Steps JSON panel | 右：Generated Code panel
      底部  — 狀態列
    """

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("CaP Robot System — Emotional Suction Arm")
        self.root.configure(bg=BG_DARK)
        self.root.geometry("980x700")
        self.root.minsize(820, 580)

        # 系統元件
        self.planner   = TaskPlanner()
        self.codegen   = CodeGenerator()
        self.sim_env   = None     # PyBulletEnv（第一次 Run 時初始化）
        self._lock     = threading.Lock()
        self._busy     = False    # 防止重複點擊

        self._build_ui()

    # ──────────────────────────────────────────
    #  UI Construction
    # ──────────────────────────────────────────

    def _build_ui(self):
        """建立所有 UI 元件"""
        self._build_header()
        self._build_input_row()
        self._build_panels()
        self._build_status_bar()

    def _build_header(self):
        """標題列"""
        header = tk.Frame(self.root, bg=BG_DARK, pady=10)
        header.pack(fill="x", padx=20)

        tk.Label(
            header,
            text="🤖  CaP Robot System",
            font=("Segoe UI", 16, "bold"),
            fg=ACCENT_GOLD, bg=BG_DARK
        ).pack(side="left")

        tk.Label(
            header,
            text="Code as Policies  ·  GPT-4o  ·  PyBullet",
            font=FONT_STATUS, fg=TEXT_DIM, bg=BG_DARK
        ).pack(side="left", padx=12, pady=4)

    def _build_input_row(self):
        """指令輸入列：文字框 + 情緒下拉選單 + Run 按鈕"""
        frame = tk.Frame(self.root, bg=BG_PANEL, pady=12, padx=16)
        frame.pack(fill="x", padx=20, pady=(0, 8))

        # Instruction label
        tk.Label(
            frame, text="Instruction:", font=FONT_LABEL,
            fg=ACCENT_BLUE, bg=BG_PANEL
        ).grid(row=0, column=0, sticky="w", padx=(0, 6))

        # Instruction entry
        self.instruction_var = tk.StringVar(value="pick up the cup")
        entry = tk.Entry(
            frame, textvariable=self.instruction_var,
            font=("Consolas", 11), bg=BG_INPUT, fg=TEXT_MAIN,
            insertbackground=TEXT_MAIN, relief="flat",
            bd=0, highlightthickness=1,
            highlightcolor=ACCENT_BLUE, highlightbackground=TEXT_DIM
        )
        entry.grid(row=0, column=1, sticky="ew", padx=(0, 12), ipady=5)
        entry.bind("<Return>", lambda e: self._on_run())

        # Replace the emotion dropdown with a spacer or remove it,
        # but the entry needs to span 4 columns now...
        entry.grid(row=0, column=1, columnspan=3, sticky="ew", padx=(0, 12), ipady=5)

        # Run button
        self.run_btn = tk.Button(
            frame, text="▶  Run", font=FONT_BTN,
            bg=ACCENT_BLUE, fg=BG_DARK, activebackground="#5a87e0",
            activeforeground=BG_DARK, relief="flat", bd=0,
            padx=18, pady=6, cursor="hand2",
            command=self._on_run
        )
        self.run_btn.grid(row=0, column=4, sticky="e")

        # Reset button
        self.reset_btn = tk.Button(
            frame, text="⟳  Reset Sim", font=FONT_BTN,
            bg=BG_INPUT, fg=TEXT_DIM, activebackground=BG_PANEL,
            relief="flat", bd=0, padx=12, pady=6, cursor="hand2",
            command=self._on_reset
        )
        self.reset_btn.grid(row=0, column=5, sticky="e", padx=(8, 0))

        frame.columnconfigure(1, weight=1)  # Entry 欄位可延伸

    def _build_panels(self):
        """中間兩個 panel：Step JSON（左）和 Generated Code（右）"""
        paned = tk.PanedWindow(
            self.root, orient="horizontal",
            bg=BG_DARK, sashwidth=6, sashrelief="flat"
        )
        paned.pack(fill="both", expand=True, padx=20, pady=4)

        # ── Left: Steps JSON ──
        left = tk.Frame(paned, bg=BG_PANEL)
        tk.Label(
            left, text="📋  Stage 1 — Plan (Steps JSON)",
            font=FONT_TITLE, fg=ACCENT_GOLD, bg=BG_PANEL, anchor="w"
        ).pack(fill="x", padx=10, pady=(8, 4))

        self.plan_text = scrolledtext.ScrolledText(
            left, font=FONT_MONO, bg=BG_INPUT, fg=TEXT_MAIN,
            insertbackground=TEXT_MAIN, relief="flat",
            state="disabled", wrap="word"
        )
        self.plan_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        paned.add(left, minsize=300)

        # ── Right: Generated Code ──
        right = tk.Frame(paned, bg=BG_PANEL)
        tk.Label(
            right, text="💻  Stage 2 — Generated Code (Python)",
            font=FONT_TITLE, fg=ACCENT_GOLD, bg=BG_PANEL, anchor="w"
        ).pack(fill="x", padx=10, pady=(8, 4))

        self.code_text = scrolledtext.ScrolledText(
            right, font=FONT_MONO, bg=BG_INPUT, fg=TEXT_MAIN,
            insertbackground=TEXT_MAIN, relief="flat",
            state="disabled", wrap="none"
        )
        self.code_text.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        paned.add(right, minsize=300)

    def _build_status_bar(self):
        """底部狀態列"""
        bar = tk.Frame(self.root, bg=BG_INPUT, pady=5)
        bar.pack(fill="x", side="bottom")

        self.status_var = tk.StringVar(value="Ready. Type an instruction and click Run.")
        self.status_label = tk.Label(
            bar, textvariable=self.status_var,
            font=FONT_STATUS, fg=TEXT_DIM, bg=BG_INPUT, anchor="w"
        )
        self.status_label.pack(fill="x", padx=16)

    # ──────────────────────────────────────────
    #  Event Handlers
    # ──────────────────────────────────────────

    def _on_run(self):
        """Run 按鈕點擊：在背景執行緒跑 pipeline"""
        if self._busy:
            return

        instruction = self.instruction_var.get().strip()
        if not instruction:
            messagebox.showwarning("No Instruction", "Please enter an instruction first.")
            return

        self._set_busy(True)
        self._clear_panels()
        self._set_status("🔄 Stage 1: Planning with GPT-4o...", ACCENT_BLUE)

        thread = threading.Thread(
            target=self._pipeline,
            args=(instruction,),
            daemon=True
        )
        thread.start()

    def _on_reset(self):
        """重置模擬環境"""
        if self._busy:
            return
        if self.sim_env:
            self.sim_env.disconnect()
            self.sim_env = None
        self._clear_panels()
        self._set_status("🔄 Simulation reset. Ready for new run.", TEXT_DIM)

    # ──────────────────────────────────────────
    #  Pipeline (background thread)
    # ──────────────────────────────────────────

    def _pipeline(self, instruction: str):
        """
        完整 pipeline：
          Stage 1: Planning (自動判斷情緒) → Stage 2: Coding → Stage 3: Execution
        """
        try:
            # ── Stage 1: Planning ────────────────────
            steps_dict = self.planner.plan(instruction)
            
            # 從 Planner 結果提取 LLM 判斷出的情緒 (預設 neutral)
            inferred_emotion = steps_dict.get("emotion", "neutral").lower()
            
            plan_json  = json.dumps(steps_dict, indent=2, ensure_ascii=False)
            self.root.after(0, self._show_plan, plan_json)
            self._set_status(f"✅ Stage 1 done (Emotion: {inferred_emotion}).  🔄 Stage 2: Generating code...", ACCENT_GREEN)

            # ── Stage 2: Code Generation ─────────────
            # 這裡使用 LLM 判斷出的 emotion
            code_str = self.codegen.generate(steps_dict, inferred_emotion)
            self.root.after(0, self._show_code, code_str)
            self._set_status("✅ Stage 2 done.  🔄 Launching PyBullet...", ACCENT_GREEN)

            # ── Stage 3: PyBullet Execution ───────────
            with self._lock:
                if self.sim_env is None:
                    self.sim_env = PyBulletEnv()
                    self.sim_env.setup()
                    self.sim_env.start_idle()

            self._set_status("🤖 Executing in PyBullet...", ACCENT_GOLD)
            self.sim_env.run_code(
                code_str,
                emotion=inferred_emotion,
                status_callback=lambda msg: self._set_status(msg, ACCENT_GOLD)
            )

            self._set_status(f"🎉 Done! (Emotion: {inferred_emotion})", ACCENT_GREEN)

        except Exception as e:
            self._set_status(f"❌ Error: {e}", ACCENT_RED)

        finally:
            self.root.after(0, self._set_busy, False)

    # ──────────────────────────────────────────
    #  UI Helpers
    # ──────────────────────────────────────────

    def _show_plan(self, text: str):
        """在左側 panel 顯示 Steps JSON"""
        self.plan_text.config(state="normal")
        self.plan_text.delete("1.0", "end")
        self.plan_text.insert("end", text)
        self.plan_text.config(state="disabled")

    def _show_code(self, text: str):
        """在右側 panel 顯示 Generated Code"""
        self.code_text.config(state="normal")
        self.code_text.delete("1.0", "end")
        self.code_text.insert("end", text)
        self.code_text.config(state="disabled")

    def _clear_panels(self):
        """清空兩個 panel"""
        for widget in (self.plan_text, self.code_text):
            widget.config(state="normal")
            widget.delete("1.0", "end")
            widget.config(state="disabled")

    def _set_status(self, msg: str, color: str = TEXT_DIM):
        """更新狀態列（可從任何執行緒呼叫）"""
        def _update():
            self.status_var.set(msg)
            self.status_label.config(fg=color)
        self.root.after(0, _update)

    def _set_busy(self, busy: bool):
        """設定忙碌狀態（停用/啟用按鈕）"""
        self._busy = busy
        state = "disabled" if busy else "normal"
        self.run_btn.config(state=state)

    def on_close(self):
        """視窗關閉時斷開 PyBullet"""
        if self.sim_env:
            self.sim_env.disconnect()
        self.root.destroy()


# ──────────────────────────────────────────
#  Entry Point
# ──────────────────────────────────────────

def main():
    root = tk.Tk()
    app = CaPGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()


if __name__ == "__main__":
    main()
