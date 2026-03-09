# Robot Primitives API
# 提供機器手臂的基本動作，供 LLM 生成的 code 呼叫
# 情緒差異設計：
#   Happy — 緩慢、流暢、大幅慶祝擺動
#   Angry — 極速、生硬、爆發性衝刺 + 震動

import pybullet as p
import time
import math


class RobotPrimitives:
    """
    機器手臂的基本動作 API。
    由 pybullet_env.py 初始化後傳入 exec() 沙盒，
    LLM 生成的 code 只能透過這個物件操作手臂。
    """

    def __init__(self, robot_id: int, cup_id: int, ee_link: int, arm_joints: list):
        self.robot_id = robot_id
        self.cup_id = cup_id
        self.ee_link = ee_link
        self.arm_joints = arm_joints
        self._suction_constraint = None

    # ------------------------------------------------------------------
    # Internal: Low-level IK Move
    # ------------------------------------------------------------------

    def move_arm(self, x: float, y: float, z: float, steps: int = 200, force: float = 200):
        """
        移動手臂末端到目標座標：直接用 IK 移動到目標，完整執行 steps 步。
        steps 越少 = 越快越生硬，steps 越多 = 越慢越流暢。
        force = 馬達輸出力道，數字越大越猛烈。
        """
        target_orn = p.getQuaternionFromEuler([math.pi, 0, 0])
        for _ in range(steps):
            joint_poses = p.calculateInverseKinematics(
                self.robot_id, self.ee_link, [x, y, z], target_orn,
                maxNumIterations=200
            )
            for i, j in enumerate(self.arm_joints):
                p.setJointMotorControl2(
                    self.robot_id, j, p.POSITION_CONTROL,
                    targetPosition=joint_poses[i], force=force
                )
            p.stepSimulation()
            time.sleep(1.0 / 240.0)

    # ------------------------------------------------------------------
    # Core Primitives
    # ------------------------------------------------------------------

    def get_object_position(self, name: str) -> list:
        """
        取得物件的世界座標 [x, y, z]。
        目前只支援 'cup'。
        """
        if name == "cup":
            pos, _ = p.getBasePositionAndOrientation(self.cup_id)
            return list(pos)
        raise ValueError(f"Unknown object: {name}")

    def activate_suction(self):
        """
        啟動吸盤：建立 fixed constraint 將杯子綁定到手臂末端。
        """
        if self._suction_constraint is not None:
            return

        cup_pos, _ = p.getBasePositionAndOrientation(self.cup_id)
        ee_state = p.getLinkState(self.robot_id, self.ee_link)
        ee_pos = ee_state[0]
        offset_z = cup_pos[2] - ee_pos[2] + 0.05

        self._suction_constraint = p.createConstraint(
            parentBodyUniqueId=self.robot_id,
            parentLinkIndex=self.ee_link,
            childBodyUniqueId=self.cup_id,
            childLinkIndex=-1,
            jointType=p.JOINT_FIXED,
            jointAxis=[0, 0, 0],
            parentFramePosition=[0, 0, 0],
            childFramePosition=[0, 0, offset_z]
        )

    def deactivate_suction(self):
        """關閉吸盤：移除 constraint，讓杯子受重力下落。"""
        if self._suction_constraint is not None:
            p.removeConstraint(self._suction_constraint)
            self._suction_constraint = None

    def wait(self, steps: int = 50):
        """等待指定的模擬步數。"""
        for _ in range(steps):
            p.stepSimulation()
            time.sleep(1.0 / 240.0)
