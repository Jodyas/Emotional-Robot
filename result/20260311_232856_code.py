def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm flinches back slightly and begins to tremble, showing initial fear and reluctance to approach.
    # Flinch back and up, with a slight tremble and a "cowering" tilt.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.35], steps=100, force=250, noise_amp=0.01, noise_freq=0.8, tilt=[0.1, 0.2, 0])

    # Step 3: Timing: Hold still for a dramatic beat, letting the fear build before moving.
    env.wait(100)

    # Step 4: Move the arm very slowly and hesitantly towards the cup, trembling noticeably. The suction cup tilts away slightly, as if reluctant.
    # Move towards the cup's hover position, very slowly (high steps), with significant trembling (noise), and tilting away (tilt).
    env.move_to("cup", steps=400, force=150, noise_amp=0.02, noise_freq=1.2, tilt=[0.2, -0.3, 0])

    # Step 5: Timing: Pause directly above the cup, trembling intensely, as if gathering courage for the dreaded touch.
    # Apply intense trembling by moving to the current position with high noise, then wait.
    current_hover_pos = env.get_object_position("cup") # Get the actual hover position
    env.move_to([current_hover_pos[0], current_hover_pos[1], current_hover_pos[2] + 0.15], steps=1, force=100, noise_amp=0.04, noise_freq=1.8)
    env.wait(150)

    # Step 6: Quickly lower, activate suction, and immediately snatch the cup up, then flinch back sharply as if burned and startled.
    # Lower quickly to grab.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=40, force=500)
    env.activate_suction()
    env.wait(10)
    # Snatch up and flinch back sharply.
    env.move_to([cup_pos[0] - 0.2, cup_pos[1] - 0.2, cup_pos[2] + 0.4], steps=60, force=600, tilt=[-0.4, 0.4, 0])

    # Step 7: Timing: A brief, sharp pause. The moment of 'oh no, it's hot!' combined with intense fear.
    env.wait(50)

    # Step 8: Exaggeration: Jerk the arm violently away from the cup's original position, still holding it, but trying to distance it in panic.
    # Move to a distant, high point with violent shaking and a panicked tilt.
    env.move_to([cup_pos[0] + 0.5, cup_pos[1] + 0.5, cup_pos[2] + 0.6], steps=70, force=700, noise_amp=0.05, noise_freq=2.5, tilt=[0.1, 0.5, 0])

    # Step 9: Drop the cup quickly and abruptly, almost throwing it away in fear and pain.
    env.deactivate_suction()
    env.wait(10)

    # Step 10: Timing: A moment of shock and relief after dropping the 'hot' and 'scary' cup. Hold still.
    env.wait(100)

    # Step 11: Follow Through: Recoil the arm further, shaking violently and rapidly, as if still scared and trying to shake off the lingering sensation of heat or the fear. The suction cup droops and hides.
    # Recoil further with violent shaking and a "hiding" or "drooping" tilt.
    for _ in range(3):
        env.move_to([cup_pos[0] + 0.7, cup_pos[1] + 0.7, cup_pos[2] + 0.8], steps=40, force=400, noise_amp=0.08, noise_freq=3.0, tilt=[0.5, 0, 0])
        env.move_to([cup_pos[0] + 0.6, cup_pos[1] + 0.6, cup_pos[2] + 0.7], steps=40, force=400, noise_amp=0.08, noise_freq=3.0, tilt=[0.4, 0.1, 0])