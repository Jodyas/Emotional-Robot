def execute(env):
    # Step 1: Detect and confirm the cup position on the table with a cheerful, curious tilt of the suction cup.
    cup_pos = env.get_object_position("cup")
    # Hover above the cup with a curious, happy tilt (looking down slightly, but with an upward "gaze" overall)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=200, force=200, tilt=[0, 0.2, 0])
    env.wait(50) # A brief moment to "confirm"

    # Step 2: Anticipation: Perform a small, happy wiggle or bounce with the arm, showing eagerness.
    # Move slightly up, then down, then back to original hover, with a happy tilt and gentle bounce noise.
    current_pos = env.get_object_position("cup") # Get current arm position (above cup)
    env.move_to([current_pos[0], current_pos[1], current_pos[2] + 0.05], steps=80, force=150, noise_amp=0.008, noise_freq=0.8, tilt=[0, 0.25, 0]) # Small hop up
    env.move_to([current_pos[0], current_pos[1], current_pos[2] - 0.02], steps=80, force=150, noise_amp=0.008, noise_freq=0.8, tilt=[0, 0.15, 0]) # Small dip down
    env.move_to([current_pos[0], current_pos[1], current_pos[2] + 0.03], steps=80, force=150, noise_amp=0.008, noise_freq=0.8, tilt=[0, 0.2, 0]) # Back to a slightly higher hover

    # Step 3: Timing: A brief, cheerful pause before approaching the cup.
    env.wait(70)

    # Step 4: Move the arm with a light, slightly bouncy motion directly above the cup, maintaining a happy tilt.
    # Move to "cup" target, which automatically offsets to hover. Add gentle noise and happy tilt.
    env.move_to("cup", steps=250, force=180, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.2, 0])

    # Step 5: Lower the arm gently, activate suction, and lift the cup with a light, upward motion.
    # Lower to grab
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=150, force=150, tilt=[0, 0.1, 0])
    env.activate_suction()
    env.wait(30) # Short wait for suction to engage
    # Lift with a light, upward motion
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=200, force=200, tilt=[0, 0.2, 0])

    # Step 6: Act Out Object Properties: Immediately perform a quick, small, jerky movement to simulate the cup briefly slipping in the suction cup's grip.
    # Move slightly to the side, then quickly back, with a small jerk.
    current_cup_hold_pos = env.get_object_position("cup") # Get current position of the held cup
    env.move_to([current_cup_hold_pos[0] + 0.02, current_cup_hold_pos[1] + 0.01, current_cup_hold_pos[2]], steps=40, force=300, noise_amp=0.02, noise_freq=1.5, tilt=[0, 0.1, 0]) # Quick slip
    env.move_to([current_cup_hold_pos[0], current_cup_hold_pos[1], current_cup_hold_pos[2]], steps=40, force=300, noise_amp=0.01, noise_freq=1.0, tilt=[0, 0.2, 0]) # Correct back

    # Step 7: Timing: A brief pause to show the robot re-stabilizing its grip after the slip, then a happy 'aha!' moment.
    env.wait(60) # Pause to re-stabilize
    # A slight upward tilt for "aha!"
    env.move_to([current_cup_hold_pos[0], current_cup_hold_pos[1], current_cup_hold_pos[2] + 0.02], steps=50, force=150, tilt=[0, 0.3, 0])
    env.wait(30)

    # Step 8: Follow Through: Perform a happy little sway or gentle bounce with the cup, showing relief and continued happiness at having secured it.
    # Sway gently side to side with the cup
    for _ in range(2):
        env.move_to([current_cup_hold_pos[0] + 0.05, current_cup_hold_pos[1], current_cup_hold_pos[2] + 0.35], steps=100, force=180, noise_amp=0.005, noise_freq=0.7, tilt=[0, 0.25, 0.1])
        env.move_to([current_cup_hold_pos[0] - 0.05, current_cup_hold_pos[1], current_cup_hold_pos[2] + 0.35], steps=100, force=180, noise_amp=0.005, noise_freq=0.7, tilt=[0, 0.25, -0.1])
    env.move_to([current_cup_hold_pos[0], current_cup_hold_pos[1], current_cup_hold_pos[2] + 0.35], steps=100, force=180, tilt=[0, 0.2, 0]) # Return to center
    env.wait(50)