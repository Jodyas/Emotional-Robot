# 任務計畫: 自動重置場景與重複播放功能 (Task ID: reset_and_replay)

## 任務目標
1. **自動重置場景 (Auto-Reset)**: 為了避免每次執行新生成的指令前都需要關閉並重新啟動 PyBullet 模擬器，我們將實作場景重置功能。在執行生成的程式碼之前，會自動將機械臂關節和杯子位置恢復到初始狀態。
2. **重複播放 (Replay)**: 在 GUI 新增一個「Replay」按鈕，讓使用者可以再次播放右側面板中目前已生成的 Python 程式碼，同樣在播放前會觸發自動重置。

## 修改範圍
1. `pybullet_env.py`:
   - 新增 `reset_scene(self)` 函式：
     - 重設 Kuka 手臂的所有關節至預設姿態。
     - 隨機重新產生杯子的座標，並透過 `p.resetBasePositionAndOrientation` 更新。
     - 呼叫 `self.env.deactivate_suction()` 清除吸盤效果（如果有吸住東西）。
     - 執行少量 `p.stepSimulation()` 使物理狀態穩定。

2. `main_gui.py`:
   - UI 區塊：在輸入列的按鈕區，新增 `replay_btn`（文字："🔁 Replay"）。
   - 事件處理：
     - 新增 `_on_replay(self)`：讀取 `self.code_text` 的內容，若有程式碼則在背景執行緒中呼叫執行。
     - 更新 `_pipeline`（針對 Run 按鈕）：在呼叫 `self.sim_env.run_code()` 前加入 `self.sim_env.reset_scene()`。
     - 新增背景負責 Replay 的專屬函式或共用執行邏輯，包含呼叫 `reset_scene()` 以及 `run_code()`。

## 驗證計畫
- 按下 Run 後，確認執行新程式碼前機械臂與杯子會歸位。
- 點擊 Replay 按鈕，確認系統能抓取當前生成的 code 再次執行，並且執行前同樣會把場景重置乾淨。
