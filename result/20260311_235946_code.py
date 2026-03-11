def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm recoils slightly, then trembles with high noise, showing initial fear and hesitation.
    # Recoil slightly back and up from the cup's general area.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.4], steps=100, force=200, noise_amp=0.03, noise_freq=1.5, tilt=[0.1, 0.2, 0])
    # Tremble in place with high noise.
    env.wait(steps=100, noise_amp=0.05, noise_freq=2.0)

    # Step 3: Timing: Hold still for a dramatic pause, letting the audience feel the robot's apprehension.
    env.wait(steps=150)

    # Step 4: Tentative approach: Move slowly and jerkily towards the general area of the cup, with the suction cup tilted away, as if trying to avoid contact.
    # Move towards a point slightly above the cup, but with a significant tilt away.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=350, force=150, noise_amp=0.015, noise_freq=0.8, tilt=[0, 0.4, 0])

    # Step 5: Exaggeration: A sudden, quick flinch *away* from the cup, as if it almost touched a spike. Jerk the arm back rapidly.
    # Flinch quickly to a point far away and up.
    env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.3, cup_pos[2] + 0.5], steps=70, force=500, noise_amp=0.08, noise_freq=2.5, tilt=[-0.2, -0.5, 0])

    # Step 6: Timing: Pause to recover from the 'flinch', holding perfectly still in shock.
    env.wait(steps=100)

    # Step 7: Cautious approach: Very slowly and hesitantly move directly above the cup, with extreme trembling and the suction cup still tilted away, showing extreme reluctance.
    # Move directly above the cup, but very slowly and with high noise, maintaining the tilt away.
    env.move_to("cup", steps=450, force=100, noise_amp=0.04, noise_freq=1.2, tilt=[0, 0.3, 0])

    # Step 8: Timing: Hold perfectly still above the cup, gathering courage before descending. A moment of dread.
    env.wait(steps=200)

    # Step 9: Lower very slowly and gingerly, activate suction, then lift the cup quickly and sharply as if relieved to have it off the table.
    # Lower very slowly.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=300, force=100, noise_amp=0.01, noise_freq=0.5)
    env.activate_suction()
    env.wait(30) # Brief pause for suction to engage
    # Lift quickly and sharply.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=80, force=400, noise_amp=0.02, noise_freq=1.0)

    # Step 10: Timing: Pause after lifting, holding the cup gingerly at arm's length.
    env.wait(steps=80)

    # Step 11: Follow Through: Hold the cup far away from the robot's 'body', trembling slightly, and quickly move it to the side as if still wary of the spikes. The suction cup droops slightly in relief/fear.
    # Move the cup to a far side position, trembling slightly.
    env.move_to([cup_pos[0] - 0.2, cup_pos[1] + 0.2, cup_pos[2] + 0.4], steps=150, force=200, noise_amp=0.01, noise_freq=0.7, tilt=[0.1, 0, 0])
    # Hold it there, with a slight droop.
    env.wait(steps=50, tilt=[0.15, 0, 0])