def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm recoils slightly, trembling violently, as if hesitant to even look at the cup. The suction cup tilts away in dread.
    # Recoil slightly back and up, with violent trembling and tilting away.
    env.move_to([cup_pos[0], cup_pos[1] - 0.2, cup_pos[2] + 0.4], steps=150, force=200, noise_amp=0.05, noise_freq=2.0, tilt=[0.3, 0.3, 0])

    # Step 3: Timing: Hold perfectly still for a dramatic pause, letting the fear build.
    env.wait(150)

    # Step 4: Hesitant approach: Move the arm very slowly and jerkily towards the cup, stopping short, as if too scared to get close. The suction cup droops.
    # Move slowly towards the cup, but stop above it with an offset, trembling, and drooping tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.2], steps=400, force=150, noise_amp=0.02, noise_freq=1.0, tilt=[0.4, 0, 0])

    # Step 5: Timing: Freeze above the cup, trembling slightly, staring at it with extreme reluctance.
    env.wait(100) # A longer wait to emphasize the reluctance
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.2], steps=50, force=100, noise_amp=0.01, noise_freq=0.8, tilt=[0.4, 0, 0]) # Small tremble in place

    # Step 6: Exaggeration: With a sudden, jerky dart, the arm quickly moves directly over the cup, as if forcing itself to act.
    # Fast, jerky movement directly over the cup.
    env.move_to("cup", steps=70, force=400, noise_amp=0.03, noise_freq=1.5)

    # Step 7: Grab quickly: Slam down, activate suction, and immediately yank the cup upwards and away from the table with a shudder.
    # Slam down quickly.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=30, force=600)
    env.activate_suction()
    env.wait(10) # Brief hold
    # Yank upwards and away with a shudder.
    env.move_to([cup_pos[0] + 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.4], steps=60, force=500, noise_amp=0.04, noise_freq=1.8)

    # Step 8: Timing: A brief, shaky pause after lifting, holding the cup tightly, still trembling.
    env.wait(80)
    env.move_to([cup_pos[0] + 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.4], steps=30, force=100, noise_amp=0.02, noise_freq=1.0) # Small tremble in place

    # Step 9: Follow Through: Quickly pull the cup close to the robot's 'body' and tremble violently, as if holding something terrifying and wanting to hide it, or keep it safe from itself. The suction cup is angled down, 'looking' at the cup with wide-eyed fear.
    # Pull the cup close, trembling violently, with the end-effector angled down.
    env.move_to([cup_pos[0] - 0.2, cup_pos[1], cup_pos[2] + 0.3], steps=150, force=300, noise_amp=0.06, noise_freq=2.5, tilt=[0.2, 0, 0])
    env.wait(100) # Hold the trembling pose