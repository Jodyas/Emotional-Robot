# Stage 2: Code Generator
# 輸入：Steps JSON (dict from Stage 1) + emotion (str)
# 輸出：可執行的 Python 函數字串 def execute(env): ...
# 使用 GPT-4o + few-shot 生成程式碼

import json
from openai import OpenAI
from config import OPENAI_API_KEY, GOOGLE_API_KEY, OPENAI_MODEL, GEMINI_MODEL
from few_shots.coding_examples import get_coding_prompt_block

# primitives API 說明（提供給 LLM 的 context）
PRIMITIVES_API_DOC = """
You are a Python code generator mapping keyframe JSON steps to robot API movements.

The robot is controlled via an `env` object.
You MUST ONLY use the following methods. Do NOT import anything. Do NOT use any other functions or fake methods like `express_emotion`.

Available API:
  env.get_object_position(name: str) -> list[float]
      Returns [x, y, z] world coordinates of an object. Supported name: "cup".

  env.move_to(target: str | list[float], steps: int = 150, force: float = 200, noise_amp: float = 0.0, noise_freq: float = 0.0, tilt: list = None)
      Moves the robot arm end-effector to the target.
      `target` can be the string "cup" (it will automatically offset to hover above the cup) OR an absolute [x, y, z] coordinate list.
      `steps` determines the speed and smoothness. Less steps (e.g. 30-50) is fast/jerky. More steps (e.g. 80-120) is slow/smooth.
      `force` determines motor force. High force (e.g. 500-600) is aggressive.
      `noise_amp` and `noise_freq` control physical jitter/shaking. 
         - To tremble gently (like hesitation/caution), use noise_amp=0.01, noise_freq=0.5
         - To violently shake (angry/pain), use noise_amp=0.08, noise_freq=2.0
         - Default is 0.0 for smooth motion.
      `tilt` is a list [roll_offset, pitch_offset, yaw_offset] in radians, controlling the end-effector orientation.
         The base orientation points straight down. Tilt offsets rotate from there.
         Use tilt to give the robot "personality" like a character's head:
         - Curious side-tilt: tilt=[0, 0.3, 0]
         - Sad/drooping: tilt=[0.2, 0, 0]
         - Proud/looking up: tilt=[-0.2, 0, 0]
         - Angry sideways jerk: alternate tilt=[0, 0.4, 0] and tilt=[0, -0.4, 0]
         Default is None (straight down).

  env.activate_suction()
      Attaches the cup to the arm.

  env.deactivate_suction()
      Releases the cup from the arm, letting it fall.

  env.wait(steps: int = 50)
      Waits for the given number of simulation steps.

Animation & Physics Principles:
- Apply 'Show, Don't Tell' by converting physical properties into motion parameters.
- Heavy Objects: Require high `force=800`, very high `steps=200+` (slow movement), and a low-frequency heavy jitter `noise_amp=0.02, noise_freq=0.3`.
- Fragile/Careful: Require smooth slow movement `steps=120`, no noise `noise_amp=0.0`.
- Anticipation: Before moving, add a small reverse/away movement or a hovering `wait()` with tiny trembles.
- Follow Through: After dropping/picking, ALWAYS add a lingering movement (e.g., dropping hand heavily, or excitedly shaking).
- **Timing & Pacing**: Use `env.wait()` to insert dramatic beats between motions. Short beat: `steps=20-35`. Long dramatic pause: `steps=70-120`. NEVER skip pauses — the silences between actions are what make the animation feel alive.

Rules:
- Generate ONLY the body of def execute(env): — nothing else.
- Use only the API methods listed above.
- Add a brief comment before each step based on the description.
- To express emotions, you translate the step into `move_to` or `wait` commands with appropriate `steps`, `force`, `noise_amp`, and `noise_freq`.
  - 'happy' -> bouncing/waving motion, targeting coordinates above the table, fluid (steps=80-100).
  - 'angry/hot' -> smashing down forcefully (fast steps=30, high force), followed by chaotic `move_to` in the air with `noise_amp=0.1, noise_freq=2.0`.
  - 'cautious' -> very slow `move_to` (steps=150) with slight trembles (`noise_amp=0.005`).
- YOU MUST NOT CAUSE ERRORS by calling non-existent methods. All physical expressions of emotion described in the JSON must be "choreographed" using a loop or sequence of `move_to` to specific explicit coordinates [x, y, z].
"""


class CodeGenerator:
    """
    使用 GPT-4o + few-shot 將 Steps JSON 轉換為可執行的 Python Code。
    """

    def __init__(self, use_gemini: bool = False):
        self.use_gemini = use_gemini
        if use_gemini:
            self.client = OpenAI(
                api_key=GOOGLE_API_KEY,
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
            )
            self.model_name = GEMINI_MODEL
        else:
            self.client = OpenAI(api_key=OPENAI_API_KEY)
            self.model_name = OPENAI_MODEL

    def generate(self, steps_dict: dict, emotion: str) -> str:
        """
        根據 Steps JSON 和情緒生成 Python 程式碼。

        Args:
            steps_dict: Stage 1 輸出的 Steps JSON (含 steps 欄位)
            emotion:    情緒風格 ('happy' | 'angry')
        Returns:
            str: 完整的 def execute(env): 函數字串
        """
        steps_json_str = json.dumps(steps_dict.get("steps", []), indent=2)
        few_shot_block = get_coding_prompt_block()

        system_prompt = PRIMITIVES_API_DOC.strip()

        user_prompt = f"""
Here are few-shot examples of Steps JSON → Python code:

{few_shot_block}

---
Now generate Python code for the following:

Emotion: {emotion}
Steps JSON:
{steps_json_str}

Generate ONLY the def execute(env): function. No imports, no extra text.
""".strip()

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_prompt}
            ],
            temperature=0.1  # 極低溫度確保程式碼穩定
        )

        raw = response.choices[0].message.content.strip()

        # 清理 markdown code block（如果 GPT 回傳帶有 ```python ... ```）
        if raw.startswith("```"):
            lines = raw.split("\n")
            # 移除首行 ```python 和尾行 ```
            lines = [l for l in lines if not l.strip().startswith("```")]
            raw = "\n".join(lines)

        return raw.strip()
