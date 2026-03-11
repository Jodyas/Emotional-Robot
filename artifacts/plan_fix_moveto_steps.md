# 任務計畫: 修復 move_to 動作步數過多導致節奏拖沓的問題 (Task ID: fix_moveto_steps)

## 任務目標
使用者反映雖然已經把 `env.wait()` 的停頓時間調短，但整體的 pacing (節奏) 和 timing 還是有些拖沓。
經查發現，罪魁禍首是除了 `wait` 之外，**手臂移動本身 `env.move_to` 的 `steps` 設定也偏大**。
在 PyBullet 中，預設物理引擎頻率是 240Hz，因此 `steps=240` 大約等於移動過程耗時 1 秒鐘。

目前在 `code_generator.py` 的 `PRIMITIVES_API_DOC` 中，給 LLM 的推薦數值非常大：
- `steps=200` (slow/smooth, default) -> 約 0.83 秒
- `steps=300` (Fragile/Careful) -> 約 1.25 秒
- `steps=400` (cautious) -> 約 1.6 秒
- `steps=500+` (Heavy Objects) -> 大於 2 秒

此外，在 `few_shots/coding_examples.py` 中，`cautious` 的範例也大量使用了 `steps=200` 和 `steps=300`，這導致當 LLM 模仿範例或遵照文件時，每一個單獨的移動都會花費將近 1~2 秒，串聯起來就顯得非常拖泥帶水。

## 修改範圍
1. `code_generator.py` 中的 `PRIMITIVES_API_DOC`:
   - 將平滑移動定義 `More steps (e.g. 200)` 修改為 `(e.g. 100)`.
   - 將 Heavy Objects `steps=500+` 修改為 `steps=200+`.
   - 將 Fragile/Careful `steps=300` 修改為 `steps=120`.
   - 將 'happy' `steps=200` 修改為 `steps=90`.
   - 將 'cautious' `steps=400` 修改為 `steps=150`.

2. `few_shots/coding_examples.py` (選擇性跟進):
   - 將 `cautious` 情境中的 `steps=200` 減半為 `100`，`steps=300` 減半為 `150`。

## 驗證計畫
修改完成後，將能強制 LLM 不再生成高達數百的 `steps` 來移動手臂，所有的位移都會在 1 秒以內完成，動畫節奏會變得相當緊湊俐落。
