def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm tenses, hovering low with a slight, aggressive twitch.
    # The suction cup angles down sharply, like an angry scowl, preparing to strike.
    # Hover slightly above the cup, tense and ready to strike.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.1], steps=150, force=500, noise_amp=0.015, noise_freq=0.8, tilt=[0, -0.4, 0])

    # Step 3: Timing: Hold this tense, angry pose for a dramatic beat, letting the anger build before the action.
    env.wait(100)

    # Step 4: Exaggeration: Slam the arm down quickly and forcefully, stopping abruptly just above the cup
    # with high speed and a jarring stop, expressing impatience and aggression.
    # Move very fast and forcefully to just above the cup, maintaining the angry tilt.
    env.move_to("cup", steps=50, force=700, tilt=[0, -0.4, 0])
    env.wait(10) # A brief, jarring stop

    # Step 5: Lower the arm with a sharp, aggressive motion onto the cup. Activate suction.
    # Then, lift the cup very slowly and with extreme effort, showing significant trembling and jitter
    # throughout the lift, as if struggling with immense, frustrating weight. The arm might dip slightly before the upward movement.
    # Aggressively lower onto the cup.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.02], steps=30, force=800, tilt=[0, -0.4, 0])
    env.activate_suction()
    env.wait(15) # Short wait to ensure suction

    # Dip slightly before lifting, then lift very slowly with extreme effort and trembling.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] - 0.01], steps=20, force=800, tilt=[0, -0.4, 0]) # Slight dip
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=400, force=800, noise_amp=0.03, noise_freq=0.5, tilt=[0, -0.3, 0])

    # Step 6: Timing: Hold the heavy, trembling cup aloft for a moment, emphasizing the strain and the anger
    # of having to deal with its weight.
    env.wait(150)

    # Step 7: Follow Through: With a frustrated, jerky motion, the arm slowly and heavily pulls the cup slightly closer,
    # still trembling with effort and anger, then holds it rigidly, refusing to yield to its weight.
    # Pull the cup closer with a frustrated, jerky, heavy motion.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=250, force=700, noise_amp=0.025, noise_freq=0.6, tilt=[0, -0.35, 0])
    env.wait(80) # Hold rigidly