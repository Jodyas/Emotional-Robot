# Stage 2 Code Generation Few-shot Examples
# 每個 example 展示：Steps JSON + emotion → def execute(env): ...
# env 是 RobotPrimitives 的 instance，只允許呼叫 primitives API

import json

CODING_EXAMPLES = [
    {
        "emotion": "cautious",
        "steps": [
            {"action": "detect_object",   "args": {"name": "cup"}},
            {"action": "move_above",      "args": {"object": "cup", "offset_z": 0.20}},
            {"action": "pick_up",         "args": {"object": "cup"}},
            {"action": "express_emotion", "args": {}}
        ],
        "code": '''\
def execute(env):
    # Step 1: Detect and confirm cup position
    cup_pos = env.get_object_position("cup")

    # Step 2: Move above the cup very slowly and smoothly to avoid knocking it (high steps, low force)
    env.move_arm(cup_pos[0], cup_pos[1], cup_pos[2] + 0.20, steps=400, force=100)

    # Step 3: Lower arm carefully, activate suction, lift cup gently
    env.move_arm(cup_pos[0], cup_pos[1], cup_pos[2] + 0.05, steps=300, force=100)
    env.activate_suction()
    env.wait(80)
    env.move_arm(cup_pos[0], cup_pos[1], cup_pos[2] + 0.30, steps=400, force=100)

    # Step 4: Express caution by moving it slowly to the side and pausing
    env.move_arm(cup_pos[0] + 0.15, cup_pos[1], cup_pos[2] + 0.30, steps=300, force=100)
    env.wait(100)
'''
    },
    {
        "emotion": "urgent",
        "steps": [
            {"action": "detect_object",   "args": {"name": "cup"}},
            {"action": "move_above",      "args": {"object": "cup", "offset_z": 0.20}},
            {"action": "pick_up",         "args": {"object": "cup"}},
            {"action": "express_emotion", "args": {}}
        ],
        "code": '''\
def execute(env):
    # Step 1: Detect and confirm cup position
    cup_pos = env.get_object_position("cup")

    # Step 2: Rush the arm above the cup quickly and forcefully (low steps, high force)
    env.move_arm(cup_pos[0], cup_pos[1], cup_pos[2] + 0.20, steps=40, force=500)

    # Step 3: Slam down fast, activate suction, thrust cup upward quickly
    env.move_arm(cup_pos[0], cup_pos[1], cup_pos[2] + 0.05, steps=30, force=600)
    env.activate_suction()
    env.wait(20)
    env.move_arm(cup_pos[0], cup_pos[1], cup_pos[2] + 0.35, steps=30, force=600)

    # Step 4: Shake the arm back and forth rapidly to signify being hurried
    for _ in range(3):
        env.move_arm(cup_pos[0] + 0.10, cup_pos[1], cup_pos[2] + 0.35, steps=20, force=600)
        env.move_arm(cup_pos[0] - 0.10, cup_pos[1], cup_pos[2] + 0.35, steps=20, force=600)
    env.move_arm(cup_pos[0], cup_pos[1], cup_pos[2] + 0.35, steps=30, force=600)
'''
    }
]


def get_coding_prompt_block() -> str:
    """
    將 few-shot examples 格式化為 prompt 文字區塊
    Returns a formatted string to be injected into the code generator prompt.
    """
    blocks = []
    for ex in CODING_EXAMPLES:
        steps_json = json.dumps(ex["steps"], indent=2)
        block = (
            f"---\n"
            f"Emotion: {ex['emotion']}\n"
            f"Steps JSON:\n{steps_json}\n\n"
            f"Generated Code:\n```python\n{ex['code']}\n```"
        )
        blocks.append(block)
    return "\n\n".join(blocks)
