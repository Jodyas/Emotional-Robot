def execute(env):
    # Step 1: Detect and confirm the cup position on the table with an aggressive, focused tilt of the suction cup.
    cup_pos = env.get_object_position("cup")
    # Move slightly above the cup, tilting aggressively to "stare" at it.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=100, force=400, tilt=[-0.2, 0.3, 0])

    # Step 2: Hold perfectly still — a tense, dramatic pause before the first attempt.
    env.wait(100)

    # Step 3: Anticipation: A sharp, aggressive jerk of the arm, showing impatience and anger before moving.
    # Jerk slightly away, then snap back to a ready position.
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.35], steps=30, force=600, tilt=[0, 0.5, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=30, force=600, tilt=[-0.2, 0.3, 0])

    # Step 4: Rush the arm directly above the cup quickly and forcefully, with a slight aggressive jitter.
    env.move_to("cup", steps=70, force=700, noise_amp=0.02, noise_freq=1.5, tilt=[-0.1, 0.2, 0])

    # Step 5: Slam the arm down, activate suction, attempt to lift the cup. Struggle visibly, lifting it only slightly with heavy jitter.
    # Slam down
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=40, force=800, noise_amp=0.01, noise_freq=0.5)
    env.activate_suction()
    env.wait(10)
    # Struggle to lift slightly
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=150, force=800, noise_amp=0.05, noise_freq=0.8, tilt=[0.1, 0, 0])

    # Step 6: Exaggeration: The arm suddenly drops downwards with a heavy thud, unable to sustain the lift due to the cup's weight. Deactivate suction implicitly as it drops.
    env.deactivate_suction() # Release the cup
    env.wait(5) # Small pause before the drop
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] - 0.05], steps=20, force=900, noise_amp=0.0, noise_freq=0.0, tilt=[0.3, 0, 0]) # Slam down below table level

    # Step 7: Timing: Freeze! A moment of shock and intense frustration after the arm drops.
    env.wait(120)

    # Step 8: Exaggeration: Violently shake the arm back and forth, jerking it erratically in a fit of anger and frustration. The suction cup droops sadly then snaps up aggressively.
    # Droop sadly first
    env.move_to([cup_pos[0] + 0.1, cup_pos[1], cup_pos[2] + 0.4], steps=50, force=300, tilt=[0.4, 0, 0])
    # Violent shaking
    for _ in range(3):
        env.move_to([cup_pos[0] + 0.2, cup_pos[1] + 0.1, cup_pos[2] + 0.6], steps=30, force=700, noise_amp=0.08, noise_freq=2.5, tilt=[0, 0.5, 0])
        env.move_to([cup_pos[0] - 0.2, cup_pos[1] - 0.1, cup_pos[2] + 0.5], steps=30, force=700, noise_amp=0.08, noise_freq=2.5, tilt=[0, -0.5, 0])
    # Snap up aggressively
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=40, force=600, tilt=[-0.3, 0.4, 0])

    # Step 9: Timing: Pause to let the frustration settle, then a determined, angry resolve.
    env.wait(80)

    # Step 10: Move the arm back above the cup with a determined, slightly aggressive, and slower motion, showing renewed effort.
    env.move_to("cup", steps=150, force=500, noise_amp=0.01, noise_freq=0.8, tilt=[-0.1, 0.2, 0])

    # Step 11: Lower the arm slowly and deliberately, activate suction, then lift the cup with visible strain and heavy, sustained jitter, showing it's very heavy.
    # Lower slowly and deliberately
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=200, force=600, tilt=[0, 0.1, 0])
    env.activate_suction()
    env.wait(15)
    # Lift with visible strain and heavy, sustained jitter
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=400, force=800, noise_amp=0.04, noise_freq=0.6, tilt=[0.1, 0, 0])

    # Step 12: Timing: Hold the heavy cup aloft, showing the effort and the successful but strained lift.
    env.wait(100)

    # Step 13: Follow Through: Slowly pull the cup closer to the robot's body, holding it with sustained, heavy jitter and a determined, slightly aggressive posture, still showing the weight and lingering anger.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.4], steps=250, force=700, noise_amp=0.03, noise_freq=0.7, tilt=[-0.1, 0.1, 0])
    env.wait(50)