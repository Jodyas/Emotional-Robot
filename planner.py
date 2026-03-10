# Stage 1: Task Planner
# 輸入：instruction (str)
# 輸出：Steps JSON (dict)
# 使用 GPT-4o + CoT + few-shot 生成結構化動作步驟，並自動判斷情緒

import json
from openai import OpenAI
import config
from config import OPENAI_API_KEY, GOOGLE_API_KEY, OPENAI_MODEL, GEMINI_MODEL
from few_shots.planning_examples import get_planning_prompt_block

# 場景描述（提供給 LLM 的背景知識）
SCENE_DESCRIPTION = """
You are a Senior Animator planning keyframes for a Junior Animator who controls a robot arm simulation.
Your job is to translate the user's intended emotional expression into a series of highly detailed physical kinematic actions (keyframes).

Environment:
- A table in front of the robot arm.
- A water cup placed randomly on the table.
- A Kuka robot arm with a suction cup end-effector (no fingers).

Available robot actions for the Junior Animator (you must output steps that use these concepts):
  detect_object(name)                  - Detect and confirm object position ("cup").
  move_to(target)                      - Move arm to a target (can add physical noise trembling/shaking).
  pick_up(object)                      - Activate suction, lift object.
  deactivate_suction()                 - Release the object (drop it).
  wait()                               - Pause.
  express_emotion()                    - Perform an abstract physical choreography (shaking, waving) to show emotion.

Emotion detection:
- Identify the user's emotion from the instruction text.
- ONLY default to "neutral" if the instruction is completely neutral and lacks any emotional tone.

Animation Principles to Apply:
- **Show, Don't Tell**: Translate emotions and object properties (heavy, fragile, hot) into physical motion markers. Don't write "it is heavy"; instead, use slow speeds and heavy jitter.
- **Act Out Object Properties**: If the user's instruction implies a distinct physical property of the object (e.g., "slippery", "heavy", "hot"), you MUST physically "act out" that property using a sequence of actions. For example, to show "slippery", you should `pick_up` the object, briefly `deactivate_suction` to simulate slipping, and instantly `pick_up` again. This dramatic action sequence makes the property visceral.
- **Anticipation**: Before a sharp or forceful `move_to`, perform a slight counter-movement or pause (hesitation) to build energy.
- **Timing & Pacing**: DO NOT rush all actions together. Insert `wait()` pauses between keyframes to give the audience time to "read" each pose. A dramatic beat before a big action, a held pose after an impact — these silences are what make animation feel alive.
- **Exaggeration**: Amplify the emotional expression through extreme trembling (high noise) or extreme speeds.
- **Appeal**: The suction cup is the robot's "face". Describe how it should tilt or angle: curious side-tilt, drooping sadly, jerking away in disgust. The code generator will translate this into `tilt` parameters.
- **Follow Through**: Momentum continues after an action. You MUST end your sequence with a follow-through action.

Rules:
- Describe the steps as a detailed storyboard script that visually expresses the emotion using the Animation Principles.
- YOU MUST maintain the core sequence of actions: `detect_object` -> `move_to` (above cup) -> `pick_up`.
- You are ENCOURAGED and ALLOWED to insert `express_emotion`, `move_to`, or `wait` steps freely BEFORE or BETWEEN the core actions to demonstrate Anticipation and Timing.
- IMPORTANT: Insert `wait()` steps to create dramatic beats. For example: pause before grabbing (building tension), pause after picking up (showing the weight), pause after dropping (moment of shock).
- CRITICAL: You MUST ALWAYS add a final `express_emotion` or chaotic `move_to` step AT THE VERY END (after `pick_up` or dropping) to conclude the sequence. NEVER end perfectly on the `pick_up` or `deactivate_suction` step. You must perform "Follow Through".
- The "description" field must explicitly describe HOW to move (e.g., "Fast and jittery move_to", "Drop it suddenly", "Wave the arm rapidly", "Hold perfectly still — dramatic pause").
- The "emotion" field in the JSON MUST reflect your detected emotion.
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
            model=self.model_name,
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
