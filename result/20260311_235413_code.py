def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Perform a cheerful, bouncy wave with the arm, tilting the suction cup upwards happily.
    # Start with a high, happy position.
    env.move_to([cup_pos[0] - 0.2, cup_pos[1] + 0.2, cup_pos[2] + 0.6], steps=150, force=200, tilt=[-0.3, 0, 0])
    # Bounce up slightly
    env.move_to([cup_pos[0] - 0.2, cup_pos[1] + 0.2, cup_pos[2] + 0.65], steps=80, force=150, tilt=[-0.4, 0, 0])
    # Bounce down slightly
    env.move_to([cup_pos[0] - 0.2, cup_pos[1] + 0.2, cup_pos[2] + 0.55], steps=80, force=150, tilt=[-0.2, 0, 0])
    # Return to a cheerful mid-wave position
    env.move_to([cup_pos[0] - 0.2, cup_pos[1] + 0.2, cup_pos[2] + 0.6], steps=100, force=200, tilt=[-0.3, 0, 0])

    # Step 3: Timing: Hold the happy pose briefly to let the emotion register.
    env.wait(70)

    # Step 4: Move the arm smoothly and happily towards the cup, but with a slight, subtle 'brace' or hesitation as it approaches, anticipating the weight.
    # Move towards the cup, still with a slight happy tilt, but add subtle noise for anticipation/bracing.
    env.move_to("cup", steps=250, force=250, noise_amp=0.005, noise_freq=0.5, tilt=[-0.1, 0, 0])

    # Step 5: Timing: Pause directly above the cup, holding perfectly still, as if gathering strength and bracing for the heavy lift.
    env.wait(100)

    # Step 6: Lower the arm slowly, activate suction, then lift the cup *very slowly* and with significant *trembling* and *strained effort* to show it is heavy. The arm should struggle slightly upwards.
    # Lower slowly to grab.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=200, force=300)
    env.activate_suction()
    env.wait(30)
    # Lift *very slowly* with *trembling* and *strained effort*.
    # Initial lift with significant struggle.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.2], steps=400, force=800, noise_amp=0.02, noise_freq=0.3, tilt=[0.1, 0, 0])
    # Continue lifting, still struggling but gaining height.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=500, force=800, noise_amp=0.03, noise_freq=0.4, tilt=[0.15, 0, 0])

    # Step 7: Timing: Hold the heavy cup, letting it dip slightly downwards for a moment, then slowly stabilize it, showing the effort of holding the weight.
    # Dip slightly from the weight.
    current_pos = env.get_object_position("cup") # Get current cup position after lift
    env.move_to([current_pos[0], current_pos[1], current_pos[2] - 0.03], steps=100, force=700, noise_amp=0.01, noise_freq=0.2, tilt=[0.2, 0, 0])
    env.wait(50)
    # Slowly stabilize.
    env.move_to([current_pos[0], current_pos[1], current_pos[2]], steps=200, force=750, noise_amp=0.005, noise_freq=0.1, tilt=[0.15, 0, 0])
    env.wait(80)

    # Step 8: Follow Through: Perform a proud, happy, slow sway with the arm, holding the heavy cup aloft. The suction cup should tilt upwards, as if showing off its accomplishment.
    # Sway proudly to one side.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] + 0.1, cup_pos[2] + 0.45], steps=250, force=700, noise_amp=0.008, noise_freq=0.2, tilt=[-0.2, 0.1, 0])
    env.wait(50)
    # Sway proudly to the other side.
    env.move_to([cup_pos[0] + 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.45], steps=250, force=700, noise_amp=0.008, noise_freq=0.2, tilt=[-0.2, -0.1, 0])
    env.wait(50)
    # Return to a central proud position.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.5], steps=200, force=700, noise_amp=0.005, noise_freq=0.1, tilt=[-0.25, 0, 0])
    env.wait(100)