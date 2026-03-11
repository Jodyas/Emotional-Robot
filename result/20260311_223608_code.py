def execute(env):
    # Step 1: Detect and confirm the cup's position on the table with a quick, almost impatient scan.
    cup_pos = env.get_object_position("cup")
    # Quick scan: move slightly above, then back, with an impatient tilt
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=50, force=300, tilt=[0, 0.2, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=40, force=350, tilt=[0, -0.2, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=30, force=400, tilt=[0, 0, 0])

    # Step 2: Anticipation: Jerk the arm slightly, a tense, frustrated twitch, showing impatience and building up to the angry grab.
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.30], steps=20, force=500, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0.3, 0])
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.30], steps=20, force=500, noise_amp=0.02, noise_freq=1.0, tilt=[0, -0.3, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=20, force=500, tilt=[0, 0, 0])

    # Step 3: Timing: A brief, tense pause to let the audience feel the robot's building anger.
    env.wait(30)

    # Step 4: Rush the arm directly above the cup with a fast, forceful, and slightly jerky motion, almost slamming into position.
    env.move_to("cup", steps=60, force=700, noise_amp=0.01, noise_freq=0.5, tilt=[0, 0.1, 0])

    # Step 5: Slam the arm down quickly, activate suction with a sharp sound, and yank the cup up abruptly and forcefully. The suction cup might tilt aggressively.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=25, force=800, tilt=[0, 0.2, 0]) # Slam down
    env.activate_suction()
    env.wait(10) # Short wait for suction to engage
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=40, force=750, tilt=[0, -0.3, 0]) # Yank up aggressively

    # Step 6: Timing: Freeze! A sudden, brief pause immediately after lifting, as if the robot just realized the cup is burning hot. The arm might tremble slightly.
    env.wait(20)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=10, force=100, noise_amp=0.008, noise_freq=1.5, tilt=[0, -0.3, 0]) # Slight tremble

    # Step 7: Exaggeration: Jerk the arm away violently and quickly to the side, as if recoiling from the heat, to a 'drop zone'.
    # Define a drop zone relative to the cup's initial position
    drop_zone = [cup_pos[0] + 0.3, cup_pos[1] + 0.4, cup_pos[2] + 0.35]
    env.move_to(drop_zone, steps=50, force=800, noise_amp=0.05, noise_freq=2.0, tilt=[-0.4, 0.5, 0]) # Violent jerk away

    # Step 8: Release the cup abruptly and forcefully, letting it drop with a clatter. The arm pulls back sharply.
    env.deactivate_suction()
    env.wait(5) # Immediate release
    env.move_to([drop_zone[0] + 0.1, drop_zone[1] + 0.1, drop_zone[2] + 0.2], steps=20, force=600, tilt=[0.5, -0.5, 0]) # Pull back sharply

    # Step 9: Timing: A moment of shock and frustration after dropping the cup. Hold still, perhaps with a slight, angry tremor.
    env.wait(40)
    env.move_to([drop_zone[0] + 0.1, drop_zone[1] + 0.1, drop_zone[2] + 0.2], steps=10, force=200, noise_amp=0.01, noise_freq=0.8, tilt=[0.5, -0.5, 0]) # Angry tremor

    # Step 10: Follow Through: Violently shake the arm side to side, retracting it quickly and aggressively, as if in pain from the burn and intense anger/frustration.
    # The suction cup might droop then snap back up.
    for _ in range(3):
        env.move_to([drop_zone[0] + 0.3, drop_zone[1] - 0.2, drop_zone[2] + 0.5], steps=25, force=700, noise_amp=0.08, noise_freq=3.0, tilt=[0.6, 0.6, 0])
        env.move_to([drop_zone[0] - 0.3, drop_zone[1] + 0.2, drop_zone[2] + 0.5], steps=25, force=700, noise_amp=0.08, noise_freq=3.0, tilt=[-0.6, -0.6, 0])
    # Final aggressive retraction
    env.move_to([drop_zone[0], drop_zone[1], drop_zone[2] + 0.8], steps=40, force=800, noise_amp=0.05, noise_freq=2.5, tilt=[0, 0, 0])