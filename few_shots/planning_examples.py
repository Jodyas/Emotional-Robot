# Stage 1 Planning Few-shot Examples
# 每個 example 展示：instruction + emotion → CoT reasoning → Steps JSON
# 核心步驟為 3 步：確認位置(detect)、移動至上方(move_above)、拿起(pick_up)。可以在這三步之間自由插入 express_emotion。

PLANNING_EXAMPLES = [
    {
        "instruction": "Please pick up the cup very carefully.",
        "thinking": (
            "The user asked to pick up the cup 'very carefully'. "
            "I should perform the task with a 'cautious' emotion. "
            "[Show, Don't Tell]: To show caution, I'll use very slow target movements. "
            "[Anticipation]: Before moving, I pause and hover slightly to build hesitation. "
            "[Timing]: I insert wait() pauses between steps so the audience can read each pose. "
            "Next, I approach it very slowly and smoothly. "
            "I hold still above the cup to carefully check alignment before grabbing. "
            "I activate the suction and lift the cup gently. "
            "[Follow Through]: I MUST NOT end here. I will slowly pull the cup closer and hold it absolutely still to show extreme care."
        ),
        "emotion": "cautious",
        "steps": [
            {
                "action": "detect_object",
                "args": {"name": "cup"},
                "description": "Detect and confirm the cup position on the table."
            },
            {
                "action": "express_emotion",
                "args": {},
                "description": "Anticipation: Pause and hover slightly to show hesitation and extreme caution."
            },
            {
                "action": "wait",
                "args": {},
                "description": "Timing: Hold still — let the audience feel the hesitation before approaching."
            },
            {
                "action": "move_to",
                "args": {"target": "cup"},
                "description": "Move the arm very slowly and smoothly above the cup to avoid knocking it."
            },
            {
                "action": "wait",
                "args": {},
                "description": "Timing: Hold perfectly still above the cup, checking alignment before grabbing."
            },
            {
                "action": "pick_up",
                "args": {"object": "cup"},
                "description": "Lower the arm slowly, activate suction, lift the cup gently."
            },
            {
                "action": "wait",
                "args": {},
                "description": "Timing: Pause after lifting — let the audience see it is safely held."
            },
            {
                "action": "express_emotion",
                "args": {},
                "description": "Follow Through: Slowly bring the cup closer and hold it perfectly still, showing extreme care."
            }
        ]
    },
    {
        "instruction": "I need that cup immediately! Hurry up!",
        "thinking": (
            "The instruction uses 'Hurry up!', indicating urgency or impatience, but also mentions burning hot. "
            "I will map this to the 'angry_hot' emotion. "
            "[Anticipation]: Shake the arm rapidly in impatience before moving. "
            "[Show, Don't Tell]: To show speed and heat, I will rush to the cup, grab it quickly, then immediately drop it violently to simulate getting burned. "
            "[Timing]: After grabbing, I insert a brief freeze — the moment of realization that it's hot. Then chaos. "
            "[Follow Through]: I MUST NOT end here. Since it's hot, the follow-through is violently shaking the arm in the air in pain."
        ),
        "emotion": "angry_hot",
        "steps": [
            {
                "action": "detect_object",
                "args": {"name": "cup"},
                "description": "Detect and confirm the cup position on the table."
            },
            {
                "action": "express_emotion",
                "args": {},
                "description": "Anticipation: Shake the arm back and forth rapidly to show impatience."
            },
            {
                "action": "move_to",
                "args": {"target": "cup"},
                "description": "Rush the arm directly above the cup quickly and forcefully."
            },
            {
                "action": "pick_up",
                "args": {"object": "cup"},
                "description": "Slam the arm down fast, activate suction, then thrust the cup up quickly."
            },
            {
                "action": "wait",
                "args": {},
                "description": "Timing: Freeze! The moment of realization — it's burning hot!"
            },
            {
                "action": "move_to",
                "args": {"target": "drop"},
                "description": "Exaggeration: Rush the arm to the side in panic."
            },
            {
                "action": "deactivate_suction",
                "args": {},
                "description": "Drop the cup immediately!"
            },
            {
                "action": "wait",
                "args": {},
                "description": "Timing: Moment of shock after dropping. Hold still."
            },
            {
                "action": "express_emotion",
                "args": {},
                "description": "Follow Through: Violently shake the arm side to side in pain, trying to cool off."
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
