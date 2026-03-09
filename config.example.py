# 系統設定檔：OpenAI API Key、模型名稱、情緒參數

OPENAI_API_KEY = "請在這裡填入你的_OPEN_AI_API_KEY"
GOOGLE_API_KEY = "請在這裡填入你的_GOOGLE_API_KEY"

# 使用的模型
OPENAI_MODEL = "gpt-4o"
GEMINI_MODEL = "gemini-2.5-flash"

# PyBullet 場景參數
SCENE_CONFIG = {
    "gravity": -9.81,
    "camera_distance": 2.2,
    "camera_yaw": 50,
    "camera_pitch": -35,
    "camera_target": [0.45, 0, 0.3],
    "robot_base_position": [0, 0, 0.63],  # 手臂放在桌上（左側）
    "table_position": [0.55, 0.0, 0.3],
    "table_half_extents": [0.70, 0.55, 0.3],  # 桌子加大：1.4m × 1.1m
    "cup_radius": 0.03,
    "cup_height": 0.10,
    "cup_color": [0.2, 0.6, 1.0, 1.0],   # 藍色水杯
    "cup_random_x_range": [0.70, 0.95],   # 杯子距手臂更遠（右側）
    "cup_random_y_range": [-0.3, 0.3],
}
