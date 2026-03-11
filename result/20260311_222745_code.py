def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup slightly to the side, slowly approaching the cup with a 'curious' angle, observing it.
    # Move to a point slightly above and to the side of the cup, with a curious side-tilt.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1] + 0.1, cup_pos[2] + 0.35], steps=280, force=150, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold still above the cup, letting the audience 'read' the curious observation.
    env.wait(steps=80)

    # Step 4: Move the arm slowly and deliberately above the cup, maintaining the curious tilt, as if examining it before the grab.
    env.move_to("cup", steps=320, force=120, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.25, 0])

    # Step 5: Timing: Pause briefly, hovering, before attempting to pick up the potentially 'slippery' object.
    env.wait(steps=50)

    # Step 6: Lower the arm, activate suction, lift slightly, then a sudden downward jiggle with a slight noise as if the cup is slipping,
    # quickly re-securing it and lifting it up carefully. (Acting out 'slippery').
    # Lower to cup
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=150, force=100, tilt=[0, 0.1, 0])
    env.activate_suction()
    env.wait(20)
    # Lift slightly
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=80, force=100)
    # Sudden downward jiggle (slipping)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.10], steps=30, force=200, noise_amp=0.01, noise_freq=1.0, tilt=[0.05, 0, 0])
    env.wait(10)
    # Quickly re-secure and lift up carefully
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.20], steps=70, force=150, noise_amp=0.005, noise_freq=0.8, tilt=[-0.05, 0, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=200, force=120, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.1, 0])

    # Step 7: Timing: Hold the cup still after the slip, recovering and ensuring it's securely held, acknowledging the tricky grab.
    env.wait(steps=60)

    # Step 8: Slowly and cautiously lift the cup higher and move it to a safe, central position,
    # maintaining a slight tremor to show it's still perceived as slippery. (Follow Through).
    # Define a safe central position relative to the cup's initial position.
    safe_pos = [cup_pos[0], cup_pos[1] - 0.2, cup_pos[2] + 0.45]
    env.move_to(safe_pos, steps=350, force=150, noise_amp=0.008, noise_freq=0.4, tilt=[0, 0.1, 0])

    # Step 9: Follow Through: Hold the cup gently, perhaps with a slight, satisfied nod of the suction cup,
    # having successfully handled the slippery object.
    # Gentle sway and a "nod"
    env.move_to([safe_pos[0], safe_pos[1], safe_pos[2] + 0.02], steps=100, force=100, tilt=[0.1, 0, 0]) # Nod down
    env.move_to([safe_pos[0], safe_pos[1], safe_pos[2] - 0.02], steps=100, force=100, tilt=[-0.1, 0, 0]) # Nod up (satisfied)
    env.wait(steps=50)