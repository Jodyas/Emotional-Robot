def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Arm jerks violently and rapidly, suction cup tilts aggressively to the side, showing impatience and building anger.
    # Jerk away slightly first, then back, with aggressive side tilts.
    env.move_to([cup_pos[0] + 0.1, cup_pos[1], cup_pos[2] + 0.4], steps=40, force=500, noise_amp=0.08, noise_freq=2.0, tilt=[0, 0.4, 0])
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.4], steps=40, force=500, noise_amp=0.08, noise_freq=2.0, tilt=[0, -0.4, 0])
    env.wait(30) # A brief, angry pause

    # Step 3: Angry approach: Arm rushes forcefully and directly above the cup with high noise and jitter, almost slamming into position.
    env.move_to("cup", steps=60, force=700, noise_amp=0.05, noise_freq=1.8, tilt=[0, 0.3, 0])

    # Step 4: First attempt (the slip): Slam down, activate suction, lift *briefly* and *unsteadily* a few inches, then immediately lose grip as it slips.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=30, force=800, tilt=[0.2, 0, 0]) # Slam down, frustrated tilt
    env.activate_suction()
    env.wait(10) # Brief grab
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=40, force=400, noise_amp=0.03, noise_freq=1.0, tilt=[0.2, 0, 0]) # Lift unsteadily

    # Step 5: The cup slips from the suction cup's grasp and drops back onto the table with a thud.
    env.deactivate_suction()
    env.wait(15) # Let it fall and "thud"

    # Step 6: A sharp, short pause. The arm freezes, hovering angrily over the cup, processing the failure with a slight tremor.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=50, force=300, noise_amp=0.01, noise_freq=0.8, tilt=[0, 0.2, 0]) # Hover angrily
    env.wait(80) # Angry stare and tremor

    # Step 7: Reposition: A frustrated, jerky adjustment, moving slightly to hover directly over the cup again, preparing for a second attempt.
    env.move_to("cup", steps=100, force=500, noise_amp=0.03, noise_freq=1.2, tilt=[0, 0.2, 0]) # Jerky adjustment

    # Step 8: Second, determined grab: Slam down again with more force, activate suction, lift the cup quickly and firmly, but with a slight, controlled wobble after lifting to acknowledge its slipperiness.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=25, force=850, tilt=[-0.1, 0, 0]) # Slam down with determination
    env.activate_suction()
    env.wait(10) # Firm grab
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=70, force=600, noise_amp=0.01, noise_freq=0.5, tilt=[-0.1, 0, 0]) # Lift quickly and firmly, slight wobble

    # Step 9: Hold the cup up, a brief, tense pause to confirm it's finally secure in its grasp.
    env.wait(60) # Tense pause, confirming grip

    # Step 10: Follow Through: Jerk the arm back sharply, pulling the cup close to the robot's body, then hold it with a slight, continuous, angry tremor, showing lingering frustration.
    env.move_to([cup_pos[0] - 0.2, cup_pos[1], cup_pos[2] + 0.4], steps=50, force=700, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0.1, 0]) # Jerk back sharply
    env.wait(100) # Hold with lingering angry tremor