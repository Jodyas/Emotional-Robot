# 任務計畫: 儲存生成結果 (Task ID: dump_results)

## 任務目標
在 `main_gui.py` 的管線執行過程中，將 Planner 生成的 JSON 結果與 Code Generator 產生的 Python 程式碼，儲存到專門的 `result` 目錄中，並以執行的時間戳記（Timestamp）作為檔名方便未來查閱。

## 修改範圍
1. `main_gui.py`:
   - 在檔案開頭匯入 `os` 以及 `time` 模組。
   - 在 `_pipeline` 方法的 Stage 2 (Code Generation) 結束後，加入儲存邏輯。
   - 確保 `result` 資料夾存在：`os.makedirs("result", exist_ok=True)`
   - 取得當前時間戳記：`timestamp = time.strftime("%Y%m%d_%H%M%S")`
   - 將 `plan_json` 寫入 `result/<timestamp>_plan.json`
   - 將 `code_str` 寫入 `result/<timestamp>_code.py`

## 驗證計畫
修改完成後，未來每次於 GUI 中點擊 Run 按鈕時，`result` 目錄下都會成對地產生計畫紀錄檔以及程式碼記錄檔。
