def execute(env):
    # Step 1: Detect and confirm the cup position on the table with an aggressive, quick scan.
    cup_pos = env.get_object_position("cup")
    # Quick scan: move slightly off-center, then to center, with fast steps and high force.
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] - 0.05, cup_pos[2] + 0.3], steps=50, force=500, tilt=[0, 0.3, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=50, force=500, tilt=[0, -0.3, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=50, force=500, tilt=[0, 0, 0])

    # Step 2: Anticipation: Jerk the arm aggressively and impatiently, showing building anger before the move.
    # Quick, sharp movements with high force and noise.
    env.move_to([cup_pos[0] + 0.1, cup_pos[1], cup_pos[2] + 0.4], steps=40, force=600, noise_amp=0.05, noise_freq=1.5, tilt=[0, 0.4, 0])
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.4], steps=40, force=600, noise_amp=0.05, noise_freq=1.5, tilt=[0, -0.4, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=30, force=600, noise_amp=0.03, noise_freq=1.0, tilt=[0, 0, 0])

    # Step 3: Timing: A tense, brief pause, letting the anger simmer before the action.
    env.wait(30)

    # Step 4: Slam the arm down forcefully and quickly towards the cup, showing aggression and impatience.
    env.move_to("cup", steps=60, force=700, tilt=[0.1, 0, 0]) # Slightly tilted down in aggression

    # Step 5: Grab the cup with an aggressive, fast motion, then immediately recoil slightly as if burned by the hot object.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=30, force=800) # Slam down
    env.activate_suction()
    env.wait(10)
    # Recoil upwards and slightly away with a jerk
    env.move_to([cup_pos[0] - 0.05, cup_pos[1] + 0.05, cup_pos[2] + 0.3], steps=40, force=600, noise_amp=0.04, noise_freq=1.8, tilt=[-0.2, 0.2, 0])

    # Step 6: Timing: Freeze! A brief, sharp moment of shock and realization that the cup is burning hot.
    env.wait(20) # Sharp pause

    # Step 7: Exaggeration: Violently jerk the arm away from the table, trying to get rid of the hot object in a panic.
    # Move far away with extreme speed, force, and noise, head jerking away.
    env.move_to([cup_pos[0] + 0.4, cup_pos[1] + 0.5, cup_pos[2] + 0.6], steps=50, force=800, noise_amp=0.08, noise_freq=2.5, tilt=[-0.5, 0.6, 0])

    # Step 8: Release the cup abruptly and forcefully, as if throwing it away due to the heat.
    env.deactivate_suction()
    env.wait(5) # Immediate release
    # Follow through with a "throwing" motion
    env.move_to([cup_pos[0] + 0.5, cup_pos[1] + 0.6, cup_pos[2] + 0.7], steps=30, force=700, noise_amp=0.05, noise_freq=2.0, tilt=[-0.6, 0.7, 0])

    # Step 9: Timing: A moment of relief/shock after dropping the hot object. Hold still briefly.
    env.wait(40)

    # Step 10: Follow Through: Shake the arm violently and rapidly, as if trying to cool off a burned hand, expressing both anger at the situation and pain from the heat.
    # Violent shaking loop
    for _ in range(5):
        env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.7, cup_pos[2] + 0.8], steps=20, force=600, noise_amp=0.1, noise_freq=3.0, tilt=[0, 0.8, 0])
        env.move_to([cup_pos[0] + 0.2, cup_pos[1] + 0.6, cup_pos[2] + 0.7], steps=20, force=600, noise_amp=0.1, noise_freq=3.0, tilt=[0, -0.8, 0])
    # End with a final angry, slightly lowered position
    env.move_to([cup_pos[0] + 0.25, cup_pos[1] + 0.65, cup_pos[2] + 0.75], steps=50, force=500, tilt=[0.3, 0, 0])