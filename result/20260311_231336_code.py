def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup slightly to the side, hovering above the table, as if observing the cup with curiosity.
    # Move to a point slightly above and to the side of the cup, with a curious tilt.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.35], steps=250, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold still for a moment, letting the 'curious' pose register.
    env.wait(steps=80)

    # Step 4: Slowly and smoothly move the arm directly above the cup, maintaining a slight curious tilt, as if examining it closely.
    env.move_to("cup", steps=300, force=120, noise_amp=0.003, noise_freq=0.3, tilt=[0, 0.3, 0])

    # Step 5: Timing: Pause directly above the cup, a moment of final inspection before attempting to pick it up.
    env.wait(steps=100)

    # Step 6: Lower the arm, activate suction, and attempt to lift. Immediately after lifting a small distance,
    # perform a quick, small, jerky drop (simulating a slip) before re-activating suction and lifting again, showing it's slippery.
    # Move down to grab the cup (neutral tilt for precision).
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=100, force=150, tilt=[0, 0, 0])
    env.activate_suction()
    env.wait(steps=20)
    # Lift slightly
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=80, force=180, tilt=[0, 0, 0])
    env.wait(steps=10) # Brief hold before the slip

    # Simulate a slip: deactivate suction, drop slightly, then reactivate and lift.
    env.deactivate_suction()
    env.wait(steps=5) # Very brief moment of release
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.08], steps=30, force=200, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0, 0]) # Jerk down
    env.activate_suction()
    env.wait(steps=15) # Re-grab
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.20], steps=100, force=250, tilt=[0, 0, 0]) # Lift again securely

    # Step 7: Timing: A brief pause after the 'slip' and re-grab, acknowledging the difficulty of holding the slippery object.
    env.wait(steps=70)

    # Step 8: Carefully and slightly shakily lift the cup higher above the table, maintaining a very stable, slow movement to avoid another slip.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.40], steps=350, force=180, noise_amp=0.008, noise_freq=0.7, tilt=[0, 0, 0])

    # Step 9: Follow Through: Hold the slippery cup gently, with a slight, continuous, almost imperceptible wobble,
    # as if still trying to maintain a secure grip. The suction cup 'face' remains slightly tilted, as if still processing the 'slippery' experience.
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.40], steps=200, force=150, noise_amp=0.01, noise_freq=0.8, tilt=[0, 0.3, 0])
    env.wait(steps=150) # Hold the pose with wobble