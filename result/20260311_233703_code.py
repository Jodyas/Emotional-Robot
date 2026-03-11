def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm trembles slightly, and the suction cup tilts away, showing initial fear and hesitation.
    # Move slightly above the cup, trembling, with the end-effector "cowering" or looking away.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=250, force=150, noise_amp=0.01, noise_freq=0.8, tilt=[0.3, -0.2, 0])

    # Step 3: Timing: Hold still for a dramatic beat, letting the fear build before approaching.
    env.wait(steps=100)

    # Step 4: Move the arm slowly and hesitantly towards the cup, with noticeable trembling.
    # The suction cup maintains a cautious, slightly averted angle.
    env.move_to("cup", steps=400, force=120, noise_amp=0.015, noise_freq=1.0, tilt=[0.2, -0.1, 0])

    # Step 5: Timing: Pause directly above the cup, making small, nervous adjustments, as if bracing for a difficult task.
    # Hover with increased trembling.
    env.move_to("cup", steps=50, force=100, noise_amp=0.02, noise_freq=1.5, tilt=[0.2, -0.1, 0])
    env.wait(steps=70)

    # Step 6: Lower the arm, activate suction, and begin to lift.
    # Immediately, simulate a slip: drop the cup a tiny bit with a sudden jerk, then quickly re-secure it with exaggerated trembling.
    # The lift is then completed very gingerly.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=200, force=100, noise_amp=0.005, noise_freq=0.5)
    env.activate_suction()
    env.wait(20)

    # Simulate a slip: quick drop then re-secure
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.02], steps=15, force=150, noise_amp=0.05, noise_freq=2.0, tilt=[0.4, 0, 0]) # Sudden jerk downwards
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.06], steps=30, force=200, noise_amp=0.03, noise_freq=1.5, tilt=[0.2, 0, 0]) # Quick re-secure upwards

    # Complete the lift very gingerly
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=350, force=150, noise_amp=0.015, noise_freq=0.8, tilt=[0.1, 0, 0])

    # Step 7: Timing: A longer pause after the near-disaster, showing relief mixed with continued fear and the realization that the cup is indeed slippery.
    env.wait(steps=150)

    # Step 8: Follow Through: Hold the cup very gingerly, pulling it close to the robot's 'body' for safety.
    # The arm continues to tremble slightly, and the suction cup droops, still showing fear and caution.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.30], steps=250, force=120, noise_amp=0.01, noise_freq=0.7, tilt=[0.25, 0.05, 0])
    env.wait(steps=80)