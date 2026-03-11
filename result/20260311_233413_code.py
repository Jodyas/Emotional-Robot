def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup slightly to the side, as if observing the cup with curiosity and a hint of skepticism about its 'slippery' nature.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=250, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold still for a moment, letting the curious observation register.
    env.wait(70)

    # Step 4: Move the arm slowly and deliberately above the cup, with a slight, investigative wobble, maintaining the curious tilt.
    env.move_to("cup", steps=300, force=180, noise_amp=0.008, noise_freq=0.7, tilt=[0, 0.3, 0])

    # Step 5: Timing: Pause briefly above the cup, as if carefully assessing the best approach for a slippery object.
    env.wait(50)

    # Step 6: Lower the arm, activate suction, and attempt to lift the cup. Describe this as a slightly unstable initial grab.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=150, force=200, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.2, 0])
    env.activate_suction()
    env.wait(30)
    # Attempt to lift, but with a slight wobble indicating instability
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=100, force=250, noise_amp=0.01, noise_freq=1.0, tilt=[0, 0.2, 0])

    # Step 7: Act Out Object Properties: A quick, small downward jerk of the arm, simulating the cup slipping slightly in the suction cup's grip.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=40, force=300, noise_amp=0.03, noise_freq=1.5, tilt=[0, 0.1, 0])

    # Step 8: Timing: A brief, surprised pause after the slip, then a quick adjustment.
    env.wait(40)
    # Quick adjustment upwards slightly before re-gripping
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.20], steps=50, force=250, tilt=[0, 0.2, 0])

    # Step 9: Re-establish a firm grip and lift the cup carefully, confirming it's now securely held.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=80, force=250, tilt=[0, 0.1, 0]) # Move down to re-engage
    env.activate_suction() # Re-activate to ensure firm grip
    env.wait(30)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=200, force=200, noise_amp=0.0, noise_freq=0.0, tilt=[0, 0.1, 0]) # Smooth, secure lift

    # Step 10: Timing: Hold the cup steady after the successful (but challenging) pickup, confirming the grip.
    env.wait(80)

    # Step 11: Follow Through: Gently bring the cup closer, tilting the suction cup again as if examining the 'slippery' cup with continued curiosity and a hint of satisfaction at overcoming the challenge.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=250, force=180, noise_amp=0.005, noise_freq=0.6, tilt=[0, 0.3, 0])
    env.wait(50)