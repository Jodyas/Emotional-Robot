def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Jerk the arm aggressively and quickly, showing building anger and impatience. The suction cup tilts sharply.
    # First, a quick aggressive move away, then a sharp tilt towards the cup.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] + 0.1, cup_pos[2] + 0.4], steps=40, force=500, noise_amp=0.03, noise_freq=1.5, tilt=[0, 0.5, 0])
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] - 0.05, cup_pos[2] + 0.45], steps=40, force=550, noise_amp=0.04, noise_freq=1.8, tilt=[0, -0.5, 0])

    # Step 3: Timing: Hold perfectly still for a dramatic beat, letting the anger simmer before the action.
    env.wait(70)

    # Step 4: Rush the arm directly above the cup with a fast, forceful, and slightly jerky motion, expressing aggression.
    env.move_to("cup", steps=60, force=700, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0.2, 0])

    # Step 5: Slam the arm down quickly, activate suction with a jolt, and thrust the cup up abruptly. The suction cup recoils slightly as if burned.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=30, force=800, noise_amp=0.01, noise_freq=0.5) # Slam down
    env.activate_suction()
    env.wait(10) # Jolt of activation
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=50, force=750, noise_amp=0.03, noise_freq=1.2, tilt=[0.1, 0, 0]) # Thrust up
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.40], steps=20, force=600, noise_amp=0.05, noise_freq=2.0) # Slight recoil/burn

    # Step 6: Timing: Freeze! A brief, tense pause as the robot 'realizes' the cup is burning hot. The arm tenses up.
    env.wait(40)

    # Step 7: Exaggeration: Jerk the arm violently to the side, flinging the 'hot' cup away from the table in panic and anger.
    # Move far away with high force and noise, head jerking away in disgust/pain.
    env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.4, cup_pos[2] + 0.5], steps=40, force=800, noise_amp=0.08, noise_freq=2.5, tilt=[-0.4, 0.6, 0])

    # Step 8: Release the cup immediately and abruptly, as if it's too hot to hold.
    env.deactivate_suction()
    env.wait(10) # Abrupt release

    # Step 9: Timing: A moment of shock and lingering anger after dropping the cup. Hold still.
    env.wait(50)

    # Step 10: Follow Through: Violently shake the arm back and forth, then wave it angrily in the air, expressing both the pain from the 'burn' and the lingering frustration/anger.
    # Violent shaking
    for _ in range(3):
        env.move_to([cup_pos[0] + 0.5, cup_pos[1] + 0.2, cup_pos[2] + 0.7], steps=20, force=600, noise_amp=0.1, noise_freq=3.0, tilt=[0, 0.7, 0])
        env.move_to([cup_pos[0] + 0.3, cup_pos[1] - 0.2, cup_pos[2] + 0.6], steps=20, force=600, noise_amp=0.1, noise_freq=3.0, tilt=[0, -0.7, 0])
    # Angry waving
    env.move_to([cup_pos[0] + 0.6, cup_pos[1], cup_pos[2] + 0.8], steps=40, force=500, noise_amp=0.05, noise_freq=2.0, tilt=[-0.2, 0.5, 0])
    env.move_to([cup_pos[0] + 0.4, cup_pos[1], cup_pos[2] + 0.7], steps=40, force=500, noise_amp=0.05, noise_freq=2.0, tilt=[-0.2, -0.5, 0])
    env.wait(30)