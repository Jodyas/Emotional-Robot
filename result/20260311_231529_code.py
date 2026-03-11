def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup slightly to the side, observing the cup with a curious wobble.
    # Move to a hovering position above the cup, with a curious side-tilt and gentle wobble.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=200, force=150, noise_amp=0.01, noise_freq=0.5, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold still, letting the audience perceive the robot's curiosity.
    env.wait(steps=100)

    # Step 4: Approach the cup slowly and deliberately, hovering slightly above it, as if examining it from different angles.
    # Move very slowly towards the cup, maintaining the curious tilt and a very subtle tremor.
    env.move_to("cup", steps=350, force=120, noise_amp=0.005, noise_freq=0.8, tilt=[0, 0.25, 0])

    # Step 5: Timing: Pause directly above the cup, observing it intently before attempting to pick it up.
    env.wait(steps=80)

    # Step 6: Descend slowly, activate suction, and begin to lift the cup, but with a slight hesitation, as if testing its grip.
    # Descend slowly to just above the cup.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=250, force=100, noise_amp=0.005, noise_freq=0.8, tilt=[0, 0.1, 0])
    env.activate_suction()
    env.wait(steps=30) # Short wait to simulate testing grip
    # Begin to lift slightly, still with a hint of hesitation.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=150, force=150, noise_amp=0.008, noise_freq=1.0, tilt=[0, 0.1, 0])

    # Step 7: Exaggeration: A quick, small, jerky movement downwards and slightly to the side, simulating the cup slipping a bit from the suction cup's grip while still attached.
    # Jerk downwards and to the side quickly.
    env.move_to([cup_pos[0] + 0.04, cup_pos[1] + 0.04, cup_pos[2] + 0.08], steps=60, force=300, noise_amp=0.03, noise_freq=1.5, tilt=[0.1, 0.2, 0])

    # Step 8: Immediately re-center the arm and lift the cup with a slight upward jerk, securing the grip more firmly, but still with a subtle, continuous jitter to show it's slippery.
    # Re-center and lift with a quick, firm movement, maintaining a subtle jitter.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=100, force=250, noise_amp=0.015, noise_freq=1.0, tilt=[0, 0.15, 0])

    # Step 9: Timing: Pause after re-securing, holding the cup with a slight, nervous tremor to emphasize its slippery nature.
    env.wait(steps=70)

    # Step 10: Follow Through: Hold the slippery cup with a continuous, subtle jitter, and tilt the suction cup slightly again, as if still curiously assessing the challenging object.
    # Move slightly to the side while holding, maintaining jitter and curious tilt.
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.30], steps=150, force=150, noise_amp=0.015, noise_freq=1.0, tilt=[0, 0.25, 0])
    env.wait(steps=100)