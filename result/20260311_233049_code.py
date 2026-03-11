def execute(env):
    # Step 1: Detect and confirm the cup position on the table with a cheerful, eager tilt of the suction cup.
    cup_pos = env.get_object_position("cup")
    # Move slightly above the cup to "confirm" its presence with an eager, slightly upward and side tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=150, force=150, tilt=[-0.1, 0.2, 0])
    env.wait(30) # A short pause to "look" at the cup.

    # Step 2: Anticipation: Perform a happy, bouncy wiggle with the arm, as if excited to pick up the cup.
    # Bounce up slightly with a happy tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=100, force=150, noise_amp=0.01, noise_freq=0.8, tilt=[-0.1, 0.2, 0])
    # Bounce down slightly, maintaining the happy tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=100, force=150, noise_amp=0.01, noise_freq=0.8, tilt=[-0.1, 0.2, 0])

    # Step 3: Timing: Hold the happy pose briefly, letting the anticipation build.
    env.wait(50)

    # Step 4: Move the arm with a bouncy, eager motion directly above the cup, maintaining a happy tilt.
    env.move_to("cup", steps=150, force=200, noise_amp=0.005, noise_freq=0.5, tilt=[-0.1, 0.2, 0])

    # Step 5: Lower the arm quickly but cheerfully, activate suction, and lift the cup with a slight happy bounce.
    # Lower quickly to grab the cup.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=80, force=300, tilt=[-0.1, 0.2, 0])
    env.activate_suction()
    env.wait(15)
    # Lift with a happy bounce, still tilted cheerfully.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=120, force=250, noise_amp=0.008, noise_freq=0.6, tilt=[-0.1, 0.2, 0])

    # Step 6: Timing: Freeze for a split second – the moment of 'oh, it's hot!' – a quick, surprised pause.
    env.wait(20) # Short, sharp pause for realization.
    # A quick, subtle tilt change to indicate surprise/pain.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=10, force=100, tilt=[0.1, -0.1, 0]) # Quick jerk of "head" in surprise.

    # Step 7: Exaggeration: Jerk the arm away from the body quickly, with a slight tremble, but still trying to maintain a cheerful (though slightly pained) tilt of the suction cup.
    # Define a "drop" location away from the original cup position.
    drop_x = cup_pos[0] + 0.2
    drop_y = cup_pos[1] + 0.3
    drop_z = cup_pos[2] + 0.30
    # Jerk away quickly with a slight tremble, maintaining a somewhat brave/pained tilt.
    env.move_to([drop_x, drop_y, drop_z], steps=70, force=400, noise_amp=0.02, noise_freq=1.0, tilt=[-0.05, 0.3, 0])

    # Step 8: Drop the hot cup quickly and decisively, as if letting go of something uncomfortable.
    env.deactivate_suction()
    env.wait(10) # Quick release.

    # Step 9: Timing: A brief pause after dropping, a 'phew' moment of relief.
    env.wait(40)

    # Step 10: Follow Through: Perform a happy, relieved shake of the arm, as if cheerfully shaking off the residual heat, ending with a bright, upward tilt of the suction cup.
    # Shake off the heat with multiple small, quick movements.
    for _ in range(3):
        env.move_to([drop_x + 0.05, drop_y, drop_z + 0.05], steps=40, force=200, noise_amp=0.01, noise_freq=0.8, tilt=[-0.2, 0.1, 0])
        env.move_to([drop_x - 0.05, drop_y, drop_z - 0.05], steps=40, force=200, noise_amp=0.01, noise_freq=0.8, tilt=[-0.2, -0.1, 0])
    # End with a bright, upward tilt, signifying relief and cheerfulness.
    env.move_to([drop_x, drop_y, drop_z + 0.1], steps=100, force=150, tilt=[-0.3, 0, 0])