def execute(env):
    # Step 1: Detect and confirm the cup position on the table with a cheerful, slightly tilted suction cup.
    cup_pos = env.get_object_position("cup")
    # Initial hover with a happy, slightly tilted orientation
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=150, force=150, tilt=[0, 0.1, 0.1])

    # Step 2: Anticipation: Perform a small, happy wiggle or bounce, as if eager to start.
    # Bounce up
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.40], steps=80, force=150, tilt=[0, 0.1, 0.1])
    # Bounce down slightly
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=80, force=150, tilt=[0, 0.1, 0.1])
    # Bounce back up
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.40], steps=80, force=150, tilt=[0, 0.1, 0.1])

    # Step 3: Timing: A brief, light pause to let the happy anticipation register.
    env.wait(50)

    # Step 4: Move the arm quickly and with a light, bouncy motion directly above the cup, suction cup tilted happily.
    env.move_to("cup", steps=100, force=200, tilt=[0, 0.1, 0.1])
    # Small bounce after reaching target
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.28], steps=50, force=150, tilt=[0, 0.1, 0.1])
    env.move_to("cup", steps=50, force=150, tilt=[0, 0.1, 0.1])

    # Step 5: Lower the arm, activate suction, and begin to lift the cup with a quick, confident motion.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=80, force=200, tilt=[0, 0.1, 0.1])
    env.activate_suction()
    env.wait(20)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=100, force=250, tilt=[0, 0.1, 0.1])

    # Step 6: Act Out Property: Immediately after lifting, perform a quick, small, jerky movement to the side,
    # simulating the cup slipping slightly in the suction cup. The suction cup might momentarily tilt in surprise.
    # Jerk to the side with a surprised tilt
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] - 0.03, cup_pos[2] + 0.28], steps=40, force=300, noise_amp=0.02, noise_freq=1.0, tilt=[0.2, -0.2, 0.3])

    # Step 7: Quickly re-stabilize the cup, bringing it back to a secure, centered position with a slight,
    # reassuring 'pat' motion. The suction cup re-tilts happily.
    # Move back to a stable position with happy tilt
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=60, force=250, tilt=[0, 0.1, 0.1])
    # Reassuring 'pat' motion (down then up)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=30, force=200, tilt=[0, 0.1, 0.1])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=30, force=200, tilt=[0, 0.1, 0.1])

    # Step 8: Timing: A brief pause, as if the robot is saying 'Phew! Got it!' with a happy little bob.
    env.wait(70)
    # Small happy bob
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.32], steps=30, force=150, tilt=[0, 0.1, 0.1])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=30, force=150, tilt=[0, 0.1, 0.1])

    # Step 9: Follow Through: Perform a happy little jig or celebratory wave with the cup,
    # showing triumph and continued happiness despite the minor slip.
    # Happy wave left
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.35], steps=70, force=200, noise_amp=0.01, noise_freq=0.8, tilt=[0, 0.1, 0.1])
    # Happy wave right
    env.move_to([cup_pos[0] + 0.1, cup_pos[1], cup_pos[2] + 0.35], steps=70, force=200, noise_amp=0.01, noise_freq=0.8, tilt=[0, 0.1, 0.1])
    # Happy wave center and slightly up
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=70, force=200, noise_amp=0.01, noise_freq=0.8, tilt=[0, 0.1, 0.1])
    # Final happy hover
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=100, force=150, tilt=[0, 0.1, 0.1])