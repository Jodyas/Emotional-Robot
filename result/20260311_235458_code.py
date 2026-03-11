def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Perform a cheerful little jig, waving the arm slightly with a happy tilt of the suction cup, showing excitement to start.
    # Move to an initial happy position
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.5], steps=150, force=150, tilt=[0, 0.2, 0])
    # Perform a little jig/wave
    env.move_to([cup_pos[0] + 0.1, cup_pos[1] + 0.1, cup_pos[2] + 0.55], steps=100, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0, -0.2, 0])
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.5], steps=100, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.2, 0])

    # Step 3: Timing: Hold the happy pose for a moment, letting the cheerfulness sink in.
    env.wait(70)

    # Step 4: Move the arm with a light, slightly bouncy motion towards the cup, maintaining a happy demeanor.
    env.move_to("cup", steps=200, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.1, 0])

    # Step 5: Anticipation: Hover directly above the cup, dipping slightly as if bracing for a heavy lift. The suction cup tilts down, looking determined.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=250, force=200, noise_amp=0.01, noise_freq=0.8, tilt=[0.2, 0, 0])
    # Small dip for bracing
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.12], steps=80, force=250, noise_amp=0.015, noise_freq=1.0, tilt=[0.25, 0, 0])

    # Step 6: Timing: A dramatic pause, building tension before the strenuous effort of lifting the heavy cup.
    env.wait(100)

    # Step 7: Lower the arm slowly, activate suction, then lift the cup *very slowly* with significant trembling and jitter, showing extreme effort and strain. The suction cup strains upwards.
    # Lower slowly with strain
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=300, force=800, noise_amp=0.03, noise_freq=1.0, tilt=[0.3, 0, 0])
    env.activate_suction()
    env.wait(30)
    # Lift very slowly with extreme effort and strain
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=500, force=800, noise_amp=0.04, noise_freq=1.2, tilt=[-0.2, 0, 0])

    # Step 8: Timing: A longer pause after lifting, holding the heavy cup. First, show the strain, then a moment of satisfaction for successfully holding it.
    env.wait(150)

    # Step 9: Follow Through: Hold the heavy cup proudly, performing a gentle, satisfied bob or sway. The suction cup looks up with a proud, happy tilt, celebrating the successful heavy lift.
    # Proud bob/sway
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.45], steps=150, force=300, noise_amp=0.008, noise_freq=0.6, tilt=[-0.25, 0.1, 0])
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.42], steps=150, force=300, noise_amp=0.008, noise_freq=0.6, tilt=[-0.2, -0.1, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=150, force=300, noise_amp=0.008, noise_freq=0.6, tilt=[-0.25, 0, 0])
    env.wait(50)