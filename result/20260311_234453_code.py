def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Jerk the arm sharply and aggressively, showing impatience and anger before moving.
    # First, a sharp upward jerk, then a forceful downward "ready" position.
    env.move_to([cup_pos[0] + 0.1, cup_pos[1] - 0.1, cup_pos[2] + 0.6], steps=50, force=700, tilt=[0, 0.5, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=50, force=700, tilt=[0, -0.5, 0])

    # Step 3: Timing: Hold still for a brief, tense moment, letting the anger build.
    env.wait(70)

    # Step 4: Rush the arm quickly and forcefully above the cup, almost slamming into position with an angry tilt.
    env.move_to("cup", steps=90, force=750, tilt=[0, -0.3, 0])

    # Step 5: Timing: Hold rigidly still above the cup, a tense pause before the effort of grabbing the heavy object.
    env.wait(120)

    # Step 6: Slam the arm down slightly past the cup (as if bracing for weight), then activate suction and lift slowly with visible strain and heavy jitter, struggling with the perceived weight. The suction cup droops slightly with effort.
    # Slam down slightly past the cup's Z-coordinate.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] - 0.02], steps=40, force=800, tilt=[0.1, 0, 0])
    env.activate_suction()
    env.wait(10)
    # Lift slowly with strain, heavy jitter, and a drooping tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=450, force=850, noise_amp=0.02, noise_freq=0.3, tilt=[0.2, 0, 0])

    # Step 7: Timing: Hold the cup aloft, trembling slightly from the effort and weight. A moment of strained triumph mixed with frustration.
    env.wait(180)

    # Step 8: Follow Through: Pull the heavy cup closer with a frustrated, aggressive tilt of the suction cup, holding it with a continuous, low-frequency tremble, showing lingering anger and the burden of its weight.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.4], steps=250, force=700, noise_amp=0.02, noise_freq=0.3, tilt=[0, 0.3, 0])
    env.wait(50)