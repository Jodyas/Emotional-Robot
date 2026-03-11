# 任務計畫: 修復動畫節奏過慢的問題 (Task ID: fix_slow_pacing)

## 任務目標
使用者反映最近產出的程式碼執行動畫時停頓太久，節奏變得很慢。
經查發現，使用者曾在 `few_shots/coding_examples.py` 中將 `env.wait()` 的數值調低（例如從 30 降到 20，70 降到 50），以使得預設的節奏變快。然而，在 `code_generator.py` 提供給 LLM 的 `PRIMITIVES_API_DOC` 提示詞中，目前仍然寫著：
`Long dramatic pause: steps=150-250`。

這導致 LLM 在遇到需要停頓的步驟時，依然會根據提示詞生成非常大的數值（150-250），大約等同於 0.6 到 1 秒的停頓，造成了動畫節奏拖沓的問題。我們必須統一這個標準。

## 修改範圍
1. `code_generator.py` 中的 `PRIMITIVES_API_DOC`:
   - 修改 `env.wait()` 相關說明的推薦參數。
   - 將 **Short beat** 從 `steps=30-50` 調整為 `steps=15-30`。
   - 將 **Long dramatic pause** 從 `steps=150-250` 調整為 `steps=40-80`（與使用者在 few-shots 中的改動相對應）。

## 驗證計畫
修改完成後，再次執行產生指令，觀察 LLM 產生的 `env.wait()` 的數值是否落在 15~80 這個較為精簡的範圍中，確保動畫恢復流暢的動作節奏。
