def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup slightly to the side, as if peeking around, showing initial interest.
    # Move to a position slightly above and to the side of the cup, with a curious side-tilt.
    env.move_to([cup_pos[0] + 0.1, cup_pos[1], cup_pos[2] + 0.35], steps=250, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold the curious peek pose for a moment, observing from a distance.
    env.wait(100)

    # Step 4: Move the arm slowly and deliberately towards the cup's general vicinity, but not directly above it.
    # Keep the suction cup tilted, 'inspecting' it from a side angle.
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] + 0.05, cup_pos[2] + 0.25], steps=300, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0.1, 0.2, 0])

    # Step 5: Timing: Pause to observe the cup from this new angle, perhaps bobbing slightly up and down.
    env.wait(80)
    # Slight bob up
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] + 0.05, cup_pos[2] + 0.27], steps=50, force=100, tilt=[0.1, 0.2, 0])
    # Slight bob down
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] + 0.05, cup_pos[2] + 0.25], steps=50, force=100, tilt=[0.1, 0.2, 0])
    env.wait(50)

    # Step 6: Exaggeration: Slowly circle the cup once, maintaining a tilted 'gaze' with the suction cup, as if examining all sides.
    # Define points for a slow circle around the cup
    hover_height = cup_pos[2] + 0.25
    circle_radius = 0.08
    env.move_to([cup_pos[0] + circle_radius, cup_pos[1], hover_height], steps=200, force=150, tilt=[0.1, 0.2, 0])
    env.move_to([cup_pos[0], cup_pos[1] + circle_radius, hover_height], steps=200, force=150, tilt=[0.1, 0.2, 0])
    env.move_to([cup_pos[0] - circle_radius, cup_pos[1], hover_height], steps=200, force=150, tilt=[0.1, 0.2, 0])
    env.move_to([cup_pos[0], cup_pos[1] - circle_radius, hover_height], steps=200, force=150, tilt=[0.1, 0.2, 0])
    # End circle directly above the cup
    env.move_to("cup", steps=200, force=150, tilt=[0.1, 0.2, 0])

    # Step 7: Timing: Pause again, directly above the cup now, but still with a slight tilt, pondering before the grab.
    env.wait(100)

    # Step 8: Lower the arm gently, activate suction, and lift the cup slowly, as if feeling its weight or texture with interest.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=250, force=100, tilt=[0.1, 0.2, 0])
    env.activate_suction()
    env.wait(30)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=300, force=150, tilt=[0.1, 0.2, 0])

    # Step 9: Timing: Hold the cup up, pausing to 'examine' it closely after lifting.
    env.wait(120)

    # Step 10: Follow Through: Bring the cup closer to the robot's 'body', tilting and rotating it slowly, as if scrutinizing it with deep curiosity.
    # Move closer to the robot's "body"
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=250, force=150, tilt=[0.1, 0.2, 0])
    env.wait(50)
    # Rotate slightly to examine
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=150, force=100, tilt=[0.1, -0.2, 0])
    env.wait(50)
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=150, force=100, tilt=[0.1, 0.2, 0])
    env.wait(50)