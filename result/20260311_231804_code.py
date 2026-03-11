def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Perform a sharp, frustrated jerk of the arm, pointing the suction cup aggressively towards the cup.
    # First, move to a slightly raised, neutral position.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=100, force=200)
    # Then, a sharp, frustrated jerk back and then aggressively forward.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.45], steps=50, force=500, tilt=[0, -0.2, 0]) # Jerk back slightly
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.4], steps=60, force=600, tilt=[0, 0.5, 0]) # Aggressive point towards cup

    # Step 3: Timing: Hold still for a brief, tense pause, letting the anger build.
    env.wait(100)

    # Step 4: Lunge the arm aggressively and quickly above the cup, with high jitter, as if slamming down.
    env.move_to("cup", steps=50, force=700, noise_amp=0.05, noise_freq=2.0, tilt=[0.1, 0.3, 0])

    # Step 5: Timing: Hold perfectly still for a very short, tense moment directly above the cup, like a predator eyeing its prey.
    env.wait(40)

    # Step 6: Slam the arm down onto the cup, activate suction, then yank the cup up quickly and forcefully.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=30, force=800, tilt=[0.1, 0.3, 0]) # Slam down
    env.activate_suction()
    env.wait(10) # Brief moment of contact
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=60, force=700, tilt=[0, 0, 0]) # Yank up forcefully

    # Step 7: Timing: Hold the cup defiantly and aggressively in the air for a brief pause.
    env.wait(80)

    # Step 8: Follow Through: Perform a final aggressive shake of the arm, holding the cup defiantly, as if glaring at it.
    # Move to a slightly different position with medium noise and a slight upward tilt (defiant glare).
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] + 0.05, cup_pos[2] + 0.5], steps=80, force=500, noise_amp=0.03, noise_freq=1.0, tilt=[-0.1, 0, 0])
    env.wait(50) # Hold the defiant pose