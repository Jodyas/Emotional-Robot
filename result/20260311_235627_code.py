def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Aggressively jab the arm towards the cup, then sharply recoil, showing anger and wariness of the 'spikes'.
    # Jab towards the cup (fast, forceful, angry tilt)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=50, force=700, tilt=[0, 0.3, 0])
    # Sharply recoil (fast, forceful, jerking away with angry tilt)
    env.move_to([cup_pos[0] - 0.2, cup_pos[1], cup_pos[2] + 0.4], steps=60, force=600, tilt=[0, -0.4, 0], noise_amp=0.03, noise_freq=1.0)

    # Step 3: Timing: Hold still for a dramatic beat, letting the audience feel the tension before the angry approach.
    env.wait(80)

    # Step 4: Move the arm quickly and forcefully above the cup, with a slight, angry jitter, as if bracing for contact with the 'spikes'.
    env.move_to("cup", steps=70, force=650, noise_amp=0.02, noise_freq=1.5, tilt=[0.1, 0.2, 0])

    # Step 5: Slam the arm down fast, activate suction, and thrust the cup up with a sharp, quick jerk, minimizing 'spiky' contact.
    # Slam down
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=30, force=800, tilt=[0.1, 0.2, 0])
    env.activate_suction()
    env.wait(10) # Brief wait for suction to engage
    # Thrust up with a sharp jerk
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=40, force=750, noise_amp=0.04, noise_freq=2.0, tilt=[-0.1, 0.1, 0])

    # Step 6: Timing: A brief, tense pause after lifting, holding the 'spiky' cup with a slight tremor.
    env.wait(50)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=10, force=200, noise_amp=0.01, noise_freq=0.5, tilt=[-0.1, 0.1, 0]) # Maintain position with tremor

    # Step 7: Follow Through: Angrily shake the cup off to the side, as if trying to dislodge the 'spikes' or get rid of the annoying object.
    # Move to a side position with an angry, disgusted shake
    for _ in range(3): # Shake back and forth a few times
        env.move_to([cup_pos[0] + 0.2, cup_pos[1] + 0.1, cup_pos[2] + 0.5], steps=30, force=600, noise_amp=0.08, noise_freq=2.5, tilt=[0, 0.5, 0])
        env.move_to([cup_pos[0] - 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.4], steps=30, force=600, noise_amp=0.08, noise_freq=2.5, tilt=[0, -0.5, 0])
    # End with a final angry position
    env.move_to([cup_pos[0] + 0.3, cup_pos[1], cup_pos[2] + 0.5], steps=50, force=500, tilt=[0, 0.3, 0])