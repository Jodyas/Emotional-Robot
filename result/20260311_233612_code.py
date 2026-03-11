def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm trembles nervously, hesitating and slightly pulling back,
    # showing fear before approaching the 'slippery' object. Suction cup tilts away nervously.
    # Move slightly back and up from the cup's general area, with nervous trembling and a fearful tilt.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.3],
                 steps=250, force=150, noise_amp=0.015, noise_freq=0.8, tilt=[0.1, 0.3, 0])

    # Step 3: Timing: Hold still for a dramatic pause, letting the audience feel the apprehension.
    env.wait(steps=100)

    # Step 4: Approach the cup slowly and with significant trembling, showing extreme caution and fear
    # due to its perceived slipperiness.
    env.move_to("cup", steps=400, force=180, noise_amp=0.025, noise_freq=1.0, tilt=[0.15, 0.2, 0])

    # Step 5: Timing: Pause directly above the cup, hesitating and trembling slightly before making contact.
    env.wait(steps=80)
    # Add a small, in-place tremble to emphasize hesitation
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.18], steps=50, noise_amp=0.01, noise_freq=0.5, tilt=[0.15, 0.2, 0])


    # Step 6: Lower the arm slowly, activate suction, and lift the cup gently, but only slightly off the table.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=300, force=150, noise_amp=0.005, noise_freq=0.5)
    env.activate_suction()
    env.wait(steps=20)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.1], steps=200, force=150, noise_amp=0.005, noise_freq=0.5)

    # Step 7: Act Out Object Properties: Immediately after the initial lift, perform a quick, jerky,
    # small side movement, as if the cup is slipping from the suction cup's grip.
    # Jerk to the side with high noise and force, as if losing grip.
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] - 0.03, cup_pos[2] + 0.08],
                 steps=40, force=400, noise_amp=0.06, noise_freq=2.0, tilt=[0.2, -0.1, 0])

    # Step 8: Act Out Object Properties: Briefly deactivate suction for a split second to simulate the cup slipping and nearly falling.
    env.deactivate_suction()
    env.wait(steps=5) # Very brief moment of release

    # Step 9: Act Out Object Properties: Immediately re-activate suction and quickly lift the cup fully and securely,
    # as if catching it just in time from falling.
    env.activate_suction()
    env.wait(steps=5) # Very brief moment to re-engage
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35],
                 steps=80, force=500, noise_amp=0.03, noise_freq=1.5, tilt=[-0.1, 0, 0]) # Quick, decisive lift

    # Step 10: Timing: A moment of shock and relief after the near-disaster.
    # Hold the cup perfectly still, but the arm itself might tremble slightly.
    env.wait(steps=120)
    # A very subtle tremble in place to show lingering shock
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=50, noise_amp=0.005, noise_freq=0.5)


    # Step 11: Follow Through: Hold the cup gingerly, trembling slightly, then quickly pull it close to the robot's 'body'
    # as if protecting it from slipping again. Suction cup droops slightly in relief/fear.
    # Pull it closer to the robot's base, with continued slight trembling and a "relieved/fearful" droop.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.30],
                 steps=200, force=200, noise_amp=0.01, noise_freq=0.7, tilt=[0.2, 0, 0])
    env.wait(steps=50) # Hold it close and safe