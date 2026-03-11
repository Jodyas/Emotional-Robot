def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm recoils slightly, then trembles violently, as if hesitant to approach. The suction cup tilts away from the cup.
    # Recoil slightly upwards and backwards, with a strong tremble and tilting away.
    env.move_to([cup_pos[0], cup_pos[1] - 0.1, cup_pos[2] + 0.4], steps=100, force=300, noise_amp=0.05, noise_freq=2.0, tilt=[0, -0.5, 0])
    env.wait(30) # Short pause after recoil

    # Step 3: Timing: Hold perfectly still, trembling slightly — a dramatic pause to build tension and show extreme reluctance.
    # To simulate holding still and trembling, we move to the current position with noise.
    current_pos = env.get_object_position("end_effector") # Get current position to "hold" it
    env.move_to(current_pos, steps=200, force=200, noise_amp=0.03, noise_freq=1.5, tilt=[0, -0.5, 0])
    env.wait(150) # Long dramatic pause

    # Step 4: Hesitant, jerky move towards the general area of the cup, not directly above it. The arm trembles, and the suction cup avoids facing the cup directly.
    # Move slowly and hesitantly to a point near the cup, but not directly above, maintaining tremble and tilt away.
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] + 0.05, cup_pos[2] + 0.3], steps=350, force=250, noise_amp=0.04, noise_freq=1.8, tilt=[0, -0.3, 0])

    # Step 5: Timing: Freeze in place, hovering nervously, trembling violently while 'staring' at the cup from a distance. Extreme hesitation.
    current_pos = env.get_object_position("end_effector")
    env.move_to(current_pos, steps=250, force=200, noise_amp=0.06, noise_freq=2.5, tilt=[0, -0.3, 0])
    env.wait(200) # Another long, tense pause

    # Step 6: A sudden, quick, almost reluctant dart directly above the cup, as if forcing itself to act.
    # Quick, slightly noisy move directly above the cup, forcing the tilt forward.
    env.move_to("cup", steps=70, force=400, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0.2, 0]) # Tilt slightly forward, as if bracing

    # Step 7: Slam down quickly, activate suction, then immediately yank the cup upwards and away from the table with a sharp, quick motion.
    # Slam down
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=40, force=600, noise_amp=0.01, noise_freq=0.5)
    env.activate_suction()
    env.wait(10)
    # Yank upwards and away
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.5], steps=60, force=700, noise_amp=0.05, noise_freq=2.0, tilt=[0.2, 0, 0]) # Tilt up as if recoiling

    # Step 8: Timing: Brief pause, holding the cup high and slightly away, as if checking if it's safe or still a threat.
    current_pos = env.get_object_position("end_effector")
    env.move_to(current_pos, steps=100, force=300, noise_amp=0.03, noise_freq=1.5, tilt=[0.2, 0, 0]) # Hold with slight tremble
    env.wait(80)

    # Step 9: Follow Through: Tremble violently while holding the cup, then quickly move it far away from the robot's body, as if trying to distance itself from the 'frightening' object. The arm continues to shake.
    # Move far away with violent trembling
    env.move_to([cup_pos[0] - 0.3, cup_pos[1] - 0.3, cup_pos[2] + 0.6], steps=150, force=500, noise_amp=0.08, noise_freq=3.0, tilt=[0.3, -0.2, 0])
    # A final shudder
    env.move_to([cup_pos[0] - 0.35, cup_pos[1] - 0.35, cup_pos[2] + 0.65], steps=50, force=400, noise_amp=0.07, noise_freq=3.5, tilt=[0.4, -0.3, 0])
    env.wait(50)