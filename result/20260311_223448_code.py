def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Hover the arm slightly above the table, tilting the suction cup to one side, as if 'peering' at the cup with curiosity.
    # Move to a position slightly above the cup, with a curious side-tilt and a gentle tremble.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=100, force=150, tilt=[0, 0.3, 0], noise_amp=0.005, noise_freq=0.5)

    # Step 3: Timing: Hold the curious pose for a moment, letting the audience register the 'look'.
    env.wait(steps=70)

    # Step 4: Move the arm slowly and deliberately towards the cup, making small, investigative side-to-side movements as if examining it closely.
    # First, a slight shift to one side, maintaining curiosity.
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.20], steps=80, force=100, tilt=[0, 0.2, 0])
    # Then, a slight shift to the other side.
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.20], steps=80, force=100, tilt=[0, 0.2, 0])
    # Finally, move directly above the cup, slowly and deliberately.
    env.move_to("cup", steps=120, force=100, tilt=[0, 0.2, 0])

    # Step 5: Timing: Pause directly above the cup, holding perfectly still, as if 'studying' it before making a move.
    env.wait(steps=50)

    # Step 6: Lower the arm, activate suction, and lift the cup. This action is initially smooth, but immediately followed by a reaction.
    # Lower smoothly to pick up.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=80, force=150)
    env.activate_suction()
    env.wait(20)
    # Lift smoothly.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=80, force=150)

    # Step 7: Timing: Freeze! A sudden, brief pause as the robot 'realizes' the cup is hot. The arm might stiffen slightly.
    env.wait(steps=30)

    # Step 8: Exaggeration: Jerk the arm away from the table quickly and violently, as if recoiling from the heat.
    # Fast, forceful move away with shaking and a strong tilt of disgust/pain.
    env.move_to([cup_pos[0] + 0.2, cup_pos[1] + 0.3, cup_pos[2] + 0.4], steps=40, force=700, noise_amp=0.05, noise_freq=2.0, tilt=[-0.4, 0.5, 0])

    # Step 9: Drop the cup immediately and abruptly, releasing it as if burned.
    env.deactivate_suction()
    env.wait(10)

    # Step 10: Timing: Moment of shock after dropping. Hold the arm stiffly in the air, slightly away from the drop zone.
    env.wait(steps=40)

    # Step 11: Follow Through: Vigorously shake the arm side to side, as if trying to cool off a burned hand, showing clear discomfort and pain.
    # Loop for vigorous shaking, alternating left and right with high noise and force.
    for _ in range(3):
        env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.1, cup_pos[2] + 0.5], steps=20, force=600, noise_amp=0.08, noise_freq=3.0, tilt=[0, 0.6, 0])
        env.move_to([cup_pos[0] - 0.3, cup_pos[1] - 0.1, cup_pos[2] + 0.5], steps=20, force=600, noise_amp=0.08, noise_freq=3.0, tilt=[0, -0.6, 0])