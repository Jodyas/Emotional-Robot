# 任務計畫: 修復機械手臂重置後的異常姿態 (Task ID: fix_initial_posture)

## 任務目標
在執行 `PyBulletEnv.reset_scene()` 之後，機械手臂姿勢異常扭曲。這是因為 PyBullet 在物理模擬當中，如果我們只用 `p.resetJointState()` 強制修改關節角度，但手臂內部的 PD 控制器 (Position Control) 的 `targetPosition` 仍然停留在上一次執行動作結束時的位置。當 `p.stepSimulation()` 一被呼叫，控制器試圖把手臂拉回先前的目標位置，導致瞬間受力過大而產生扭曲。

我們必須在呼叫 `p.resetJointState()` 之後，同時使用 `p.setJointMotorControl2()` 將每個關節的位置控制目標也設定回預設的預備姿態 (rest_poses)。

## 修改範圍
1. `pybullet_env.py` - `reset_scene(self)`:
   - 在 `rest_poses` 迴圈內，除了呼叫 `p.resetJointState(self.robot_id, j, rest_poses[i])`，
   - 追加呼叫 `p.setJointMotorControl2(self.robot_id, j, p.POSITION_CONTROL, targetPosition=rest_poses[i], force=100)`

## 驗證計畫
修改完成後，在 GUI 點擊 `Replay` 開啟自動重置，確認重置時手臂會完美回到我們指定的 `[0, 0, 0, -math.pi / 2, 0, math.pi / 4, 0]` 初始位置，不會再發生奇異變形。
