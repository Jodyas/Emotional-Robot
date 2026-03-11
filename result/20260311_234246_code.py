def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Jerk the arm sharply and aggressively to the side, showing impatience and anger before approaching the 'heavy' task.
    # Move quickly to a point to the side of the cup, slightly higher, with an angry sideways tilt.
    env.move_to([cup_pos[0] + 0.2, cup_pos[1] - 0.2, cup_pos[2] + 0.4], steps=50, force=700, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0.5, 0])

    # Step 3: Timing: Hold still for a dramatic beat, letting the anger simmer.
    env.wait(steps=100)

    # Step 4: Slam the arm down quickly and forcefully above the cup, showing aggression and impatience.
    # Move directly to "cup" target with aggressive speed and force, and a slight forward tilt like glaring.
    env.move_to("cup", steps=60, force=800, tilt=[0.1, 0, 0])

    # Step 5: Timing: Pause briefly above the cup, a moment of angry resolve before tackling the heavy object.
    env.wait(steps=40)

    # Step 6: Drop the arm heavily onto the cup, activate suction, then lift *slowly and with great effort*, trembling violently to show the immense weight and struggle.
    # Drop heavily to grab.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=30, force=800)
    env.activate_suction()
    env.wait(10) # Brief wait for suction to engage.
    # Lift slowly with great effort, heavy trembling, and a drooping tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=500, force=800, noise_amp=0.02, noise_freq=0.3, tilt=[0.2, 0, 0])

    # Step 7: Timing: Hold the cup up, but with visible strain and continuous heavy trembling, emphasizing the weight.
    env.wait(steps=150, noise_amp=0.02, noise_freq=0.3, tilt=[0.2, 0, 0])

    # Step 8: Follow Through: Aggressively pull the cup closer, then give a frustrated, sharp shake, still angry about the effort required to lift it.
    # Aggressively pull closer.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.4], steps=100, force=700, tilt=[0, 0, 0])
    # Frustrated, sharp shake (loop for effect).
    for _ in range(2):
        env.move_to([cup_pos[0] - 0.15, cup_pos[1] + 0.05, cup_pos[2] + 0.4], steps=20, force=600, noise_amp=0.05, noise_freq=2.0, tilt=[0, 0.3, 0])
        env.move_to([cup_pos[0] - 0.15, cup_pos[1] - 0.05, cup_pos[2] + 0.4], steps=20, force=600, noise_amp=0.05, noise_freq=2.0, tilt=[0, -0.3, 0])
    # End with a final angry hold.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.4], steps=50, force=600, tilt=[0.1, 0, 0])