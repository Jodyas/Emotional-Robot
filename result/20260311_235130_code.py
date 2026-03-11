def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: The arm trembles slightly, and the suction cup (head) droops a bit, showing initial fear and hesitation.
    # Hover slightly above the cup, trembling, with a fearful droop.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=250, force=300, noise_amp=0.01, noise_freq=0.5, tilt=[0.2, 0, 0])

    # Step 3: Timing: Hold still for a dramatic beat, letting the fear sink in before approaching.
    env.wait(steps=150)

    # Step 4: Move the arm very slowly and hesitantly towards the cup, with noticeable trembling, as if dreading the task.
    # Move slowly towards the cup's hover position, maintaining tremble and droop.
    env.move_to("cup", steps=400, force=400, noise_amp=0.015, noise_freq=0.6, tilt=[0.25, 0, 0])

    # Step 5: Timing: Pause directly above the cup, bracing for the perceived heavy weight. The arm shivers slightly.
    env.wait(steps=80)
    # Add a small shiver while waiting
    env.move_to("cup", steps=30, force=200, noise_amp=0.005, noise_freq=0.8, tilt=[0.25, 0, 0])
    env.wait(steps=30)


    # Step 6: Lower the arm slowly, with a slight dip *before* activating suction to anticipate the weight.
    # Activate suction, then lift the cup *very slowly* and with significant, strained jitter.
    # The suction cup tilts downwards ('drops the head') to exaggerate the effort and fear of the weight.
    # A slight dip *after* lifting emphasizes the perceived heaviness.

    # Anticipation dip: move down slightly, then up, then down to grab
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.02], steps=100, force=500, noise_amp=0.01, noise_freq=0.5, tilt=[0.3, 0, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.08], steps=80, force=500, noise_amp=0.01, noise_freq=0.5, tilt=[0.3, 0, 0])

    # Lower to cup and activate suction (very slow, high force for perceived weight)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=300, force=800, noise_amp=0.02, noise_freq=0.4, tilt=[0.4, 0, 0])
    env.activate_suction()
    env.wait(steps=30) # Hold for a moment to "grip"

    # Lift *very slowly* with strained jitter and exaggerated droop
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=500, force=800, noise_amp=0.03, noise_freq=0.3, tilt=[0.45, 0, 0])

    # Slight dip *after* lifting to emphasize perceived heaviness
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.20], steps=100, force=800, noise_amp=0.02, noise_freq=0.3, tilt=[0.45, 0, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=200, force=800, noise_amp=0.02, noise_freq=0.3, tilt=[0.45, 0, 0])


    # Step 7: Timing: Hold the cup aloft, still trembling slightly, showing the ongoing strain and fear of dropping it.
    env.wait(steps=100)
    # Add a small tremble while holding
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=50, force=600, noise_amp=0.01, noise_freq=0.5, tilt=[0.4, 0, 0])
    env.wait(steps=50)


    # Step 8: Follow Through: Slowly pull the cup slightly closer, still trembling and with the suction cup drooping,
    # conveying lingering fear and the burden of the weight. The arm moves away from the initial pick-up spot with a slow, strained motion.
    # Move to a new position (slightly closer, higher) with continued strain and trembling.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.40], steps=400, force=700, noise_amp=0.02, noise_freq=0.4, tilt=[0.4, 0, 0])
    env.wait(steps=100) # Hold in final strained position