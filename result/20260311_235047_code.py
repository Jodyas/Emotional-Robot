def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm trembles noticeably, making a slight jerky movement away from the cup, showing reluctance and fear. The suction cup 'head' tilts slightly down.
    # Move slightly away from the cup's hover position, with noticeable tremble and a fearful tilt.
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.35], steps=100, force=300, noise_amp=0.02, noise_freq=0.8, tilt=[0.2, 0, 0])

    # Step 3: Timing: Hold still for a dramatic pause, letting the fear and hesitation build.
    env.wait(150)

    # Step 4: Move the arm slowly and hesitantly towards the cup, with continuous, high-frequency trembling to show fear. The suction cup 'head' remains slightly drooped.
    # Move to hover above the cup, very slowly, with continuous trembling.
    env.move_to("cup", steps=400, force=400, noise_amp=0.025, noise_freq=1.0, tilt=[0.2, 0, 0])

    # Step 5: Timing: Pause directly above the cup, still trembling, as if gathering courage or bracing for the effort.
    env.wait(100)

    # Step 6: Anticipation for Heavy Lift: Perform a very slow, slight dip downwards just before activating suction, as if bracing for the immense weight. The suction cup 'head' drops further down.
    # Dip slightly below the default "cup" hover, very slowly, with increased tilt and tremble.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.08], steps=300, force=500, noise_amp=0.03, noise_freq=1.2, tilt=[0.3, 0, 0])

    # Step 7: Lower the arm very slowly, activate suction. Lift the cup with extreme slowness and significant, strained jitter/trembling, showing immense effort. The suction cup 'head' remains heavily drooped, conveying strain and fear.
    # Move to cup for suction, very slowly.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.02], steps=200, force=600, noise_amp=0.04, noise_freq=1.5, tilt=[0.4, 0, 0])
    env.activate_suction()
    env.wait(30) # Brief wait to ensure suction, still trembling.
    # Lift the cup with extreme slowness and strained jitter.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=600, force=800, noise_amp=0.05, noise_freq=1.8, tilt=[0.4, 0, 0])

    # Step 8: Timing: Hold the cup aloft for a moment, still trembling from the effort and fear. A moment of strained triumph or relief.
    env.wait(150)

    # Step 9: Follow Through: Slowly bring the cup closer, still trembling and moving very deliberately, as if the weight is an ongoing struggle and the fear persists. The suction cup 'head' remains slightly drooped, showing continued strain and apprehension.
    # Bring the cup closer to the robot's base, very slowly and deliberately, maintaining tremble and drooped head.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.40], steps=500, force=700, noise_amp=0.035, noise_freq=1.5, tilt=[0.35, 0, 0])
    env.wait(50)