def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Slowly tilt the suction cup to the side, 'looking' at the cup with curiosity, then slowly focus on it.
    # Move to a hovering position above the cup with a curious side tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=300, force=200, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold still, observing the cup with a curious tilt, building anticipation for the interaction.
    env.wait(steps=100)

    # Step 4: Move the arm very slowly and deliberately towards the cup, hovering slightly above it, as if cautiously investigating its nature. Maintain a curious tilt.
    env.move_to("cup", steps=400, force=200, tilt=[0, 0.3, 0])

    # Step 5: Timing: Hold perfectly still above the cup, a moment of contemplation before attempting to lift, still curious.
    env.wait(steps=150)

    # Step 6: Lower the arm slowly. Activate suction. Lift the cup *very slowly* and with significant, exaggerated trembling and jitter,
    # simulating immense effort due to its perceived heaviness. There should be a slight dip before the full lift, as if struggling.
    # Lower slowly to just above the cup.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=400, force=800, tilt=[-0.2, 0, 0]) # Strained up tilt
    env.activate_suction()
    env.wait(steps=20)

    # Slight dip before lift, simulating struggle.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.03], steps=100, force=800, noise_amp=0.02, noise_freq=0.3, tilt=[-0.2, 0, 0])
    env.wait(steps=30)

    # Lift very slowly with high trembling, emphasizing heaviness.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.40], steps=500, force=800, noise_amp=0.03, noise_freq=0.5, tilt=[-0.2, 0, 0])

    # Step 7: Timing: Pause after lifting, holding the cup aloft with continued, exaggerated trembling, emphasizing the struggle with its weight.
    env.wait(steps=200) # Long pause to emphasize the struggle

    # Step 8: Follow Through: Slowly bring the heavy, trembling cup closer to the robot's 'body', still struggling slightly with the weight,
    # as if examining this surprisingly heavy object with continued curiosity. The suction cup maintains a curious tilt.
    examine_pos = [cup_pos[0] - 0.2, cup_pos[1], cup_pos[2] + 0.35] # Closer to robot's base
    env.move_to(examine_pos, steps=400, force=600, noise_amp=0.015, noise_freq=0.4, tilt=[0, 0.3, 0]) # Medium trembling, curious tilt

    # Step 9: Follow Through: End with the arm holding the cup, swaying slightly from the weight, suction cup tilted,
    # still showing curiosity about its unexpected heaviness.
    # A slight sway to emphasize the weight.
    env.move_to([examine_pos[0] + 0.02, examine_pos[1], examine_pos[2] - 0.02], steps=100, force=500, noise_amp=0.01, noise_freq=0.3, tilt=[0, 0.3, 0])
    env.move_to(examine_pos, steps=100, force=500, noise_amp=0.01, noise_freq=0.3, tilt=[0, 0.3, 0])
    env.wait(steps=100) # Hold the final curious, slightly swaying position