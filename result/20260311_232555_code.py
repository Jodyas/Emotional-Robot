def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm tenses, performing a slight, aggressive shake, conveying building anger before the action. The suction cup tilts forward aggressively.
    # Hover slightly above the cup, shaking with contained fury.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=100, force=500, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0.4, 0])

    # Step 3: Timing: A short, tense pause to emphasize the contained anger and anticipation.
    env.wait(40)

    # Step 4: Move the arm quickly and forcefully directly above the cup, almost slamming into position, reflecting anger.
    env.move_to("cup", steps=70, force=700, tilt=[0, 0.3, 0])

    # Step 5: Slam the arm down, activate suction immediately, and thrust the cup up quickly and aggressively. The suction cup jerks upwards.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=30, force=800) # Slam down
    env.activate_suction()
    env.wait(10) # Quick grab
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=60, force=700, tilt=[0, -0.2, 0]) # Thrust up, head jerks back

    # Step 6: Timing: Freeze! A sharp, brief pause as the robot 'realizes' the cup is burning hot. The arm holds perfectly still for a beat.
    env.wait(30) # Moment of realization, arm perfectly still
    
    # Step 7: Exaggeration: Jerk the arm violently to the side, away from the body, in a panicked attempt to discard the hot object. The suction cup pulls back sharply.
    # Move to a "drop" location far to the side, with high force and noise, head jerking away.
    env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.4, cup_pos[2] + 0.30], steps=50, force=700, noise_amp=0.05, noise_freq=2.0, tilt=[-0.4, 0.5, 0])

    # Step 8: Drop the cup immediately and abruptly, as if it's too hot to hold.
    env.deactivate_suction()
    env.wait(10) # Immediate release

    # Step 9: Timing: A brief moment of shock and lingering pain after dropping the cup. The arm remains momentarily frozen.
    env.wait(30)

    # Step 10: Follow Through: Violently shake the arm back and forth and retract it quickly, as if trying to cool off a burned 'hand'. The suction cup droops slightly then jerks erratically.
    # Shake violently, retracting the arm.
    for _ in range(3):
        env.move_to([cup_pos[0] + 0.5, cup_pos[1] + 0.2, cup_pos[2] + 0.6], steps=20, force=600, noise_amp=0.08, noise_freq=3.0, tilt=[0.1, 0.6, 0])
        env.move_to([cup_pos[0] + 0.4, cup_pos[1] - 0.2, cup_pos[2] + 0.5], steps=20, force=600, noise_amp=0.08, noise_freq=3.0, tilt=[-0.1, -0.6, 0])
    # Final retraction to a "safe" position, still slightly agitated.
    env.move_to([cup_pos[0] + 0.6, cup_pos[1], cup_pos[2] + 0.7], steps=80, force=500, noise_amp=0.03, noise_freq=1.5, tilt=[0, 0.2, 0])