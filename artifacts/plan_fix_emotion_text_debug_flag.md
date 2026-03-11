# 任務計畫: 修復未啟用 debug 依舊顯示情緒文字 (Task ID: fix_emotion_text_debug_flag)

## 任務目標
使用者回報在執行 `main_gui.py -gemini` （未加上 `-debug` 參數）時，PyBullet 畫面中依舊會出現情緒浮空文字。
經查發現在上一次加入 `-debug` 旗標邏輯時，`pybullet_env.py` 的 `run_code` 方法內不小心留下了重複且無條件執行的 `self._show_emotion_text(emotion)`。這導致 `if debug:` 的防呆機制被後面的程式碼直接覆蓋而失效。

## 修改範圍
1. `pybullet_env.py` 中的 `run_code` 方法：
   - 刪除多餘且未受 `if debug:` 保護的：
     ```python
         # 暫停 idle_loop，避免 stepSimulation() race condition
         p.removeAllUserDebugItems()
         self._show_emotion_text(emotion)
     ```
   - 保留正確受保護的邏輯：
     ```python
         # 清除舊的 debug text 並顯示新情緒
         p.removeAllUserDebugItems()
         if debug:
             self._show_emotion_text(emotion)
     ```

## 驗證計畫
修改完成後，在沒有 `-debug` 參數的狀況下執行程式並點擊 Run，確保 PyBullet 不會因為預設情緒 (neutral) 或是生成的其他情緒而在畫面上印出 Debug Text。
