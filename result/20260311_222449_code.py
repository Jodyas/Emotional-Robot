def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup to the side, as if looking at the cup with curiosity,
    # then slowly move it slightly left and right to observe.
    # Initial hover with curious tilt
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=250, force=150, tilt=[0, 0.3, 0])
    env.wait(30)
    # Observe by moving slightly left and right
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.4], steps=150, force=100, tilt=[0, 0.3, 0], noise_amp=0.005, noise_freq=0.5)
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.4], steps=150, force=100, tilt=[0, 0.3, 0], noise_amp=0.005, noise_freq=0.5)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=100, force=100, tilt=[0, 0.3, 0]) # Return to center

    # Step 3: Slowly move the arm in a small arc around the cup, examining it from different angles, still showing curiosity.
    env.move_to([cup_pos[0] + 0.08, cup_pos[1] + 0.08, cup_pos[2] + 0.35], steps=200, force=120, tilt=[0, 0.2, 0])
    env.move_to([cup_pos[0] - 0.08, cup_pos[1] + 0.08, cup_pos[2] + 0.35], steps=200, force=120, tilt=[0, 0.2, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=150, force=120, tilt=[0, 0.1, 0]) # Return to above cup, slightly less tilt

    # Step 4: Timing: Hold still above the cup, letting the curiosity settle before the approach.
    env.wait(80)

    # Step 5: Approach the cup slowly and cautiously, hovering directly above it, preparing to pick up.
    env.move_to("cup", steps=300, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0.1, 0, 0]) # Slight forward tilt for focus

    # Step 6: Lower the arm to the cup, activate suction, and begin to lift.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=200, force=150, tilt=[0.1, 0, 0])
    env.activate_suction()
    env.wait(30)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=150, force=150, tilt=[0.1, 0, 0]) # Lift slightly

    # Step 7: Timing: Brief pause as the cup is lifted slightly, then a sudden, small downward jerk as it 'slips'.
    env.wait(40)
    # Simulate a small downward jerk
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.10], steps=30, force=300, noise_amp=0.02, noise_freq=1.0, tilt=[0.3, 0, 0]) # Sudden droop/jerk

    # Step 8: Briefly deactivate suction to simulate the cup slipping from the grip.
    env.deactivate_suction()
    env.wait(10) # Cup falls briefly

    # Step 9: Quickly re-adjust the arm slightly downwards and sideways to 'catch' the slipping cup,
    # showing a moment of surprise/perplexion.
    # Move quickly to catch, with a perplexed/surprised tilt
    env.move_to([cup_pos[0] + 0.03, cup_pos[1] - 0.03, cup_pos[2] + 0.08], steps=70, force=400, noise_amp=0.03, noise_freq=1.5, tilt=[0.4, -0.2, 0])
    env.wait(20) # Brief pause to "regain"

    # Step 10: Re-activate suction and carefully lift the cup again, this time successfully.
    env.activate_suction()
    env.wait(30)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=300, force=200, noise_amp=0.008, noise_freq=0.7, tilt=[0.2, 0, 0]) # Careful lift, perplexed tilt

    # Step 11: Timing: Pause after successfully picking up, showing relief but also continued caution.
    env.wait(70)

    # Step 12: Hold the cup with slight, continuous micro-adjustments and a gentle sway,
    # as if trying to maintain a secure grip on a slippery object. The suction cup might droop slightly in perplexity.
    # Gentle sway with perplexed/concerned droop
    for _ in range(3):
        env.move_to([cup_pos[0] + 0.01, cup_pos[1], cup_pos[2] + 0.35], steps=80, force=100, noise_amp=0.005, noise_freq=0.5, tilt=[0.25, 0, 0])
        env.move_to([cup_pos[0] - 0.01, cup_pos[1], cup_pos[2] + 0.35], steps=80, force=100, noise_amp=0.005, noise_freq=0.5, tilt=[0.25, 0, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=50, force=100, tilt=[0.2, 0, 0]) # Return to center

    # Step 13: Follow Through: Slowly bring the cup closer to the robot's 'body',
    # still handling it with exaggerated care and slight jitters, as if continuously trying to maintain grip on the slippery surface.
    safe_pos = [cup_pos[0] - 0.2, cup_pos[1], cup_pos[2] + 0.4] # Define a safe position closer to the robot
    env.move_to(safe_pos, steps=400, force=180, noise_amp=0.01, noise_freq=0.6, tilt=[0.2, 0, 0])
    env.wait(100)