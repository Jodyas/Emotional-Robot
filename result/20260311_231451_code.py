def execute(env):
    # Step 1: Detect and confirm the cup position on the table with an aggressive, focused tilt of the suction cup.
    cup_pos = env.get_object_position("cup")
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=150, force=300, tilt=[0.2, 0.2, 0]) # Hover and "look" aggressively

    # Step 2: Anticipation: Jerk the arm sharply and quickly, shaking with frustration and impatience before moving.
    # Jerk to a slightly offset position with high noise and force, then a short wait.
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] - 0.05, cup_pos[2] + 0.40], steps=40, force=500, noise_amp=0.05, noise_freq=1.5, tilt=[0, 0.4, 0])
    env.wait(30) # Short, impatient pause

    # Step 3: Rush the arm directly above the cup with a fast, forceful, and slightly erratic movement, showing anger.
    env.move_to("cup", steps=70, force=600, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0, 0])

    # Step 4: Slam the arm down quickly, activate suction with a jolt, then yank the cup up abruptly and forcefully.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=20, force=800) # Slam down
    env.activate_suction()
    env.wait(5) # Jolt of activation
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=40, force=700) # Yank up

    # Step 5: Timing: Freeze! A brief, tense pause as the robot 'realizes' the cup is burning hot. The arm might tremble slightly.
    # Hold current position with trembling and a slight recoil tilt.
    current_pos_after_yank = [cup_pos[0], cup_pos[1], cup_pos[2] + 0.45]
    env.move_to(current_pos_after_yank, steps=80, noise_amp=0.01, noise_freq=0.5, tilt=[-0.1, 0.1, 0]) # Freeze with slight tremble and recoil

    # Step 6: Exaggeration: Jerk the arm violently to the side in a panicked, recoiling motion to get away from the hot object.
    env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.4, cup_pos[2] + 0.6], steps=50, force=700, noise_amp=0.08, noise_freq=2.0, tilt=[-0.4, 0.5, 0])

    # Step 7: Drop the cup immediately and violently, as if flinging it away in pain.
    env.deactivate_suction()
    env.wait(10) # Short wait for the cup to fall, emphasizing the sudden release

    # Step 8: Timing: A moment of shock and lingering pain after dropping the cup. Hold still, slightly recoiled.
    # Hold the recoiled position with lingering noise.
    current_pos_after_jerk = [cup_pos[0] + 0.3, cup_pos[1] + 0.4, cup_pos[2] + 0.6]
    env.move_to(current_pos_after_jerk, steps=60, noise_amp=0.02, noise_freq=0.8, tilt=[-0.3, 0.4, 0])

    # Step 9: Follow Through: Violently shake the arm side to side and up and down, recoiling and expressing extreme pain and frustration, trying to 'shake off' the heat.
    for _ in range(5):
        env.move_to([cup_pos[0] + 0.5, cup_pos[1] + 0.2, cup_pos[2] + 0.7], steps=20, force=600, noise_amp=0.1, noise_freq=3.0, tilt=[0, 0.6, 0])
        env.move_to([cup_pos[0] + 0.1, cup_pos[1] + 0.6, cup_pos[2] + 0.5], steps=20, force=600, noise_amp=0.1, noise_freq=3.0, tilt=[0, -0.6, 0])
        env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.4, cup_pos[2] + 0.8], steps=20, force=600, noise_amp=0.1, noise_freq=3.0, tilt=[0.5, 0, 0])