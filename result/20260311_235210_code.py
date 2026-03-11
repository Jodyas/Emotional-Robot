def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm trembles slightly, the suction cup tilts downwards (drooping head) showing initial apprehension and fear.
    # Hover above the cup, trembling with a fearful, drooping tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=250, force=200, noise_amp=0.01, noise_freq=0.8, tilt=[0.2, 0, 0])

    # Step 3: Timing: Hold still, letting the fear and hesitation build before approaching.
    env.wait(100)

    # Step 4: Move the arm very slowly and hesitantly towards the cup, with continuous slight trembling. The suction cup maintains a fearful, drooping tilt.
    env.move_to("cup", steps=400, force=250, noise_amp=0.008, noise_freq=0.7, tilt=[0.25, 0, 0])

    # Step 5: Timing: Pause directly above the cup, bracing for the perceived weight. A slight dip as if gathering strength, still trembling.
    # Dip slightly as if bracing, then hold.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=100, force=300, noise_amp=0.015, noise_freq=1.0, tilt=[0.3, 0, 0])
    env.wait(80)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.20], steps=50, force=300, noise_amp=0.01, noise_freq=0.8, tilt=[0.25, 0, 0])
    env.wait(50)


    # Step 6: Lower the arm slowly and with great effort, activate suction. Lift the cup extremely slowly, with exaggerated jitter and strain, as if struggling with immense weight. The suction cup droops significantly downwards, showing the 'dropped head' and the effort.
    # Lower with effort
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=350, force=600, noise_amp=0.02, noise_freq=0.5, tilt=[0.4, 0, 0])
    env.activate_suction()
    env.wait(30)
    # Lift with extreme effort and strain
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=500, force=800, noise_amp=0.03, noise_freq=0.3, tilt=[0.5, 0, 0])

    # Step 7: Timing: Hold the cup aloft, still trembling slightly, emphasizing the sustained effort of holding something so heavy.
    env.wait(150)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=50, force=700, noise_amp=0.015, noise_freq=0.6, tilt=[0.45, 0, 0]) # Slight adjustment to maintain tremor
    env.wait(50)

    # Step 8: Follow Through: Slowly bring the cup closer to the robot's body, as if resting it after the strenuous lift. The arm still shows a slight, continuous tremor, and the suction cup remains slightly drooped, conveying exhaustion and relief.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=300, force=500, noise_amp=0.008, noise_freq=0.7, tilt=[0.3, 0, 0])
    env.wait(100)