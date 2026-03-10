# 任務計畫: 讓 Planner 學會「演繹」物件屬性 (Task ID: act_properties)

## 任務目標
修改 `planner.py` 中的提示詞 (prompt)，讓 LLM 能夠在規劃動作步驟時，主動「演出」物件的物理屬性，而不需要將具體動作寫死在 few-shot examples 中。

例如：當使用者輸入 "Pick up the slippery cup"，LLM 應該要知道透過「拿起 -> 放開 (deactivate suction) -> 馬上再拿起」的動作序列來表現「很滑」的這個屬性。

## 修改範圍
1. `planner.py`:
   - 在 `SCENE_DESCRIPTION` 中的 `Animation Principles to Apply` 區塊，新增一個與「物件屬性演繹 (Acting out object properties)」相關的準則。
   - 準則內容將指示 LLM：當遇到具有特殊屬性（如 slippery, heavy, fragile）的物件時，必須透過連續動作的組合（例如：短暫掉落再接住，來表現 slippery）來展示該屬性，將屬性轉化為戲劇化的物理表現。

## 驗證計畫
修改完成後，將透過測試 "Pick up the slippery cup" 指令，確保生成的動作列表中包含嘗試拿起後滑落，再度拿起的 sequences。
