def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Lean in slightly, tilting the suction cup to the side as if observing the cup with initial curiosity.
    # Move slightly forward and above the cup, with a curious side-tilt (pitch) and slight roll.
    env.move_to([cup_pos[0], cup_pos[1] + 0.1, cup_pos[2] + 0.3], steps=200, force=100, tilt=[0.1, 0.3, 0])

    # Step 3: Timing: Hold the pose, allowing the audience to 'read' the initial curious observation.
    env.wait(steps=80)

    # Step 4: Curiosity: Slowly and tentatively move the arm towards the cup, stopping a short distance away to inspect it.
    # Move closer to the cup's level, maintaining a curious tilt and adding a slight tremble.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=300, force=100, noise_amp=0.005, noise_freq=0.5, tilt=[0.1, 0.2, 0])

    # Step 5: Act Out Spiky/Curiosity: Circle the suction cup slowly around the cup, tilting it from side to side, as if examining the spikes from different angles.
    # Define a hover height for circling.
    hover_height = cup_pos[2] + 0.2
    # Circle around the cup with varying tilts
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], hover_height], steps=100, force=100, tilt=[0, 0.3, 0]) # Look from right
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], hover_height], steps=100, force=100, tilt=[0, -0.3, 0]) # Look from left
    env.move_to([cup_pos[0], cup_pos[1] + 0.05, hover_height], steps=100, force=100, tilt=[0.3, 0, 0]) # Look from front
    env.move_to([cup_pos[0], cup_pos[1] - 0.05, hover_height], steps=100, force=100, tilt=[-0.3, 0, 0]) # Look from back
    env.move_to([cup_pos[0], cup_pos[1], hover_height], steps=100, force=100, tilt=[0, 0, 0]) # Return to center hover

    # Step 6: Timing: Pause to 'process' the visual information of the spikes.
    env.wait(steps=100)

    # Step 7: Act Out Spiky: Move *very* slightly closer to the cup, then perform a quick, small jerk back, as if tentatively touching a spike and recoiling.
    # Move slightly closer, just above the rim.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.08], steps=100, force=100)
    # Quick jerk back.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.2], steps=50, force=200, noise_amp=0.01, noise_freq=1.0)

    # Step 8: Timing: Hold still, a moment of hesitation and consideration after the 'prick'.
    env.wait(steps=70)

    # Step 9: Careful Grab: Slowly and precisely position the arm directly above the cup, avoiding any further contact with the sides.
    env.move_to("cup", steps=300, force=100, noise_amp=0.0)

    # Step 10: Gently lower the arm, activate suction, and lift the cup slowly and smoothly.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=250, force=100)
    env.activate_suction()
    env.wait(steps=30)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=250, force=100)

    # Step 11: Timing: Pause after lifting, holding the cup gingerly.
    env.wait(steps=60)

    # Step 12: Follow Through/Act Out Spiky: Perform a slight, quick tremor or a small, uncomfortable jerk of the arm, as if the spikes are still a bit bothersome even when held. Tilt the cup slightly away from the arm's body.
    # Move slightly to the side and up, with a gentle tremor and a tilt that suggests keeping distance.
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.35], steps=150, force=150, noise_amp=0.015, noise_freq=1.0, tilt=[0.2, 0, 0])