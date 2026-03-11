def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm recoils slightly, then trembles violently, as if startled and fearful of the spiky cup.
    # Recoil slightly back and up, with a sharp, fearful tilt and violent trembling.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.4], steps=100, force=250, noise_amp=0.05, noise_freq=1.5, tilt=[0.1, 0.3, 0])

    # Step 3: Timing: Hold still, trembling slightly, contemplating the spiky object with dread.
    # Hold position, maintaining trembling and a cringing tilt.
    env.wait(steps=150, noise_amp=0.03, noise_freq=1.0, tilt=[0.1, 0.2, 0])

    # Step 4: Approach the cup very slowly and gingerly, with high noise (trembling) and slight jerky movements,
    # as if trying to avoid touching spikes. The suction cup tilts away slightly.
    # Move towards the cup very slowly, with continuous trembling and the end-effector "cringing" away.
    env.move_to("cup", steps=400, force=150, noise_amp=0.02, noise_freq=0.8, tilt=[0.2, -0.2, 0])

    # Step 5: Timing: Hover above the cup, making small, hesitant jerks away and back, as if afraid to commit to touching it.
    # The suction cup 'flinches'.
    # Perform small, hesitant movements around the hover position, with increased flinching.
    env.move_to([cup_pos[0] + 0.02, cup_pos[1], cup_pos[2] + 0.25], steps=50, force=100, noise_amp=0.01, noise_freq=0.5, tilt=[0.3, -0.3, 0]) # Flinch away
    env.move_to([cup_pos[0] - 0.01, cup_pos[1], cup_pos[2] + 0.25], steps=50, force=100, noise_amp=0.01, noise_freq=0.5, tilt=[0.2, -0.2, 0]) # Hesitantly back
    env.wait(steps=80, noise_amp=0.01, noise_freq=0.5, tilt=[0.2, -0.2, 0]) # Hold hover with trembling

    # Step 6: Lower the arm extremely slowly and carefully, activate suction, then lift the cup very gently and slowly,
    # as if it might prick the arm at any moment.
    # Lower extremely slowly and gently, maintaining trembling and a fearful tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=500, force=80, noise_amp=0.008, noise_freq=0.4, tilt=[0.2, -0.2, 0])
    env.activate_suction()
    env.wait(steps=30) # Brief pause to ensure suction
    # Lift very gently and slowly, still trembling.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=400, force=100, noise_amp=0.01, noise_freq=0.6, tilt=[0.2, -0.2, 0])

    # Step 7: Timing: Pause after lifting, holding the cup gingerly, a moment of fearful relief mixed with continued apprehension.
    # Hold the cup gingerly, maintaining trembling and apprehension.
    env.wait(steps=100, noise_amp=0.01, noise_freq=0.6, tilt=[0.2, -0.2, 0])

    # Step 8: Follow Through: Quickly pull the cup away from the robot's 'body', holding it far out and continuing to tremble,
    # showing sustained fear of the spiky object.
    # Rapidly pull the cup far away, with strong trembling and a pronounced "cringing" tilt.
    env.move_to([cup_pos[0] - 0.3, cup_pos[1] + 0.3, cup_pos[2] + 0.5], steps=250, force=200, noise_amp=0.03, noise_freq=1.2, tilt=[0.3, -0.4, 0])
    env.wait(steps=50, noise_amp=0.03, noise_freq=1.2, tilt=[0.3, -0.4, 0]) # Hold the fearful position