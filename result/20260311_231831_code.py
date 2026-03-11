def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Jerk the arm sharply and quickly, as if in a burst of frustration or impatience.
    # Start from a neutral hover, then a sharp upward jerk, followed by a sharp downward snap.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=100, force=300) # Initial hover
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.5], steps=30, force=500, noise_amp=0.05, noise_freq=1.5, tilt=[0, 0.3, 0]) # Sharp upward jerk with angry tilt
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=30, force=600, noise_amp=0.05, noise_freq=1.5, tilt=[0, -0.3, 0]) # Sharp downward snap

    # Step 3: Timing: Hold perfectly still for a brief, tense moment after the initial angry gesture.
    env.wait(steps=80)

    # Step 4: Slam the arm down towards the cup with a fast, direct, and slightly jerky motion, showing aggression.
    env.move_to("cup", steps=50, force=700, noise_amp=0.02, noise_freq=1.0, tilt=[0.1, 0, 0])

    # Step 5: Activate suction with a sudden, forceful movement, then yank the cup upwards quickly and aggressively.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.02], steps=20, force=800) # Slam down onto the cup
    env.activate_suction()
    env.wait(10) # Brief moment of forceful contact
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=40, force=700, noise_amp=0.03, noise_freq=1.5, tilt=[-0.1, 0, 0]) # Yank upwards aggressively

    # Step 6: Timing: Hold the cup rigidly in the air for a brief, sharp moment, conveying the force of the grab.
    env.wait(steps=70)

    # Step 7: Follow Through: Thrust the cup slightly forward and then pull it back sharply, or give it a small, aggressive shake, as if challenging it or showing dominance.
    # Aggressive forward thrust
    env.move_to([cup_pos[0] + 0.1, cup_pos[1], cup_pos[2] + 0.45], steps=30, force=600, tilt=[0, 0.3, 0])
    # Sharp pull back
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.45], steps=30, force=600, tilt=[0, -0.3, 0])
    # Small aggressive shake
    for _ in range(2):
        env.move_to([cup_pos[0], cup_pos[1] + 0.05, cup_pos[2] + 0.45], steps=20, force=500, noise_amp=0.05, noise_freq=2.0)
        env.move_to([cup_pos[0], cup_pos[1] - 0.05, cup_pos[2] + 0.45], steps=20, force=500, noise_amp=0.05, noise_freq=2.0)