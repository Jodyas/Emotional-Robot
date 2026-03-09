# Stage 1 Planning Few-shot Examples
# 每個 example 展示：instruction + emotion → CoT reasoning → Steps JSON
# 步驟固定為 4 步：確認位置、情緒化移動、拿起杯子、表達情緒

PLANNING_EXAMPLES = [
    {
        "instruction": "Please pick up the cup very carefully.",
        "thinking": (
            "The user asked to pick up the cup 'very carefully'. "
            "I should perform the task with a 'cautious' or 'careful' emotion. "
            "First, I confirm the cup's location on the table. "
            "Then I approach it very slowly and smoothly to avoid knocking it over. "
            "I activate the suction and lift the cup gently. "
            "Finally, I express caution by moving it slowly to the side and pausing."
        ),
        "emotion": "cautious",
        "steps": [
            {
                "action": "detect_object",
                "args": {"name": "cup"},
                "description": "Detect and confirm the cup position on the table."
            },
            {
                "action": "move_above",
                "args": {"object": "cup", "offset_z": 0.20},
                "description": "Move the arm very slowly and smoothly above the cup to avoid knocking it."
            },
            {
                "action": "pick_up",
                "args": {"object": "cup"},
                "description": "Lower the arm slowly, activate suction, then lift the cup gently."
            },
            {
                "action": "express_emotion",
                "args": {},
                "description": "Slowly move the arm to the side and hold it still to show extreme care."
            }
        ]
    },
    {
        "instruction": "I need that cup immediately! Hurry up!",
        "thinking": (
            "The instruction uses 'immediately' and 'Hurry up!', indicating urgency or impatience. "
            "I will map this to the 'urgent' emotion. "
            "I confirm the cup location, then rush toward it. "
            "I grab it quickly and thrust upward to show speed and impatience."
        ),
        "emotion": "urgent",
        "steps": [
            {
                "action": "detect_object",
                "args": {"name": "cup"},
                "description": "Detect and confirm the cup position on the table."
            },
            {
                "action": "move_above",
                "args": {"object": "cup", "offset_z": 0.20},
                "description": "Rush the arm directly above the cup quickly and forcefully."
            },
            {
                "action": "pick_up",
                "args": {"object": "cup"},
                "description": "Slam the arm down fast, activate suction, then thrust the cup up quickly."
            },
            {
                "action": "express_emotion",
                "args": {},
                "description": "Shake the arm back and forth rapidly to signify being hurried."
            }
        ]
    }
]


def get_planning_prompt_block() -> str:
    """
    將 few-shot examples 格式化為 prompt 文字區塊
    Returns a formatted string to be injected into the planner prompt.
    """
    blocks = []
    for ex in PLANNING_EXAMPLES:
        steps_str = "\n".join(
            f"  Step {i+1}: {s['action']}({s['args']}) — {s['description']}"
            for i, s in enumerate(ex["steps"])
        )
        block = (
            f"---\n"
            f"Instruction: \"{ex['instruction']}\"\n"
            f"Emotion: {ex['emotion']}\n"
            f"Thinking: {ex['thinking']}\n"
            f"Steps:\n{steps_str}"
        )
        blocks.append(block)
    return "\n\n".join(blocks)
