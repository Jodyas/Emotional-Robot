def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Perform a happy, bouncy little jig with the arm, suction cup tilted up cheerfully, before approaching the cup.
    # Start from a neutral high position, then bounce around.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.5], steps=100, force=200, tilt=[-0.2, 0, 0]) # Initial cheerful high pose
    env.move_to([cup_pos[0] + 0.1, cup_pos[1] + 0.1, cup_pos[2] + 0.45], steps=150, force=250, noise_amp=0.005, noise_freq=0.5, tilt=[-0.2, 0.1, 0]) # Bounce 1
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.55], steps=150, force=250, noise_amp=0.005, noise_freq=0.5, tilt=[-0.2, -0.1, 0]) # Bounce 2
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.5], steps=100, force=200, tilt=[-0.2, 0, 0]) # Return to cheerful high pose

    # Step 3: Timing: Hold a brief, cheerful pose, letting the happiness sink in.
    env.wait(70)

    # Step 4: Move the arm with a light, bouncy, slightly exaggerated motion directly above the cup, as if skipping towards it.
    # Approach with a slight bounce before settling.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=100, force=300, noise_amp=0.008, noise_freq=0.8, tilt=[-0.1, 0, 0]) # Skipping approach
    env.move_to("cup", steps=80, force=250, tilt=[-0.1, 0, 0]) # Settle above cup

    # Step 5: Lower the arm quickly and playfully, activate suction, then lift the cup swiftly, minimizing contact time to acknowledge the 'hot' property.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=40, force=400) # Quick playful lower
    env.activate_suction()
    env.wait(10) # Minimal contact time
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=70, force=350, tilt=[-0.1, 0, 0]) # Swift lift

    # Step 6: Immediately after lifting, perform a very quick, small, sharp jerk of the arm to the side, a subtle 'ouch' reaction to the heat.
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] + 0.05, cup_pos[2] + 0.30], steps=30, force=500, noise_amp=0.02, noise_freq=1.5, tilt=[0, 0.2, 0]) # Sharp jerk

    # Step 7: Timing: A very brief, almost imperceptible pause for the 'hot' jolt, then immediately recover.
    env.wait(15)

    # Step 8: Follow Through: Immediately recover to exaggerated happiness. Perform a celebratory, bouncy wave with the cup, bringing it close as if admiring a prize, completely overriding the 'hot' sensation with joy. Suction cup remains tilted up cheerfully.
    # Recover to a high, cheerful pose, then perform a bouncy wave.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.45], steps=80, force=300, tilt=[-0.2, 0, 0]) # Recover to cheerful high
    for _ in range(3): # Perform a bouncy wave
        env.move_to([cup_pos[0] - 0.2, cup_pos[1] + 0.1, cup_pos[2] + 0.5], steps=120, force=250, noise_amp=0.005, noise_freq=0.5, tilt=[-0.2, 0.1, 0])
        env.move_to([cup_pos[0] - 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.45], steps=120, force=250, noise_amp=0.005, noise_freq=0.5, tilt=[-0.2, -0.1, 0])
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.45], steps=100, force=200, tilt=[-0.2, 0, 0]) # Settle in a proud, close pose
    env.wait(100)