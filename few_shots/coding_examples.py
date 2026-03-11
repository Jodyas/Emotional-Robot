# Stage 2 Code Generation Few-shot Examples
# 每個 example 展示：Steps JSON + emotion → def execute(env): ...
# env 是 RobotPrimitives 的 instance，只允許呼叫 primitives API

import json

CODING_EXAMPLES = [
    {
        "emotion": "cautious",
        "steps": [
            {"action": "detect_object",   "args": {"name": "cup"}, "description": "Detect object."},
            {"action": "express_emotion", "args": {}, "description": "Pause and hover slightly, shaking from hesitation."},
            {"action": "move_to",         "args": {"target": "cup"}, "description": "Move above the cup smoothly."},
            {"action": "pick_up",         "args": {"object": "cup"}, "description": "Gently lift the cup."},
            {"action": "express_emotion", "args": {}, "description": "Bring it closer and hold still."}
        ],
        "code": '''\
def execute(env):
    # Step 1: Detect object.
    cup_pos = env.get_object_position("cup")

    # Step 2: Pause and hover slightly, tilting head down to "look" at cup (curious droop)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=100, force=100, noise_amp=0.01, noise_freq=0.8, tilt=[0.2, 0.15, 0])

    # Step 3: Move above the cup smoothly, head still tilted to examine
    env.move_to("cup", steps=150, force=100, tilt=[0.15, 0, 0])

    # Step 4: Gently lift the cup
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=100, force=100)
    env.activate_suction()
    env.wait(20)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=150, force=100)

    # Step 5: Bring it closer and hold still, head level (relieved)
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=100, force=100, tilt=[0, 0, 0])
    env.wait(50)
'''
    },
    {
        "emotion": "angry_hot",
        "steps": [
            {"action": "detect_object",   "args": {"name": "cup"}, "description": "Detect object."},
            {"action": "move_to",         "args": {"target": "cup"}, "description": "Rush above the cup aggressively."},
            {"action": "pick_up",         "args": {"object": "cup"}, "description": "Slam down, grab, and yank upwards."},
            {"action": "move_to",         "args": {"target": "drop"}, "description": "Realize it's hot, rush to drop off corner."},
            {"action": "deactivate_suction","args": {}, "description": "Drop it!"},
            {"action": "express_emotion", "args": {}, "description": "Violently shake hand in pain."}
        ],
        "code": '''\
def execute(env):
    # Step 1: Detect object.
    cup_pos = env.get_object_position("cup")

    # Step 2: Rush above the cup aggressively (fast steps, high force)
    env.move_to("cup", steps=80, force=600)

    # Step 3: Slam down, grab, and yank upwards
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=30, force=700)
    env.activate_suction()
    env.wait(6)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.40], steps=50, force=600)

    # Step 4: Realize it's hot, rush to drop off corner — head jerks away in disgust
    env.wait(15)  # Timing: freeze — moment of realization
    env.move_to([cup_pos[0] + 0.2, cup_pos[1] + 0.3, cup_pos[2] + 0.30], steps=60, force=600, noise_amp=0.03, noise_freq=1.5, tilt=[-0.3, 0.4, 0])

    # Step 5: Drop it!
    env.deactivate_suction()
    env.wait(6)  # Timing: moment of shock after dropping

    # Step 6: Violently shake hand in pain — alternate LEFT/RIGHT with head flailing!
    for _ in range(4):
        env.move_to([cup_pos[0] + 1.0, cup_pos[1], cup_pos[2] + 0.85], steps=25, force=500, noise_amp=0.06, noise_freq=3.0, tilt=[0, 0.5, 0])
        env.move_to([cup_pos[0] - 1.0, cup_pos[1], cup_pos[2] - 0.85], steps=25, force=500, noise_amp=0.06, noise_freq=3.0, tilt=[0, -0.5, 0])
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
