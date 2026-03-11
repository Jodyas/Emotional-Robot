def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Jerk the arm aggressively to the side, showing impatience and anger before the action.
    # Move to a point to the side of the cup, slightly above, with fast, forceful, and noisy motion.
    env.move_to([cup_pos[0] + 0.2, cup_pos[1] - 0.1, cup_pos[2] + 0.4], steps=50, force=700, noise_amp=0.05, noise_freq=1.5, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold still for a tense beat, building up to the angry approach.
    env.wait(80)

    # Step 4: Slam the arm down forcefully and directly above the cup, showing aggression and impatience.
    # First, a slight "wind-up" motion upwards, then a very fast, forceful slam.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.5], steps=50, force=600) # Wind up
    env.move_to("cup", steps=40, force=800, tilt=[0.1, 0, 0]) # Slam down, slight forward tilt

    # Step 5: Lower the arm quickly, activate suction, then lift the cup slowly and with visible strain and trembling, emphasizing its heavy weight.
    # Lower quickly to grab.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=30, force=700)
    env.activate_suction()
    env.wait(10) # Short wait for suction to engage.
    # Lift slowly with strain and trembling, using heavy object parameters.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=400, force=800, noise_amp=0.02, noise_freq=0.3, tilt=[0.2, 0, 0])

    # Step 6: Timing: Hold the cup, visibly trembling and struggling, showing the immediate effort of holding something heavy.
    # Hold current position with continued trembling.
    current_lift_pos = [cup_pos[0], cup_pos[1], cup_pos[2] + 0.3]
    env.move_to(current_lift_pos, steps=100, force=800, noise_amp=0.025, noise_freq=0.4, tilt=[0.25, 0, 0])
    env.wait(100) # Long wait to emphasize the struggle.

    # Step 7: Act Out Object Properties: The arm sags slightly downwards, struggling to maintain the lift, emphasizing the cup's heavy weight.
    # Move to a slightly lower Z coordinate, slowly, with more noise and a more pronounced drooping tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.2], steps=250, force=800, noise_amp=0.03, noise_freq=0.3, tilt=[0.3, 0, 0])
    current_sagged_pos = [cup_pos[0], cup_pos[1], cup_pos[2] + 0.2]

    # Step 8: Follow Through: Shake the arm aggressively while holding the cup, showing lingering frustration and anger at its weight and the effort required.
    # Perform a series of aggressive jerks around the current sagged position.
    for _ in range(3):
        env.move_to([current_sagged_pos[0] + 0.05, current_sagged_pos[1], current_sagged_pos[2] + 0.05], steps=30, force=600, noise_amp=0.08, noise_freq=2.0, tilt=[0, 0.4, 0])
        env.move_to([current_sagged_pos[0] - 0.05, current_sagged_pos[1], current_sagged_pos[2] - 0.05], steps=30, force=600, noise_amp=0.08, noise_freq=2.0, tilt=[0, -0.4, 0])