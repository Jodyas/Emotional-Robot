def execute(env):
    # Step 1: Detect and confirm the cup position on the table, with the suction cup slightly tilted as if peering nervously.
    cup_pos = env.get_object_position("cup")
    # Move slightly above the cup to "peer" at it, with a nervous tilt
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=150, force=150, tilt=[0.1, 0.2, 0])
    env.wait(50) # A short pause to "look"

    # Step 2: Anticipation: The arm trembles noticeably, hovering slightly, showing extreme hesitation and fear before approaching the 'slippery' object.
    # Hover slightly higher, trembling with fear, head pulled back a bit
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.35], steps=200, force=100, noise_amp=0.02, noise_freq=1.0, tilt=[-0.1, 0.3, 0])

    # Step 3: Timing: Hold still for a dramatic beat, letting the audience feel the robot's apprehension.
    env.wait(100)

    # Step 4: Move the arm slowly and with significant jitter/trembling towards the cup, as if extremely nervous about touching it.
    # The suction cup is slightly retracted, showing reluctance.
    # Move very slowly towards the cup, with high noise and a fearful tilt
    env.move_to("cup", steps=400, force=100, noise_amp=0.03, noise_freq=1.5, tilt=[0.1, 0.2, 0])

    # Step 5: Timing: Pause directly above the cup, still trembling, gathering courage for the difficult grab.
    env.wait(80)
    # Maintain trembling while waiting
    env.move_to("cup", steps=50, force=100, noise_amp=0.02, noise_freq=1.0, tilt=[0.1, 0.2, 0])

    # Step 6: Lower the arm quickly but nervously, activate suction, and lift the cup slightly.
    # Immediately, the arm jerks, simulating a brief slip as if the cup is hard to hold.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=80, force=200, noise_amp=0.01, noise_freq=0.8)
    env.activate_suction()
    env.wait(10)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=50, force=200, noise_amp=0.01, noise_freq=0.8)
    # Simulate a brief slip - a quick downward jerk
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.10], steps=20, force=300, noise_amp=0.05, noise_freq=2.0, tilt=[0.3, 0, 0]) # A sudden, sharp tilt/jerk

    # Step 7: Briefly deactivate suction for a split second, causing the cup to 'slip' down a tiny bit, then immediately re-activate suction to catch it again.
    env.deactivate_suction()
    env.wait(5) # Very short wait to allow a tiny drop
    env.activate_suction()
    env.wait(5) # Re-activate immediately

    # Step 8: Re-secure the cup with a sudden, firm suction, lifting it higher with a visible 'sigh' of relief (slight upward jerk).
    # A quick, firm upward movement with a slight "sigh" tilt
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=70, force=300, tilt=[-0.1, 0, 0]) # Upward jerk, slight relief tilt

    # Step 9: Timing: Hold the cup still for a moment after the near-slip, a beat of shock and relief.
    env.wait(100)

    # Step 10: Follow Through: Pull the cup close to the robot's 'body' while still trembling slightly,
    # holding it very carefully and protectively, as if afraid to lose it again.
    # Pull back and hold protectively, still with slight trembling
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.30], steps=200, force=150, noise_amp=0.008, noise_freq=0.7, tilt=[0.05, 0.1, 0])
    env.wait(100)