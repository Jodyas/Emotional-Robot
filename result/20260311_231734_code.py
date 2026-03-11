def execute(env):
    # Step 1: Detect and confirm the cup position on the table with a quick, almost impatient scan.
    cup_pos = env.get_object_position("cup")
    # A quick, impatient scan can be implied by the immediate aggressive movement in the next step.

    # Step 2: Anticipation: Jerk the arm sharply downwards and then quickly back up, showing a burst of frustration and impatience before moving.
    # Start from a slightly raised position, then jerk down aggressively.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=50, force=500, tilt=[0, 0, 0]) # Initial neutral hover
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.1], steps=30, force=800, tilt=[0, 0.4, 0]) # Sharp jerk downwards, aggressive tilt
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=40, force=800, tilt=[0, -0.3, 0]) # Quick snap back up, defiant tilt

    # Step 3: Timing: Hold perfectly still for a brief, tense moment, letting the anger build before the next action.
    env.wait(70) # Tense pause

    # Step 4: Rush the arm directly above the cup with a forceful, almost slamming motion, tilting the suction cup aggressively downwards.
    env.move_to("cup", steps=60, force=800, tilt=[0, 0.5, 0]) # Fast, forceful move with aggressive pitch down

    # Step 5: Timing: Hold perfectly still, hovering aggressively above the cup, like a predator about to strike.
    env.wait(50) # Aggressive hover

    # Step 6: Slam the arm down quickly, activate suction with a sharp click, and then thrust the cup upwards abruptly and forcefully.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=20, force=900, tilt=[0, 0.5, 0]) # Slam down
    env.activate_suction()
    env.wait(10) # Brief wait for suction to engage
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.5], steps=40, force=800, tilt=[0, -0.3, 0]) # Thrust upwards abruptly and forcefully

    # Step 7: Timing: Hold the cup high and still for a brief moment, showing defiance in its grasp.
    env.wait(80) # Defiant hold

    # Step 8: Follow Through: Thrust the arm forward slightly with the cup, then pull it back sharply and hold it tightly, perhaps with a slight, controlled tremor of residual anger, before settling into a defiant pose.
    env.move_to([cup_pos[0] + 0.1, cup_pos[1], cup_pos[2] + 0.45], steps=30, force=700, tilt=[0, -0.2, 0]) # Thrust forward
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.55], steps=30, force=700, tilt=[0, -0.4, 0]) # Pull back sharply
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.5], steps=100, force=600, noise_amp=0.01, noise_freq=0.8, tilt=[0, -0.3, 0]) # Settle with slight tremor of residual anger
    env.wait(100) # Hold defiant pose