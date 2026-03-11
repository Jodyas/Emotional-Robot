def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup head to the side, slowly approaching the cup with a curious, investigative motion.
    # Start from a slightly higher, neutral position to prepare for observation
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.5], steps=100, force=200)
    # Slowly approach with a curious side-tilt, investigating
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] + 0.1, cup_pos[2] + 0.3], steps=150, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.3, 0])
    env.wait(30) # A brief pause to "look"

    # Step 3: Slowly and deliberately move the arm above the cup, perhaps circling it slightly, as if examining it from different angles.
    # Examine from one side
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] - 0.05, cup_pos[2] + 0.25], steps=120, force=120, tilt=[0, 0.2, 0.1])
    env.wait(20)
    # Examine from another side
    env.move_to([cup_pos[0] - 0.05, cup_pos[1] + 0.05, cup_pos[2] + 0.25], steps=120, force=120, tilt=[0, 0.2, -0.1])
    env.wait(20)
    # Move directly above the cup, still curious
    env.move_to("cup", steps=150, force=120, tilt=[0, 0.3, 0])

    # Step 4: Timing: Hold perfectly still above the cup, observing it with a slight head tilt – a moment of curious contemplation.
    env.wait(80) # Long contemplation

    # Step 5: Lower the arm, activate suction, lift the cup slightly, then perform a brief, erratic downward jerk to simulate the cup slipping, immediately followed by re-securing it with suction and lifting it carefully.
    # Lower the arm to pick up
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=100, force=150, tilt=[0, 0.1, 0])
    env.activate_suction()
    env.wait(20)
    # Lift slightly
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=80, force=150, tilt=[0, 0.1, 0])
    env.wait(10)

    # Simulate the cup slipping: brief release, quick downward jerk, re-secure, lift carefully
    env.deactivate_suction()
    env.wait(5) # Moment of release
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.02], steps=30, force=500, noise_amp=0.05, noise_freq=1.0, tilt=[0.1, 0.2, 0]) # Quick jerk down
    env.activate_suction()
    env.wait(15) # Re-securing
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.20], steps=100, force=200, noise_amp=0.008, noise_freq=0.7, tilt=[0, 0.1, 0]) # Lift carefully

    # Step 6: Timing: Pause after the 'slip' and re-secure, holding the cup gingerly to show it's now stable but still perceived as slippery.
    env.wait(70) # Pause, holding gingerly

    # Step 7: Carefully lift the cup higher above the table, making small, precise adjustments to maintain a secure grip, still showing a hint of caution.
    # Lift higher with caution and small adjustments
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=180, force=180, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.1, 0])

    # Step 8: Follow Through: Slowly bring the cup closer to the 'body' of the robot, tilting the suction cup head again, as if examining its 'catch' with continued curiosity and carefulness.
    # Bring closer to "examine" with continued curiosity
    env.move_to([cup_pos[0] - 0.15, cup_pos[1] - 0.1, cup_pos[2] + 0.40], steps=150, force=150, noise_amp=0.003, noise_freq=0.3, tilt=[0, 0.3, 0])
    env.wait(50)