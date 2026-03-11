def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Perform a small, joyful sway with a playful side-tilt of the suction cup, showing eagerness.
    # Move slightly above the cup, then sway gently side to side with a happy tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=150, force=150, tilt=[0, 0.3, 0])
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.35], steps=100, force=150, tilt=[0, -0.3, 0])
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.35], steps=100, force=150, tilt=[0, 0.3, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=100, force=150, tilt=[0, 0, 0]) # Return to neutral tilt for next step

    # Step 3: Timing: Hold still for a brief moment, letting the happy anticipation settle.
    env.wait(50)

    # Step 4: Move the arm smoothly and with a slight, gentle bounce towards the cup, maintaining a happy tilt.
    # First, a slight upward "hop" then down to the cup.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=100, force=180, tilt=[0, 0.2, 0]) # Slight hop up
    env.move_to("cup", steps=150, force=180, tilt=[0, 0.2, 0]) # Move to cup with happy tilt

    # Step 5: Timing: Pause briefly above the cup, like a happy 'I'm here!' moment, before grabbing.
    env.wait(30)

    # Step 6: Lower gently, activate suction, and lift the cup with a smooth, slightly upward 'bounce' to convey joy.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=100, force=150, tilt=[0, 0.1, 0]) # Lower gently
    env.activate_suction()
    env.wait(20)
    # Lift with a joyful bounce
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=150, force=200, tilt=[0, 0.1, 0]) # Lift higher than usual
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=80, force=150, tilt=[0, 0.1, 0]) # Settle slightly lower

    # Step 7: Timing: Pause after lifting, holding the cup, like a moment of happy satisfaction.
    env.wait(70)

    # Step 8: Follow Through: Gently sway the arm side-to-side, holding the cup, in a small celebratory gesture, maintaining the happy tilt.
    for _ in range(2): # Sway twice
        env.move_to([cup_pos[0] + 0.08, cup_pos[1], cup_pos[2] + 0.35], steps=120, force=150, tilt=[0, 0.2, 0])
        env.move_to([cup_pos[0] - 0.08, cup_pos[1], cup_pos[2] + 0.35], steps=120, force=150, tilt=[0, -0.2, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=100, force=150, tilt=[0, 0, 0]) # Return to neutral