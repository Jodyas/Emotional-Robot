def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Arm trembles slightly, suction cup tilts away from the cup, showing initial apprehension.
    # Hover slightly above and to the side of the cup, with a slight tremble and tilting away.
    env.move_to([cup_pos[0] + 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.3], steps=250, force=200, noise_amp=0.015, noise_freq=0.6, tilt=[0.1, 0.3, 0])

    # Step 3: Timing: Hold still for a dramatic pause, letting the fear sink in before approaching.
    env.wait(100)

    # Step 4: Approach the cup very slowly, with significant trembling and hesitation, as if reluctant and bracing for the weight. Suction cup droops slightly in fear.
    # Move directly above the cup, but very slowly and with more pronounced trembling, and a fearful droop.
    env.move_to("cup", steps=450, force=300, noise_amp=0.03, noise_freq=0.8, tilt=[0.3, 0.1, 0])

    # Step 5: Timing: Hold perfectly still above the cup, hesitating and bracing for the heavy lift.
    env.wait(80)

    # Step 6: Anticipation: Perform a slight dip downwards just before grabbing, as if bracing and gathering strength for the heavy lift.
    # Calculate a position slightly below the default "cup" hover.
    # Assuming "cup" target hovers at cup_pos[2] + 0.15, a dip would be cup_pos[2] + 0.10.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.10], steps=300, force=400, noise_amp=0.02, noise_freq=0.7, tilt=[0.3, 0.1, 0])

    # Step 7: Lower slowly, activate suction, then lift the cup *extremely slowly* with maximum jitter and trembling, showing immense strain and struggle against the perceived weight.
    # Lower to grab.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=200, force=500, noise_amp=0.04, noise_freq=0.9, tilt=[0.3, 0.1, 0])
    env.activate_suction()
    env.wait(30) # Short wait to ensure suction, still trembling.
    # Lift extremely slowly with maximum jitter and high force for perceived weight.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=700, force=800, noise_amp=0.06, noise_freq=1.2, tilt=[0.3, 0.1, 0])

    # Step 8: Timing: Hold the cup up, trembling violently, emphasizing the effort and the fear of dropping it.
    env.wait(150) # Long wait, holding position, with implicit trembling from previous move_to's noise.

    # Step 9: Follow Through: Pull the cup slightly closer to the robot's body, still trembling and holding it with visible strain, as if struggling to maintain control. The suction cup remains slightly drooped in fear.
    # Move slightly closer to the robot's base, maintaining the fearful droop and trembling.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.45], steps=350, force=750, noise_amp=0.05, noise_freq=1.0, tilt=[0.3, 0.1, 0])
    env.wait(50) # Hold the final strained position.