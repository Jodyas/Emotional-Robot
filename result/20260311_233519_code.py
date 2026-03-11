def execute(env):
    # Step 1: Detect and confirm the cup position on the table, but with the suction cup slightly tilted away, as if apprehensive.
    cup_pos = env.get_object_position("cup")
    # Hover slightly above the cup, with a tilt suggesting apprehension (looking away/downcast)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=150, force=150, tilt=[0.1, 0.2, 0])

    # Step 2: Anticipation: The arm trembles noticeably, shaking back and forth slightly, showing extreme hesitation and fear before approaching.
    # Simulate trembling by moving to slightly different points with high noise
    env.move_to([cup_pos[0] + 0.02, cup_pos[1], cup_pos[2] + 0.32], steps=70, force=100, noise_amp=0.02, noise_freq=1.5, tilt=[0.1, 0.2, 0])
    env.move_to([cup_pos[0] - 0.02, cup_pos[1], cup_pos[2] + 0.32], steps=70, force=100, noise_amp=0.02, noise_freq=1.5, tilt=[0.1, 0.2, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.32], steps=70, force=100, noise_amp=0.02, noise_freq=1.5, tilt=[0.1, 0.2, 0])

    # Step 3: Timing: Hold still for a dramatic pause, letting the fear build before the next move.
    env.wait(100)

    # Step 4: Move the arm slowly and hesitantly towards the cup, with continuous, high-frequency trembling. The suction cup remains slightly tilted away.
    env.move_to("cup", steps=400, force=120, noise_amp=0.01, noise_freq=1.0, tilt=[0.1, 0.2, 0])

    # Step 5: Timing: Pause directly above the cup, still trembling, as if gathering courage for the difficult task.
    # Move to current position with noise to simulate trembling while pausing
    current_pos = env.get_object_position("cup") # Get current hover position
    env.move_to([current_pos[0], current_pos[1], current_pos[2] + 0.15], steps=100, force=100, noise_amp=0.01, noise_freq=1.0, tilt=[0.1, 0.2, 0])
    env.wait(80)

    # Step 6: Lower the arm, activate suction, and lift the cup. Immediately after lifting, simulate a 'slip'.
    # Lower slowly and carefully
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=250, force=100, noise_amp=0.005, noise_freq=0.8, tilt=[0.1, 0.2, 0])
    env.activate_suction()
    env.wait(20)
    # Lift the cup
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.2], steps=150, force=150, tilt=[0.1, 0.2, 0])
    # Simulate a 'slip': jerk slightly to one side with sharp tremor
    env.move_to([cup_pos[0] + 0.03, cup_pos[1], cup_pos[2] + 0.18], steps=30, force=300, noise_amp=0.05, noise_freq=3.0, tilt=[0.1, 0.3, 0])
    # Quickly re-center as if barely caught
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=40, force=250, noise_amp=0.01, noise_freq=1.5, tilt=[0.1, 0.2, 0])

    # Step 7: Timing: Freeze for a moment after the near-slip, showing a beat of panic and relief that it wasn't dropped.
    env.wait(70)

    # Step 8: Quickly pull the cup closer to the robot's body, holding it very carefully and still trembling slightly, as if protecting it from further slips.
    # Define a safe position closer to the robot
    safe_pos = [cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35]
    env.move_to(safe_pos, steps=200, force=180, noise_amp=0.008, noise_freq=0.7, tilt=[0.1, 0.1, 0])

    # Step 9: Follow Through: Hold the cup perfectly still but with a continuous, low-frequency tremor, showing lingering fear and extreme caution. The suction cup droops slightly in relief/exhaustion.
    # Hold current position with lingering tremor and a drooping tilt
    env.move_to(safe_pos, steps=150, force=100, noise_amp=0.005, noise_freq=0.5, tilt=[0.2, 0, 0])
    env.wait(100)