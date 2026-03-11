# PyBullet 模擬環境
# 負責建立場景（桌子、杯子、機器手臂），並提供 run_code() 執行 LLM 生成的 code

import pybullet as p
import pybullet_data
import time
import math
import random
import threading
import os
import shutil

from config import SCENE_CONFIG
from primitives import RobotPrimitives


class PyBulletEnv:
    """
    PyBullet 場景管理器。
    建立：地板、桌子、Kuka 機器手臂、水杯。
    提供 run_code() 方法執行 LLM 生成的 Python 函數。
    """

    def __init__(self):
        self.physics_client = None
        self.robot_id = None
        self.cup_id = None
        self.table_id = None
        self.env = None              # RobotPrimitives instance（供 LLM code 使用）
        self._sim_thread = None
        self._running = False
        self._paused = False         # 執行 code 時暫停 idle_loop，避免 race condition

    # ------------------------------------------------------------------
    # Scene Setup
    # ------------------------------------------------------------------

    def setup(self):
        """
        初始化 PyBullet 場景：連線、載入模型、建立物件。
        """
        cfg = SCENE_CONFIG

        # 連線 PyBullet GUI
        self.physics_client = p.connect(p.GUI)
        
        # 處理中文路徑導致 loadURDF 失敗的 Bug
        data_path = pybullet_data.getDataPath()
        if not data_path.isascii():
            temp_dir = r"C:\temp\pybullet_data_temp"
            if not os.path.exists(temp_dir):
                os.makedirs(r"C:\temp", exist_ok=True)
                print(f"[PyBulletEnv] Copying pybullet_data to {temp_dir} to bypass non-ASCII path issue...")
                shutil.copytree(data_path, temp_dir)
            data_path = temp_dir
            print(f"[PyBulletEnv] Using temporary ASCII data path: {data_path}")
            
        p.setAdditionalSearchPath(data_path)
        p.setGravity(0, 0, cfg["gravity"])

        # 攝影機設定
        p.resetDebugVisualizerCamera(
            cameraDistance=cfg["camera_distance"],
            cameraYaw=cfg["camera_yaw"],
            cameraPitch=cfg["camera_pitch"],
            cameraTargetPosition=cfg["camera_target"]
        )

        # 載入地板
        p.loadURDF("plane.urdf")

        # 建立桌子（使用 box 碰撞形體）
        self.table_id = self._create_table(
            position=cfg["table_position"],
            half_extents=cfg["table_half_extents"]
        )

        # 載入 Kuka 機器手臂（放在桌面上）
        self.robot_id = p.loadURDF(
            "kuka_iiwa/model.urdf",
            basePosition=cfg["robot_base_position"],
            useFixedBase=True
        )

        # 設定手臂關節
        self.ee_link = 6
        self.arm_joints = [0, 1, 2, 3, 4, 5, 6]

        # 手臂歸零到預備姿勢
        rest_poses = [0, 0, 0, -math.pi / 2, 0, math.pi / 4, 0]
        for i, j in enumerate(self.arm_joints):
            p.resetJointState(self.robot_id, j, rest_poses[i])
        for _ in range(100):
            p.stepSimulation()

        # 建立水杯（隨機位置在桌面上）
        self.cup_id = self._create_cup()

        # 建立 RobotPrimitives instance（提供給 LLM code 使用）
        self.env = RobotPrimitives(
            robot_id=self.robot_id,
            cup_id=self.cup_id,
            ee_link=self.ee_link,
            arm_joints=self.arm_joints
        )

        self._running = True

    def _create_table(self, position: list, half_extents: list) -> int:
        """建立桌子（木頭色長方體）"""
        col_id = p.createCollisionShape(p.GEOM_BOX, halfExtents=half_extents)
        vis_id = p.createVisualShape(
            p.GEOM_BOX, halfExtents=half_extents,
            rgbaColor=[0.9, 0.85, 0.75, 1.0]  # 木頭色
        )
        table_id = p.createMultiBody(
            baseMass=0,               # 靜態（質量=0）
            baseCollisionShapeIndex=col_id,
            baseVisualShapeIndex=vis_id,
            basePosition=position
        )
        return table_id

    def _create_cup(self) -> int:
        """在桌面上隨機位置建立水杯（藍色圓柱體）"""
        cfg = SCENE_CONFIG
        table_top_z = cfg["table_position"][2] + cfg["table_half_extents"][2]
        cup_z = table_top_z + cfg["cup_height"] / 2.0

        rand_x = random.uniform(*cfg["cup_random_x_range"])
        rand_y = random.uniform(*cfg["cup_random_y_range"])

        col_id = p.createCollisionShape(
            p.GEOM_CYLINDER,
            radius=cfg["cup_radius"],
            height=cfg["cup_height"]
        )
        vis_id = p.createVisualShape(
            p.GEOM_CYLINDER,
            radius=cfg["cup_radius"],
            length=cfg["cup_height"],
            rgbaColor=cfg["cup_color"]
        )
        cup_id = p.createMultiBody(
            baseMass=cfg.get("cup_mass", 0.5),
            baseCollisionShapeIndex=col_id,
            baseVisualShapeIndex=vis_id,
            basePosition=[rand_x, rand_y, cup_z]
        )
        p.changeDynamics(
            cup_id,
            -1,
            lateralFriction=cfg.get("cup_friction", 1.0),
            spinningFriction=0.1,
            rollingFriction=0.1
        )
        return cup_id

    # ------------------------------------------------------------------
    # Emotion Debug Text（顯示在 PyBullet 視窗中）
    # ------------------------------------------------------------------

    def _show_emotion_text(self, emotion: str):
        """在 PyBullet 視窗中顯示情緒標示"""
        label_map = {
            "happy": ("HAPPY  :)", [0.2, 0.9, 0.2]),   # 綠色
            "angry": ("ANGRY  >:(", [0.9, 0.2, 0.2]),  # 紅色
            "neutral": ("NEUTRAL", [0.8, 0.8, 0.8])    # 灰色
        }
        
        # 如果是字典裡找不到的未知情緒，就直接轉大寫並用白色顯示
        if emotion in label_map:
            text, color = label_map[emotion]
        else:
            text, color = (emotion.upper(), [1.0, 1.0, 1.0])

        p.addUserDebugText(
            text,
            textPosition=[0.0, -0.5, 1.2],
            textColorRGB=color,
            textSize=2.5,
            lifeTime=0  # 永遠顯示直到清除
        )

    # ------------------------------------------------------------------
    # Emotion Debug Text（顯示在 PyBullet 視窗中）
    # ------------------------------------------------------------------

    def _show_emotion_text(self, emotion: str):
        """在 PyBullet 視窗中顯示情緒標示"""
        label_map = {
            "happy": ("HAPPY  :)", [0.2, 0.9, 0.2]),   # 綠色
            "angry": ("ANGRY  >:(", [0.9, 0.2, 0.2]),  # 紅色
            "neutral": ("NEUTRAL", [0.8, 0.8, 0.8])    # 灰色
        }
        
        # 如果是字典裡找不到的未知情緒，就直接轉大寫並用白色顯示
        if emotion in label_map:
            text, color = label_map[emotion]
        else:
            text, color = (emotion.upper(), [1.0, 1.0, 1.0])

        p.addUserDebugText(
            text,
            textPosition=[0.0, -0.5, 1.2],
            textColorRGB=color,
            textSize=2.5,
            lifeTime=0  # 永遠顯示直到清除
        )

    # ------------------------------------------------------------------
    # Code Execution（執行前暫停 idle_loop，避免 race condition）
    # ------------------------------------------------------------------

    def run_code(self, code_str: str, emotion: str = "happy", status_callback=None, debug: bool = False):
        """
        在沙盒環境內執行 LLM 生成的 Python 程式碼。
        沙盒只注入 'env'（RobotPrimitives），禁止其他系統呼叫。

        Args:
            code_str:        LLM 生成的完整 Python code（包含 def execute(env):）
            emotion:         情緒（用於顯示 debug text）
            status_callback: 狀態更新回呼函數（用於 GUI 更新）
            debug:           是否顯示情緒 debug 文字 (預設 False)
        """
        # 清除舊的 debug text 並顯示新情緒
        p.removeAllUserDebugItems()
        if debug:
            self._show_emotion_text(emotion)

        # 暫停 idle_loop，避免 stepSimulation() race condition
        p.removeAllUserDebugItems()
        self._show_emotion_text(emotion)

        # 暫停 idle_loop，避免 stepSimulation() race condition
        self._paused = True
        time.sleep(0.05)

        try:
            if status_callback:
                status_callback("⚙️ Executing generated code in PyBullet...")

            # 沙盒：只允許 env 物件
            sandbox = {"env": self.env}
            exec(code_str, sandbox)

            if "execute" not in sandbox:
                raise RuntimeError("Generated code must define a function named 'execute(env)'.")

            sandbox["execute"](self.env)

            if status_callback:
                status_callback("✅ Execution complete!")

        except Exception as e:
            if status_callback:
                status_callback(f"❌ Execution error: {e}")
            raise

        finally:
            # 恢復 idle_loop
            self._paused = False

    # ------------------------------------------------------------------
    # Idle Loop（保持 PyBullet 視窗存活，支援暫停）
    # ------------------------------------------------------------------

    def idle_loop(self):
        """背景持續 step simulation，執行 code 時自動暫停"""
        while self._running and p.isConnected():
            if not self._paused:
                p.stepSimulation()
                time.sleep(1.0 / 240.0)
            else:
                time.sleep(0.01)

    def start_idle(self):
        """啟動背景 idle thread"""
        self._sim_thread = threading.Thread(target=self.idle_loop, daemon=True)
        self._sim_thread.start()

    def disconnect(self):
        """關閉 PyBullet 連線"""
        self._running = False
        if p.isConnected():
            p.disconnect()
