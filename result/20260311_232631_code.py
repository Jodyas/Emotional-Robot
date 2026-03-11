def execute(env):
    # Step 1: Detect and confirm the cup's position on the table with a sharp, focused movement.
    cup_pos = env.get_object_position("cup")
    # Move quickly and sharply to a point just above the cup to "confirm" its presence.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=70, force=500, tilt=[0, 0.2, 0])
    env.wait(30) # A brief, sharp pause

    # Step 2: Anticipation: Perform a sharp, aggressive jerk of the arm, as if in frustrated impatience, with the suction cup tilting aggressively.
    # Jerk arm slightly back and up, with an angry tilt.
    env.move_to([cup_pos[0] - 0.05, cup_pos[1] - 0.05, cup_pos[2] + 0.35], steps=40, force=600, tilt=[0, 0.5, 0])
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] + 0.05, cup_pos[2] + 0.30], steps=40, force=600, tilt=[0, -0.5, 0])

    # Step 3: Timing: Hold perfectly still for a tense beat, building up to the angry action.
    env.wait(80)

    # Step 4: Rush the arm directly above the cup with high speed and aggressive, jerky movements, showing anger.
    env.move_to("cup", steps=60, force=700, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0.3, 0])

    # Step 5: Slam the arm down forcefully, activate suction, then thrust the cup up abruptly and quickly, showing an angry grab.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.03], steps=25, force=800) # Slam down
    env.activate_suction()
    env.wait(10) # Quick grab
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=40, force=700, tilt=[0, -0.2, 0]) # Thrust up aggressively

    # Step 6: Timing: Freeze! A dramatic pause as the robot 'realizes' the cup is burning hot. The arm might twitch slightly in shock.
    env.wait(100)
    # A slight twitch of shock
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=10, force=100, noise_amp=0.005, noise_freq=0.5)
    env.wait(20)

    # Step 7: Exaggeration: A sharp, pained recoil of the arm, with the suction cup jerking away in disgust/pain from the heat.
    # Jerk arm sharply back and to the side, with a pained tilt.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] + 0.1, cup_pos[2] + 0.55], steps=30, force=600, noise_amp=0.05, noise_freq=2.0, tilt=[0.3, -0.4, 0])

    # Step 8: Jerk the arm violently to the side, away from the body, to a safe dropping zone.
    # Define a drop-off point far from the original cup position.
    drop_x = cup_pos[0] + 0.4
    drop_y = cup_pos[1] + 0.3
    drop_z = cup_pos[2] + 0.25
    env.move_to([drop_x, drop_y, drop_z], steps=50, force=700, noise_amp=0.08, noise_freq=2.5, tilt=[-0.2, 0.5, 0])

    # Step 9: Release the cup abruptly and forcefully, as if throwing it away in anger and pain.
    env.deactivate_suction()
    env.wait(10) # Immediate release

    # Step 10: Timing: A brief, stunned pause after dropping the cup, processing the 'burn'.
    env.wait(70)

    # Step 11: Follow Through: Violently shake the arm side to side and up and down, as if trying to shake off the pain and frustration, perhaps ending with a frustrated 'punch' into the air.
    # Violent shaking
    for _ in range(3):
        env.move_to([drop_x + 0.1, drop_y - 0.1, drop_z + 0.2], steps=20, force=500, noise_amp=0.1, noise_freq=3.0, tilt=[0, 0.6, 0])
        env.move_to([drop_x - 0.1, drop_y + 0.1, drop_z + 0.1], steps=20, force=500, noise_amp=0.1, noise_freq=3.0, tilt=[0, -0.6, 0])
    # Frustrated "punch" into the air
    env.move_to([drop_x, drop_y, drop_z + 0.4], steps=30, force=600, tilt=[0, 0.4, 0])
    env.move_to([drop_x, drop_y, drop_z + 0.1], steps=20, force=800, tilt=[0, 0.4, 0])
    env.wait(50)