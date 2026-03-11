def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup slightly to the side, performing a small, investigative wiggle to show initial curiosity.
    # Move slightly above the cup with a curious side tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=200, force=150, tilt=[0, 0.3, 0])
    # Small wiggle
    env.move_to([cup_pos[0] + 0.02, cup_pos[1], cup_pos[2] + 0.3], steps=50, force=100, tilt=[0, 0.35, 0], noise_amp=0.005, noise_freq=0.5)
    env.move_to([cup_pos[0] - 0.02, cup_pos[1], cup_pos[2] + 0.3], steps=50, force=100, tilt=[0, 0.25, 0], noise_amp=0.005, noise_freq=0.5)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=50, force=100, tilt=[0, 0.3, 0])
    env.wait(30) # Pause after the wiggle

    # Step 3: Slowly and deliberately approach the cup from an angle, 'peeking' at it rather than moving directly above. Maintain a curious tilt.
    # Approach from an offset position to "peek"
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] + 0.1, cup_pos[2] + 0.25], steps=300, force=150, tilt=[0, 0.3, 0])

    # Step 4: Timing: Pause, holding the curious tilt, as if observing the cup intently.
    env.wait(100)

    # Step 5: Tentatively move the suction cup very close to the cup's rim, almost touching, then quickly recoil slightly, as if feeling the heat.
    # Move very close to the rim
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.01], steps=250, force=100, tilt=[0, 0.3, 0], noise_amp=0.005, noise_freq=0.5)
    env.wait(20) # Brief touch
    # Quickly recoil
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.2], steps=80, force=200, tilt=[0, 0.3, 0])

    # Step 6: A quick, subtle shake of the arm (reacting to heat), then a more pronounced curious tilt, as if processing the 'hot' sensation and finding it interesting.
    # Subtle shake for heat reaction
    env.move_to([cup_pos[0] + 0.01, cup_pos[1], cup_pos[2] + 0.25], steps=30, force=150, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0.3, 0])
    env.move_to([cup_pos[0] - 0.01, cup_pos[1], cup_pos[2] + 0.25], steps=30, force=150, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0.3, 0])
    # More pronounced curious tilt
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=100, force=150, tilt=[0, 0.5, 0])

    # Step 7: Timing: Pause, considering the next move after the 'hot' discovery.
    env.wait(120)

    # Step 8: Carefully, with a slight side-tilt of the suction cup, move directly above the cup, maintaining curiosity but with a hint of caution.
    env.move_to("cup", steps=250, force=150, tilt=[0, 0.3, 0], noise_amp=0.005, noise_freq=0.5)

    # Step 9: Gently lower, activate suction, and lift the cup with a slightly quicker upward motion, as if still wary of prolonged contact with the 'hot' surface.
    # Gently lower
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=200, force=100, tilt=[0, 0.3, 0])
    env.activate_suction()
    env.wait(20)
    # Lift with slightly quicker motion
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=150, force=200, tilt=[0, 0.3, 0])

    # Step 10: Timing: Hold the cup, observing it with a curious tilt after lifting.
    env.wait(80)

    # Step 11: Follow Through: Bring the cup closer, tilt it from side to side, examining it with sustained curiosity, perhaps a very subtle, controlled tremor to acknowledge the 'hot' property while still being intrigued.
    # Bring cup closer
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=200, force=150, tilt=[0, 0.3, 0])
    # Examine by tilting side to side with subtle tremor
    for _ in range(2):
        env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=100, force=100, tilt=[0, 0.4, 0], noise_amp=0.008, noise_freq=0.7)
        env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=100, force=100, tilt=[0, 0.2, 0], noise_amp=0.008, noise_freq=0.7)
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=100, force=100, tilt=[0, 0.3, 0])
    env.wait(50)