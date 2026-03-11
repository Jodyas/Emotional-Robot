def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Flinch back slightly, then slowly and tentatively extend the arm, showing initial fear and hesitation. The suction cup tilts away slightly.
    # Flinch back quickly
    env.move_to([cup_pos[0] - 0.15, cup_pos[1] - 0.1, cup_pos[2] + 0.4], steps=50, force=300, tilt=[0, 0.3, 0])
    env.wait(30) # Short pause after flinching

    # Tentatively extend arm, hovering, with slight tremble and tilting away
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.35], steps=300, force=150, noise_amp=0.01, noise_freq=0.8, tilt=[0, -0.2, 0])

    # Step 3: Timing: Hold still, letting the audience feel the robot's apprehension before approaching the 'spiky' object.
    env.wait(150)

    # Step 4: Move the arm extremely slowly and hesitantly towards the cup, with high jitter/trembling, as if trying to avoid touching the 'spikes'. The suction cup droops slightly.
    env.move_to("cup", steps=400, force=100, noise_amp=0.03, noise_freq=1.0, tilt=[0.1, 0.1, 0])

    # Step 5: Timing: Hover above the cup, trembling, as if gathering courage for the final descent. A brief recoil before committing.
    env.wait(80) # Hover and tremble
    # Brief recoil
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.2], steps=40, force=150, noise_amp=0.01, noise_freq=0.5, tilt=[0.1, 0.1, 0])
    env.wait(20) # Short pause before committing

    # Step 6: A very, very slow and careful descent onto the cup, bracing for contact, with slight trembling.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=500, force=80, noise_amp=0.015, noise_freq=0.7, tilt=[0.05, 0.05, 0])

    # Step 7: Activate suction, then lift the cup extremely slowly and gingerly, pulling it straight up to avoid brushing any 'spikes'.
    env.activate_suction()
    env.wait(30) # Brief moment of contact
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=450, force=120, noise_amp=0.01, noise_freq=0.6, tilt=[0, 0, 0])

    # Step 8: Timing: Pause after lifting, holding the cup away from the body, trembling slightly, as if relieved but still wary.
    env.wait(100)

    # Step 9: Follow Through: Pull the cup further away from the body, holding it at arm's length, and shiver/tremble continuously, showing lingering fear and discomfort with the 'spiky' object. The suction cup remains tilted away.
    # Pull further away, shivering
    env.move_to([cup_pos[0] - 0.25, cup_pos[1] - 0.15, cup_pos[2] + 0.5], steps=300, force=150, noise_amp=0.025, noise_freq=1.5, tilt=[0, -0.3, 0])
    # Continue shivering in place
    for _ in range(3):
        env.move_to([cup_pos[0] - 0.25, cup_pos[1] - 0.15, cup_pos[2] + 0.5], steps=50, force=100, noise_amp=0.03, noise_freq=2.0, tilt=[0, -0.3, 0])
        env.wait(20)