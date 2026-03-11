def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Curiosity: Tilt the suction cup slightly to the side, slowly moving the arm in a small arc around the cup, as if examining it with interest.
    # Hover above the cup first with a curious tilt
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=100, force=150, tilt=[0, 0.3, 0])
    # Move in a small arc to the left
    env.move_to([cup_pos[0] - 0.08, cup_pos[1] + 0.05, cup_pos[2] + 0.35], steps=80, force=150, tilt=[0, 0.35, 0])
    # Move in a small arc to the right
    env.move_to([cup_pos[0] + 0.08, cup_pos[1] - 0.05, cup_pos[2] + 0.35], steps=80, force=150, tilt=[0, 0.25, 0])
    # Return to center above the cup
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=80, force=150, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold still for a moment, letting the audience 'read' the curious pose.
    env.wait(50)

    # Step 4: Curious Approach: Slowly and smoothly move the arm directly above the cup, with a slight, gentle wobble, as if carefully investigating before touching.
    env.move_to("cup", steps=120, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.2, 0])

    # Step 5: Hot Cup Grab: Lower the arm quickly, activate suction, and immediately lift the cup with a sharp, surprised jerk, indicating it's hot.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=40, force=500) # Lower quickly
    env.activate_suction()
    env.wait(10) # Short wait to ensure suction
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=30, force=700, noise_amp=0.02, noise_freq=1.0, tilt=[0.1, 0, 0]) # Jerk upwards

    # Step 6: Timing: Freeze! A brief, dramatic pause as the robot 'realizes' the cup is burning hot.
    env.wait(40)

    # Step 7: Pain/Panic: Violently shake the arm back and forth while holding the cup, as if trying to cool it down or get rid of the heat.
    for _ in range(3):
        env.move_to([cup_pos[0] + 0.15, cup_pos[1], cup_pos[2] + 0.4], steps=20, force=600, noise_amp=0.08, noise_freq=2.0, tilt=[0, 0.4, 0])
        env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.4], steps=20, force=600, noise_amp=0.08, noise_freq=2.0, tilt=[0, -0.4, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.5], steps=20, force=600, noise_amp=0.08, noise_freq=2.0, tilt=[0, 0, 0]) # Settle slightly after shaking

    # Step 8: Anticipation/Wind-up: Sharply pull the arm back and to the side, preparing for a forceful throw, showing anger and urgency.
    env.move_to([cup_pos[0] - 0.3, cup_pos[1] - 0.3, cup_pos[2] + 0.6], steps=50, force=700, tilt=[-0.2, -0.5, 0])

    # Step 9: Throw: Forcefully extend the arm forward and release the cup with a sudden, aggressive motion, simulating throwing it away in pain.
    throw_target = [cup_pos[0] + 0.6, cup_pos[1] + 0.6, cup_pos[2] + 0.2]
    env.move_to(throw_target, steps=30, force=800, tilt=[0.1, 0.5, 0])
    env.deactivate_suction()
    env.wait(5) # Short wait for the cup to detach

    # Step 10: Follow Through: Immediately recoil the arm sharply after the throw, then shake it vigorously in the air, as if still feeling the burn and expressing lingering pain and frustration.
    env.move_to([throw_target[0] - 0.2, throw_target[1] - 0.2, throw_target[2] + 0.4], steps=20, force=700, tilt=[-0.3, -0.3, 0]) # Sharp recoil
    for _ in range(4):
        env.move_to([throw_target[0] + 0.1, throw_target[1], throw_target[2] + 0.7], steps=20, force=500, noise_amp=0.07, noise_freq=2.5, tilt=[0, 0.3, 0])
        env.move_to([throw_target[0] - 0.1, throw_target[1], throw_target[2] + 0.7], steps=20, force=500, noise_amp=0.07, noise_freq=2.5, tilt=[0, -0.3, 0])
    env.wait(50) # Lingering frustration