def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm flinches slightly and recoils, then slowly approaches with extreme hesitation and a slight side-to-side tremor, as if facing something scary. The suction cup tilts away slightly.
    # Flinch away
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.4], steps=100, force=200, tilt=[0.1, -0.2, 0])
    # Slowly approach with hesitation and tremor, tilting away
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] + 0.05, cup_pos[2] + 0.35], steps=300, force=150, noise_amp=0.015, noise_freq=0.8, tilt=[0.1, -0.3, 0])

    # Step 3: Timing: Hold still for a dramatic pause, letting the audience feel the fear and reluctance.
    env.wait(150)

    # Step 4: Move the arm very slowly and hesitantly above the cup, with continuous, subtle trembling. The suction cup maintains a slight 'scared' tilt.
    env.move_to("cup", steps=400, force=150, noise_amp=0.01, noise_freq=0.7, tilt=[0.1, -0.3, 0])

    # Step 5: Timing: Pause directly above the cup, gathering courage and bracing for the perceived heavy lift. A slight, nervous jitter.
    env.wait(100)
    # Add a small jitter while waiting
    env.move_to(env.get_object_position("cup"), steps=50, force=100, noise_amp=0.008, noise_freq=1.0, tilt=[0.1, -0.3, 0])

    # Step 6: Lower the arm slowly and cautiously. Activate suction. Then, lift the cup *extremely slowly* and with significant, exaggerated trembling and jitter, showing immense strain and effort, as if the cup is incredibly heavy. The arm might dip slightly before the upward movement to show bracing.
    # Dip slightly as if bracing
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=100, force=300, noise_amp=0.01, noise_freq=0.5, tilt=[0.1, -0.3, 0])
    # Lower slowly and cautiously
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=300, force=200, noise_amp=0.005, noise_freq=0.5, tilt=[0.1, -0.3, 0])
    env.activate_suction()
    env.wait(30)
    # Lift extremely slowly with exaggerated trembling and strain
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=600, force=800, noise_amp=0.03, noise_freq=0.8, tilt=[0.2, -0.4, 0])

    # Step 7: Timing: Hold the cup aloft, trembling intensely and struggling to maintain its position, emphasizing the perceived weight and the fear of dropping it.
    # Hold position with intense trembling
    env.move_to(env.get_object_position("cup"), steps=150, force=700, noise_amp=0.04, noise_freq=1.0, tilt=[0.2, -0.4, 0])
    env.wait(100) # Additional wait for dramatic effect

    # Step 8: Follow Through: Slowly, with continued exaggerated trembling and visible strain, move the cup to a slightly different, 'safer' position on the table, as if trying to get rid of the heavy burden.
    side_safe_position = [cup_pos[0] + 0.25, cup_pos[1] + 0.25, cup_pos[2] + 0.3]
    env.move_to(side_safe_position, steps=500, force=750, noise_amp=0.025, noise_freq=0.9, tilt=[0.1, -0.3, 0])

    # Step 9: Carefully and slowly release the cup, as if relieved to be rid of the weight.
    env.move_to([side_safe_position[0], side_safe_position[1], side_safe_position[2] - 0.25], steps=200, force=300, noise_amp=0.005, noise_freq=0.5, tilt=[0.1, -0.2, 0])
    env.deactivate_suction()
    env.wait(50) # Pause after release, a moment of relief

    # Step 10: Follow Through: The arm slowly droops, performing a final, exhausted shudder, then slowly pulls back, showing relief and lingering exhaustion from the ordeal of lifting the 'heavy' and 'scary' cup.
    # Arm slowly droops with an exhausted shudder
    env.move_to([side_safe_position[0] - 0.05, side_safe_position[1] - 0.05, side_safe_position[2] - 0.3], steps=250, force=150, noise_amp=0.01, noise_freq=0.3, tilt=[0.3, 0, 0])
    # Slowly pulls back to a resting position
    env.move_to([side_safe_position[0] - 0.3, side_safe_position[1] - 0.3, side_safe_position[2] + 0.1], steps=300, force=100, tilt=[0, 0, 0])
    env.wait(100)