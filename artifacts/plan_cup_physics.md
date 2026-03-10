# 任務計畫: 調整杯子物理屬性 (Task ID: cup_physics)

## 任務目標
調高水杯的質量與摩擦係數，避免機械臂觸碰時水杯輕易飛出。

## 修改範圍
1. `config.py`:
   - 增加 `cup_mass`: 0.5 (提高質量)
   - 增加 `cup_friction`: 1.0 (提高摩擦係數)

2. `pybullet_env.py`:
   - 於 `_create_cup` 函式中，透過 `SCENE_CONFIG` 讀取並指派 `baseMass`。
   - 在建立水杯 `cup_id` 後，呼叫 `p.changeDynamics(cup_id, -1, lateralFriction=cfg["cup_friction"], spinningFriction=0.1, rollingFriction=0.1)` 來設定摩擦係數。
   
## 驗證計畫
修改完成後，將透過測試機器手臂碰觸杯子，驗證杯子具有穩定的物理反應，不會像原本那樣隨意飛離桌面。
