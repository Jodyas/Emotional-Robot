def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm recoils slightly, then approaches slowly with high noise (trembling).
    # The suction cup tilts away, 'looking' at the cup with apprehension.
    # Recoil slightly upwards and backwards from the cup's general area.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.4], steps=100, force=200, noise_amp=0.02, noise_freq=1.0, tilt=[0.1, 0.3, 0])
    # Hover and tremble with apprehension, looking away.
    env.move_to([cup_pos[0] - 0.05, cup_pos[1] - 0.05, cup_pos[2] + 0.35], steps=200, force=150, noise_amp=0.03, noise_freq=1.5, tilt=[0.15, 0.4, 0])

    # Step 3: Timing: A dramatic pause to emphasize the fear and hesitation before committing to the approach.
    env.wait(150)

    # Step 4: Move the arm very slowly and cautiously towards the cup, with significant trembling,
    # keeping a slight distance. The suction cup is angled as if trying to avoid direct contact.
    # Move to a point just above the cup, but not directly centered, maintaining distance and tilt.
    env.move_to([cup_pos[0] + 0.02, cup_pos[1] + 0.02, cup_pos[2] + 0.15], steps=400, force=100, noise_amp=0.04, noise_freq=1.8, tilt=[0.2, 0.5, 0])

    # Step 5: Timing: Pause above the cup, hovering, as if gathering courage or trying to find a safe spot.
    env.wait(100)

    # Step 6: Exaggeration: A quick, sharp flinch or recoil, as if a spike just pricked it.
    # The arm jerks back slightly and quickly.
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] + 0.05, cup_pos[2] + 0.25], steps=50, force=300, noise_amp=0.05, noise_freq=2.5, tilt=[0.3, 0.6, 0])
    env.wait(30) # Short pause after flinch

    # Step 7: Lower the arm very gingerly, activate suction, then immediately lift it quickly but carefully.
    # Gingerly lower.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=350, force=100, noise_amp=0.03, noise_freq=1.5, tilt=[0.1, 0.4, 0])
    env.activate_suction()
    env.wait(20) # Brief hold
    # Lift quickly but carefully.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=150, force=200, noise_amp=0.03, noise_freq=1.5, tilt=[0.1, 0.4, 0])

    # Step 8: Timing: A brief pause after lifting, holding the cup at arm's length, still trembling slightly.
    env.wait(80)

    # Step 9: Follow Through: Hold the cup away from its 'body', still trembling with high noise,
    # maintaining a fearful posture.
    # Move to a "safe" distance, further away, maintaining trembling and fearful tilt.
    env.move_to([cup_pos[0] - 0.2, cup_pos[1] + 0.1, cup_pos[2] + 0.4], steps=200, force=150, noise_amp=0.04, noise_freq=1.8, tilt=[0.2, 0.5, 0])
    # Hold and tremble for a longer duration.
    env.wait(200)