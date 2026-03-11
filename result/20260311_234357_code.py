def execute(env):
    # Step 1: Detect and confirm the cup's position on the table with a sharp, focused movement.
    cup_pos = env.get_object_position("cup")
    # Move quickly to just above the cup, with a focused, slightly aggressive tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=80, force=500, tilt=[0, -0.2, 0])
    env.wait(30) # Brief pause to "confirm"

    # Step 2: Anticipation: The arm tenses, performing a quick, sharp, frustrated shake, as if impatient. Suction cup tilts aggressively forward.
    # Quick, sharp shake (small, rapid movements)
    env.move_to([cup_pos[0], cup_pos[1] + 0.02, cup_pos[2] + 0.25], steps=30, force=600, tilt=[0, -0.4, 0])
    env.move_to([cup_pos[0], cup_pos[1] - 0.02, cup_pos[2] + 0.25], steps=30, force=600, tilt=[0, -0.4, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=30, force=600, tilt=[0, -0.4, 0])

    # Step 3: Timing: A brief, tense pause to build up the angry energy before the approach.
    env.wait(80) # Tense pause

    # Step 4: Move the arm quickly and forcefully directly above the cup, almost slamming down, showing anger.
    # Fast steps, high force, low jitter, maintaining aggressive forward tilt.
    env.move_to("cup", steps=70, force=700, noise_amp=0.01, noise_freq=0.5, tilt=[0, -0.4, 0])

    # Step 5: Act Out Heaviness: Forcefully press down, then 'drop the arm a bit' with a noticeable dip as if bracing for weight. Activate suction, then lift the cup slowly and with significant trembling, showing extreme strain.
    # Forcefully press down
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.02], steps=40, force=800, tilt=[0, -0.3, 0])
    # 'Drop the arm a bit' with a noticeable dip
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] - 0.02], steps=20, force=800, tilt=[0.1, -0.2, 0]) # Slight tilt change for the dip
    env.activate_suction()
    env.wait(10)
    # Lift the cup slowly and with significant trembling, showing extreme strain.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=400, force=800, noise_amp=0.03, noise_freq=0.8, tilt=[0.2, -0.1, 0])

    # Step 6: Timing: Hold the cup mid-air, slightly sagging, emphasizing its perceived heavy weight and the effort required to hold it.
    # Hold slightly lower than normal, with persistent tremble.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=100, force=700, noise_amp=0.025, noise_freq=0.7, tilt=[0.2, -0.1, 0])
    env.wait(120)

    # Step 7: Move the heavy cup slowly and deliberately to a new position on the side, maintaining the strained posture and trembling, still showing the immense effort.
    side_table_pos = [cup_pos[0] + 0.3, cup_pos[1] + 0.3, cup_pos[2] + 0.25]
    env.move_to(side_table_pos, steps=500, force=750, noise_amp=0.02, noise_freq=0.6, tilt=[0.2, -0.1, 0])

    # Step 8: Follow Through: Hold the cup in the new position, the arm slightly lower than expected, with a persistent tremble and the suction cup drooping slightly, conveying lingering strain and frustration from the heavy lift.
    # Hold slightly lower, with persistent tremble and drooping tilt.
    side_table_hold_pos_sag = [side_table_pos[0], side_table_pos[1], side_table_pos[2] - 0.05]
    env.move_to(side_table_hold_pos_sag, steps=100, force=700, noise_amp=0.025, noise_freq=0.7, tilt=[0.3, 0, 0]) # More pronounced droop
    env.wait(150)