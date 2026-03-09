# Emotional Robot

這是一套基於 **Code as Policies (CaP)** 概念建立的機器手臂協同模擬系統。利用大語言模型 (GPT-4o) 結合 Few-Shot learning，將使用者的自然語言指令（如："小心地把水杯拿起來"）動態且自動地轉換為可執行的 Python 機器人控制程式碼。最特別的是，系統會**自主推斷使用者話語中的情緒**，並隨之改變程式碼的寫法，從而在 PyBullet 模擬環境中呈現出細緻、緩慢，亦或快速、猛烈的多樣化物理動態表現。

## ⚙️ 系統架構與流程說明

整個大腦的運作流程可分為三個階段 (Stages)，全部由一支圖形化介面程式 `main_gui.py` 進行調度。

### Stage 1: 規劃階段 (Task Planner)
- **核心模組**: `planner.py`、`few_shots/planning_examples.py`
- **流程**: 
  1. 接收使用者輸入的環境指令。
  2. 根據指令的語氣，模型被授權進行**開放式情緒推論 (Open-Ended Emotion Inference)**（如判斷出語境為 `cautious`, `urgent`, `lazy` 或毫無情緒的 `neutral`）。
  3. LLM 扮演規劃器，將龐大的動作分解成由 `detect_object`, `move_above`, `pick_up`, `express_emotion` 組成的高階動作步驟。
  4. 最終強制輸出為一個乾淨嚴謹的 JSON 結構 `Steps JSON`。

### Stage 2: 程式碼生成階段 (Code Generator)
- **核心模組**: `code_generator.py`、`few_shots/coding_examples.py`
- **流程**:
  1. 接收 Planner 解析出的 `Steps JSON` 與目標情緒字眼。
  2. 根據情緒，模型會自己寫出一連串基於基本 API `env.move_arm(x, y, z, steps, force)` 組成的實體 Python 程式碼。
  3. 例如：當情緒為 `urgent` 時，生成器會明白它需要輸出較小的 `steps` (讓移動變快) 以及較大的 `force` (讓馬達出力更猛，甚至產生震動)。模型在此階段**完全自主發明**物理表現。
  4. 產出具有 `def execute(env):` 進入點的純 Python Code 字串。

### Stage 3: 模擬執行階段 (PyBullet Execution)
- **核心模組**: `pybullet_env.py`、`primitives.py`、`main_gui.py`
- **流程**:
  1. 當使用者按下 Run，GUI 透過背景執行緒開啟 PyBullet 模擬並載入 Kuka 手臂與水杯場景。
  2. 將 `RobotPrimitives` (定義了真實底層 IK 推算與吸盤功能的沙盒物件 `env`) 實例化。
  3. 動態執行 (`exec`) Stage 2 產生的程式碼，並在畫面上浮現目前演繹的情緒字眼，讓您可以看見手臂如何被情緒影響動作速度與力道。

---

## 🚀 安裝與啟動教學

### 1. 環境安裝與設定 (Environment Setup)

本專案使用 [Conda](https://docs.conda.io/en/latest/miniconda.html) 進行環境與套件的管理。請依照以下步驟建立執行環境：

- **安裝 Conda**
   如果你尚未安裝 Conda，請先下載並安裝 [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 或 [Anaconda](https://www.anaconda.com/download)。

- **建立虛擬環境**
   在專案的根目錄下（即包含 `environment.yml` 的資料夾），開啟終端機（如 Anaconda Prompt 或 PowerShell）並執行以下指令。這個過程需要一點時間，因為 Conda 會自動下載並安裝所有必要的套件：
   ```bash
   conda env create -f environment.yml
   ```

- **啟動環境**
   環境建立完成後，使用以下指令來啟動環境（這個環境名稱為 `cap_env`）：
   ```bash
   conda activate cap_env
   ```

- **(選用) 更新環境**
   如果日後專案有新增套件並更新了 `environment.yml`，你可以透過以下指令來同步更新原有的環境：
   ```bash
   conda env update -f environment.yml --prune
   ```

### 2. 設定 OpenAI API 金鑰

為了保護你的 API 金鑰不被意外上傳到 GitHub，請依照以下步驟設定：
1. 複製專案內的 `config.example.py` 檔案。
2. 將複製出來的檔案重新命名為 `config.py`。
3. 開啟 `config.py` 並填入你的 OpenAI API 金鑰：

```bash
# 在終端機/PowerShell快速複製：
cp config.example.py config.py
```

```python
# config.py 內容範例
OPENAI_API_KEY = "你的_OPEN_AI_API_KEY"
MODEL = "gpt-4o"

# PyBullet 場景參數
SCENE_CONFIG = {
    "gravity": -9.81,
    "camera_distance": 2.2,
    "camera_yaw": 50,
    "camera_pitch": -35,
    "camera_target": [0.45, 0, 0.3],
    "robot_base_position": [0, 0, 0.63],
    "table_position": [0.55, 0.0, 0.3],
    "table_half_extents": [0.70, 0.55, 0.3],
    "cup_radius": 0.03,
    "cup_height": 0.10,
    "cup_color": [0.2, 0.6, 1.0, 1.0],
    "cup_random_x_range": [0.70, 0.95],
    "cup_random_y_range": [-0.3, 0.3],
}
```

### 3. 啟動系統

直接透過 Python 執行您的主程式介面：

```bash
python main_gui.py
```

在開啟的介面中央上方，可以任意輸入指令如：
* `"Please pick up the cup, but I am very tired and lazy today."`
* `"Grab it right NOW!"`
* `"Take the cup carefully."`

按下 **Run** 後，靜待 Stage 1 和 Stage 2 介面刷新，便會看到 PyBullet 自動彈出畫面並執行充滿生命力的動作！
