"""
Benchmark: Verify timeBeginPeriod(1) fix for Windows sleep precision.
"""
import pybullet as p
import pybullet_data
import time
import math
import os
import shutil
import ctypes

# Enable high-resolution timer (the fix we're testing)
ctypes.windll.winmm.timeBeginPeriod(1)

physics_client = p.connect(p.GUI)
data_path = pybullet_data.getDataPath()
if not data_path.isascii():
    data_path = r"C:\temp\pybullet_data_temp"
p.setAdditionalSearchPath(data_path)
p.setGravity(0, 0, -9.81)
p.loadURDF("plane.urdf")
robot_id = p.loadURDF("kuka_iiwa/model.urdf", basePosition=[0.0, -0.3, 0.65], useFixedBase=True)

ee_link = 6
arm_joints = [0, 1, 2, 3, 4, 5, 6]
rest_poses = [0, 0, 0, -math.pi / 2, 0, math.pi / 4, 0]
for i, j in enumerate(arm_joints):
    p.resetJointState(robot_id, j, rest_poses[i])

target = [0.3, 0.1, 1.0]
target_orn = p.getQuaternionFromEuler([math.pi, 0, 0])
steps = 25

print(f"\n=== WITH timeBeginPeriod(1): steps={steps} ===\n")

total_start = time.perf_counter()
for k in range(steps):
    joint_poses = p.calculateInverseKinematics(robot_id, ee_link, target, target_orn, maxNumIterations=200)
    for i, j in enumerate(arm_joints):
        p.setJointMotorControl2(robot_id, j, p.POSITION_CONTROL, targetPosition=joint_poses[i], force=700)
    p.stepSimulation()
    time.sleep(1.0 / 240.0)

total = time.perf_counter() - total_start
expected = steps / 240.0
print(f"  Total:    {total*1000:.1f}ms  (expected: {expected*1000:.1f}ms)")
print(f"  Avg/step: {total/steps*1000:.2f}ms")
print(f"  Slowdown: {total/expected:.2f}x")

time.sleep(1)
p.disconnect()
ctypes.windll.winmm.timeEndPeriod(1)
