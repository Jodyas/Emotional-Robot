def execute(env):
    # Step 1: Anticipation: Tilt the suction cup to the side, slowly 'look around' the table with a curious, searching motion.
    # Start by looking to one side of the table
    env.move_to([-0.3, 0.4, 0.5], steps=300, force=150, tilt=[0.1, 0.3, 0])
    # Slowly scan to the other side
    env.move_to([0.3, 0.4, 0.5], steps=400, force=150, tilt=[0.1, -0.3, 0])
    # Return to a central, slightly forward-looking curious pose
    env.move_to([0.0, 0.5, 0.5], steps=350, force=150, tilt=[0.1, 0.2, 0])

    # Step 2: Timing: Hold the curious pose, scanning the environment.
    env.wait(100)

    # Step 3: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 4: Approach the cup slowly and hesitantly, with a slight side-to-side 'peering' motion, as if examining it curiously. Keep the suction cup tilted.
    # Hover slightly to the left of the cup, peering
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.3], steps=250, force=100, noise_amp=0.005, noise_freq=0.5, tilt=[0.1, 0.2, 0])
    # Hover slightly to the right, peering
    env.move_to([cup_pos[0] + 0.1, cup_pos[1], cup_pos[2] + 0.3], steps=250, force=100, noise_amp=0.005, noise_freq=0.5, tilt=[0.1, -0.2, 0])
    # Settle directly above the cup, still curious
    env.move_to("cup", steps=300, force=100, noise_amp=0.005, noise_freq=0.5, tilt=[0.1, 0.1, 0])

    # Step 5: Timing: Pause directly above the cup, observing it closely with a slight tilt, building anticipation for the grab.
    env.wait(80)

    # Step 6: Lower the arm towards the cup with a slight jitter, activate suction, and begin to lift. This is the initial attempt to pick up.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=150, force=150, noise_amp=0.01, noise_freq=0.8, tilt=[0.1, 0.1, 0])
    env.activate_suction()
    env.wait(30)
    # Initial slight lift
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=80, force=150, tilt=[0.1, 0.1, 0])

    # Step 7: Show, Don't Tell: Immediately after initial suction, perform a quick, small, uncontrolled 'slip' movement.
    # A sudden jerk down and to the side
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] - 0.05, cup_pos[2] + 0.1], steps=40, force=300, noise_amp=0.05, noise_freq=2.0, tilt=[0.2, -0.1, 0])

    # Step 8: Timing: A brief pause, as if the robot is regaining control after the slip, re-evaluating its grip.
    env.wait(50)

    # Step 9: Carefully re-center and lift the cup smoothly after correcting the slip, holding it gingerly.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=250, force=150, noise_amp=0.008, noise_freq=0.6, tilt=[0.05, 0.05, 0])

    # Step 10: Timing: Hold the cup steady for a moment, letting the audience register it's now securely held, but still 'slippery'.
    env.wait(70)

    # Step 11: Follow Through: Gently pull the cup closer, holding it with a slight, continuous wobble to emphasize its 'slippery' nature. The suction cup maintains a curious tilt, as if still examining the object.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=200, force=120, noise_amp=0.015, noise_freq=0.7, tilt=[0.1, 0.2, 0])
    env.wait(100)