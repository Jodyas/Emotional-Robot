# Stage 1: Task Planner
# 輸入：instruction (str)
# 輸出：Steps JSON (dict)
# 使用 GPT-4o + CoT + few-shot 生成結構化動作步驟，並自動判斷情緒

import json
from openai import OpenAI
from config import OPENAI_API_KEY, MODEL
from few_shots.planning_examples import get_planning_prompt_block

# 場景描述（提供給 LLM 的背景知識）
SCENE_DESCRIPTION = """
You are a task planner for a robot arm simulation.

Environment:
- A table in front of the robot arm.
- A water cup placed randomly on the table.
- A Kuka robot arm with a suction cup end-effector (no fingers).

Available robot actions:
  detect_object(name)                  - Detect and confirm object position ("cup").
  move_above(object, offset_z)         - Move arm above an object.
  pick_up(object)                      - Lower arm, activate suction, lift object.

Emotion detection:
- Identify the user's emotion from the instruction text.
- If the instruction strongly conveys an emotion (e.g., sad, lazy, cautious, excited, eager, happy, angry), infer that emotion as a single lowercase word.
- ONLY default to "neutral" if the instruction is completely neutral and lacks any emotional tone.

Rules:
- Describe the steps required to complete the task and express the emotion.
- Rather than a style parameter, YOU must explicitly generate steps that describe HOW to move (e.g., "Move the arm slowly and heavily", "Quickly and forcefully slam the arm").
- The "emotion" field in the JSON MUST reflect your detected emotion (any valid emotion word, or "neutral").
- Emotion shapes HOW each step is performed and what extra physical expression steps are taken at the end.
- Output ONLY valid JSON. No extra text outside the JSON block.
"""

# JSON 輸出格式說明
OUTPUT_FORMAT = """
Output format (strict JSON):
{
  "reasoning": "<your chain-of-thought reasoning>",
  "emotion": "<emotion>",
  "steps": [
    {"action": "<action_name>", "args": {<args>}, "description": "<what this step does, including speed, force or movement pattern>"},
    ...
  ]
}
"""


class TaskPlanner:
    """
    使用 GPT-4o + CoT + few-shot 將自然語言指令轉換為 Steps JSON。
    """

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def plan(self, instruction: str) -> dict:
        """
        根據指令自動判斷情緒並生成執行步驟。

        Args:
            instruction: 自然語言指令（例如 "Happily pick up the cup"）
        Returns:
            dict: Steps JSON，包含 reasoning, emotion, steps 欄位
        """
        few_shot_block = get_planning_prompt_block()

        system_prompt = SCENE_DESCRIPTION.strip()

        user_prompt = f"""
Here are few-shot examples of how to plan tasks and detect emotion:

{few_shot_block}

---
Now plan the following task:

Instruction: "{instruction}"

Think step by step to identify the emotion and the steps, then output the Steps JSON.

{OUTPUT_FORMAT}
""".strip()

        response = self.client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_prompt}
            ],
            temperature=0.2,  # 低溫度確保輸出穩定一致
            response_format={"type": "json_object"}  # 強制輸出 JSON
        )

        content = response.choices[0].message.content
        result = json.loads(content)
        return result
