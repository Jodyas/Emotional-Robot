def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup slightly to the side, slowly approaching the general area of the cup,
    # hovering with a curious 'hmm?' gesture.
    # Move to a point slightly offset from the cup, higher up, with a curious side tilt.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] + 0.1, cup_pos[2] + 0.4], steps=250, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold the curious pose, observing the cup from a distance.
    env.wait(100)

    # Step 4: Slowly and smoothly move the arm to hover directly above the cup, maintaining a slight curious tilt
    # of the suction cup, as if examining it closely.
    env.move_to("cup", steps=300, force=150, tilt=[0, 0.2, 0])

    # Step 5: Timing: Hold perfectly still above the cup, focused and contemplating before the grab.
    env.wait(70)

    # Step 6: Lower the arm, activate suction, lift the cup, but immediately perform a small, quick, jerky movement
    # to the side as if it almost slipped from the suction cup, then quickly re-center and lift higher to secure it.
    # Lower to grab
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=100, force=200, tilt=[0, 0.1, 0])
    env.activate_suction()
    env.wait(20)
    # Lift slightly
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=80, force=200)
    # Jerk to the side (almost slipped!)
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.15], steps=30, force=400, noise_amp=0.02, noise_freq=1.5, tilt=[0, -0.2, 0])
    # Quickly re-center
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=30, force=400, tilt=[0, 0.2, 0])
    # Lift higher to secure it
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=150, force=250, noise_amp=0.008, noise_freq=0.8, tilt=[0, 0.1, 0])

    # Step 7: Timing: Pause after the 'slip' and re-stabilization, holding the cup with a visible, slight tremble
    # to show it's still slippery.
    env.wait(80) # Hold with the slight tremble from the previous move_to

    # Step 8: Follow Through: Bring the cup closer to the robot's 'body', still trembling slightly to show its
    # slippery nature, and tilt the suction cup as if examining the 'slippery' object with continued curiosity
    # and a hint of relief.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=200, force=200, noise_amp=0.01, noise_freq=0.5, tilt=[0, 0.25, 0])
    env.wait(50) # A final moment of curious, slightly relieved observation