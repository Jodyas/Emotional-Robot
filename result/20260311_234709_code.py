def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup slightly to the side, looking 'curious', and make a small, hesitant exploratory movement towards the cup's general direction.
    # Move slightly away from the cup, with a curious side-tilt and a gentle tremble.
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.35], steps=200, force=200, noise_amp=0.005, noise_freq=0.8, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold the curious pose, observing the cup before committing to a direct approach.
    env.wait(steps=100)

    # Step 4: Move the arm slowly and deliberately above the cup, maintaining a curious side-tilt of the suction cup, as if examining it.
    env.move_to("cup", steps=350, force=300, tilt=[0, 0.3, 0])

    # Step 5: Timing: Pause directly above the cup, holding the curious tilt, as if contemplating its weight or nature.
    env.wait(steps=150)

    # Step 6: Lower the arm very slowly, bracing for impact. Activate suction, then lift the cup extremely slowly with significant jitter and trembling to show immense strain from its weight. After lifting, let it momentarily 'sag' slightly before catching itself, emphasizing the sudden heaviness.
    # Lower very slowly, bracing.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=400, force=800, tilt=[0, 0.3, 0])
    env.activate_suction()
    env.wait(steps=30) # Short wait to ensure suction

    # Lift extremely slowly with strain.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=600, force=900, noise_amp=0.02, noise_freq=0.3, tilt=[0, 0.3, 0])
    
    # Momentarily 'sag' slightly before catching itself.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.20], steps=100, force=900, noise_amp=0.03, noise_freq=0.5, tilt=[0.1, 0.3, 0]) # Sag down
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.28], steps=200, force=900, noise_amp=0.02, noise_freq=0.3, tilt=[0, 0.3, 0]) # Catch and lift slightly higher

    # Step 7: Timing: Hold the cup aloft, visibly struggling against its weight, with a slight tremor.
    env.wait(steps=200)

    # Step 8: Slowly and carefully move the heavy cup to a new position, maintaining a slight tremor to continuously act out its weight. The suction cup maintains a slightly strained, curious tilt.
    # Define a target for "side_table" relative to the cup's initial position.
    side_table_target = [cup_pos[0] + 0.3, cup_pos[1] + 0.3, cup_pos[2] + 0.35]
    env.move_to(side_table_target, steps=450, force=850, noise_amp=0.015, noise_freq=0.4, tilt=[0.05, 0.25, 0])

    # Step 9: Follow Through: Gently lower the cup a tiny bit, then lift it slightly again, as if testing its weight one last time, ending with a sustained, curious and strained hold.
    # Lower a tiny bit.
    env.move_to([side_table_target[0], side_table_target[1], side_table_target[2] - 0.03], steps=150, force=800, noise_amp=0.01, noise_freq=0.3, tilt=[0.05, 0.25, 0])
    # Lift slightly again, testing weight.
    env.move_to([side_table_target[0], side_table_target[1], side_table_target[2] + 0.02], steps=200, force=850, noise_amp=0.015, noise_freq=0.4, tilt=[0.05, 0.25, 0])
    # Sustained hold.
    env.wait(steps=100)