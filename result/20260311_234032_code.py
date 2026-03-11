def execute(env):
    # Step 1: Detect and confirm the cup position on the table with a cheerful, curious tilt of the suction cup.
    cup_pos = env.get_object_position("cup")
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=150, force=150, tilt=[0, 0.3, 0]) # Hover above, curious tilt
    env.wait(50) # Brief pause to "confirm"

    # Step 2: Anticipation: Perform a light, bouncy sway of the arm, showing eagerness and happiness before approaching.
    # Sway slightly left, then right, then back to center, with a happy tilt.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.4], steps=100, force=150, noise_amp=0.005, noise_freq=0.8, tilt=[0, 0.2, 0])
    env.move_to([cup_pos[0] + 0.1, cup_pos[1], cup_pos[2] + 0.4], steps=100, force=150, noise_amp=0.005, noise_freq=0.8, tilt=[0, -0.2, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=100, force=150, noise_amp=0.005, noise_freq=0.8, tilt=[0, 0, 0]) # Back to center, slightly higher

    # Step 3: Move the arm with a light, slightly bouncy motion directly above the cup, maintaining a happy tilt.
    env.move_to("cup", steps=180, force=180, noise_amp=0.003, noise_freq=0.5, tilt=[0, 0.1, 0])

    # Step 4: Timing: Hold perfectly still above the cup for a brief moment, a happy pause before the action.
    env.wait(70)

    # Step 5: Lower the arm, activate suction, and attempt to lift the cup slightly, but with a small, quick jitter to indicate slipperiness.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=80, force=150, tilt=[0, 0.1, 0]) # Lower to grab
    env.activate_suction()
    env.wait(10)
    # Attempt to lift with jitter
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=50, force=100, noise_amp=0.02, noise_freq=1.5, tilt=[0, 0.1, 0])
    env.wait(20) # Hold briefly, feeling it slip

    # Step 6: The Slip: Immediately release the cup, letting it drop back down onto the table with a quick, surprised jerk of the arm.
    env.deactivate_suction()
    env.wait(5) # Release
    # Quick, surprised jerk upwards and slightly back
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.3], steps=40, force=300, tilt=[0.2, 0.2, 0]) # Surprised tilt

    # Step 7: Timing: A quick, surprised pause after the slip, the suction cup tilting slightly in 'oops' fashion.
    env.wait(60) # "Oops" pause

    # Step 8: Quickly re-position the arm directly above the cup, a determined but still happy tilt, ready for a second attempt.
    env.move_to("cup", steps=100, force=200, tilt=[0, 0.15, 0]) # Determined, slightly more focused tilt

    # Step 9: Lower the arm, activate suction, and lift the cup successfully this time, with a smooth, confident motion.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=80, force=150, tilt=[0, 0.15, 0])
    env.activate_suction()
    env.wait(10)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=200, force=180, tilt=[-0.1, 0, 0]) # Smooth, confident lift, proud tilt

    # Step 10: Timing: Hold the cup up for a brief moment, showing successful acquisition with a happy, proud tilt.
    env.wait(80)

    # Step 11: Follow Through: Perform a small, celebratory bounce or wave with the cup, showing triumph and continued happiness.
    # Bounce up and down slightly with the cup
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=80, force=150, noise_amp=0.01, noise_freq=0.5, tilt=[-0.2, 0, 0]) # Higher bounce, proud
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=80, force=150, noise_amp=0.01, noise_freq=0.5, tilt=[-0.1, 0, 0]) # Lower bounce
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.40], steps=80, force=150, noise_amp=0.01, noise_freq=0.5, tilt=[-0.2, 0, 0]) # Final celebratory position
    env.wait(100)