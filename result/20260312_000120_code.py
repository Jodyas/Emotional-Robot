def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Perform a happy, bouncy wave with the arm, tilting the suction cup curiously, showing excitement to interact with the cup.
    # Start from a neutral high position, then bounce down and up.
    initial_wave_pos = [cup_pos[0] - 0.2, cup_pos[1] - 0.2, cup_pos[2] + 0.5]
    env.move_to(initial_wave_pos, steps=150, force=200, tilt=[0, 0.2, 0.2]) # Initial excited position
    env.move_to([initial_wave_pos[0], initial_wave_pos[1], initial_wave_pos[2] - 0.1], steps=80, force=150, noise_amp=0.005, noise_freq=0.8, tilt=[0, 0.3, 0.1]) # Bounce down
    env.move_to([initial_wave_pos[0], initial_wave_pos[1], initial_wave_pos[2] + 0.05], steps=80, force=150, noise_amp=0.005, noise_freq=0.8, tilt=[0, 0.2, 0.2]) # Bounce up
    env.move_to([initial_wave_pos[0] + 0.1, initial_wave_pos[1], initial_wave_pos[2]], steps=100, force=150, tilt=[0, 0.25, 0]) # Sway slightly

    # Step 3: Timing: Hold the happy pose for a moment, letting the audience 'read' the emotion.
    env.wait(70)

    # Step 4: Approach the cup with a light, bouncy movement, hovering slightly above it, as if playfully assessing the 'spikes'.
    # Move to hover above the cup, with a slight bounce and curious tilt.
    hover_pos = [cup_pos[0], cup_pos[1], cup_pos[2] + 0.2]
    env.move_to(hover_pos, steps=180, force=180, noise_amp=0.003, noise_freq=0.5, tilt=[0, 0.3, 0])
    env.move_to([hover_pos[0], hover_pos[1], hover_pos[2] - 0.02], steps=50, force=100, tilt=[0, 0.3, 0]) # Small dip
    env.move_to(hover_pos, steps=50, force=100, tilt=[0, 0.3, 0]) # Back up

    # Step 5: Act Out Spiky: Gently 'poke' the side of the cup with the suction cup, then quickly retract a tiny bit, as if feeling a spike playfully.
    # Poke from one side (e.g., +X direction)
    poke_pos_1 = [cup_pos[0] + 0.08, cup_pos[1], cup_pos[2] + 0.1]
    retract_pos_1 = [cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.15]
    env.move_to(poke_pos_1, steps=70, force=150, tilt=[0, 0.4, 0]) # Poke
    env.move_to(retract_pos_1, steps=40, force=100, tilt=[0, 0.2, 0]) # Retract quickly

    # Step 6: Timing: A brief pause to emphasize the playful 'poke' and slight 'surprise'.
    env.wait(40)

    # Step 7: Act Out Spiky: Another playful 'poke' from a different angle, retracting quickly again, enjoying the 'spiky' sensation.
    # Poke from another side (e.g., +Y direction)
    poke_pos_2 = [cup_pos[0], cup_pos[1] + 0.08, cup_pos[2] + 0.1]
    retract_pos_2 = [cup_pos[0], cup_pos[1] + 0.05, cup_pos[2] + 0.15]
    env.move_to(poke_pos_2, steps=70, force=150, tilt=[0, 0.4, 0]) # Poke
    env.move_to(retract_pos_2, steps=40, force=100, tilt=[0, 0.2, 0]) # Retract quickly

    # Step 8: Timing: Another brief pause before committing to the grab.
    env.wait(40)

    # Step 9: Lower the arm, activate suction, and lift the cup with a slight, quick 'flinch' or 'jerk' upwards as if the spikes were felt, then immediately smooth into a happy, confident lift.
    # Move directly above the cup for pickup.
    env.move_to("cup", steps=100, force=200, tilt=[0, 0.1, 0])
    env.activate_suction()
    env.wait(10)
    # Quick 'flinch' upwards
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.1], steps=30, force=300, noise_amp=0.01, noise_freq=1.0, tilt=[0.1, 0.2, 0])
    # Smooth into a happy, confident lift
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=200, force=250, tilt=[-0.1, 0, 0]) # Proud lift

    # Step 10: Timing: Pause after lifting, holding the cup securely, letting the audience see it's successfully held.
    env.wait(60)

    # Step 11: Follow Through: Perform a happy little 'dance' or sway with the cup, tilting it slightly, showing joy and success despite the 'spikes'.
    # Sway left, then right, with a proud tilt.
    current_cup_height = cup_pos[2] + 0.35
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], current_cup_height], steps=120, force=180, noise_amp=0.005, noise_freq=0.5, tilt=[-0.15, 0.1, 0]) # Sway left
    env.move_to([cup_pos[0] + 0.1, cup_pos[1], current_cup_height], steps=120, force=180, noise_amp=0.005, noise_freq=0.5, tilt=[-0.15, -0.1, 0]) # Sway right
    env.move_to([cup_pos[0], cup_pos[1], current_cup_height + 0.05], steps=80, force=150, tilt=[-0.2, 0, 0]) # Little bounce up
    env.move_to([cup_pos[0], cup_pos[1], current_cup_height], steps=80, force=150, tilt=[-0.15, 0, 0]) # Settle