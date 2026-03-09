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
You are a Python code generator for a robot arm simulation.

The robot is controlled via an `env` object (RobotPrimitives instance).
You MUST ONLY use the following methods. Do NOT import anything. Do NOT use any other functions.

Available API:
  env.get_object_position(name: str) -> list[float]
      Returns [x, y, z] world coordinates of an object. Supported name: "cup".

  env.move_arm(x: float, y: float, z: float, steps: int = 200, force: float = 200)
      Moves the robot arm end-effector to (x, y, z).
      `steps` determines the speed and smoothness. Fewer steps (e.g., 40-50) mean fast, abrupt, and jerky movement. More steps (e.g., 200-250) mean slow, smooth movement.
      `force` determines the physical force applied to the joints. High force (e.g., 500-600) is good for aggressive or forceful actions.

  env.activate_suction()
      Attaches the cup to the arm using a virtual suction constraint.

  env.deactivate_suction()
      Releases the cup from the arm.

  env.wait(steps: int = 50)
      Waits for the given number of simulation steps.

Rules:
- Generate ONLY the body of def execute(env): — nothing else.
- Use only the API methods listed above.
- Add a brief comment before each step.
- The output must be valid Python code starting with: def execute(env):
- To express emotions, you MUST NOT call 'express_emotion', rather you sequence a series of `env.move_arm` instructions adjusting `steps` and `force` to physically match the target emotion. 
- For example:
  - 'happy' -> waving motion, fluid (steps=250)
  - 'angry' -> smashing down/up forcefully (steps=40, force=600)
  - 'lazy' -> moving very slowly, dragging the cup (steps=500, force=100)
  - 'cautious' / 'careful' -> small precise movements, pausing frequently
  - YOU must invent the physical choreography for ANY emotion passed in.
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
