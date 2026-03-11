def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Timing: A brief, neutral pause after detection, acknowledging the information.
    env.wait(steps=50)

    # Step 3: Move the arm smoothly and directly above the cup, without hesitation or rush.
    env.move_to("cup", steps=200, force=200)

    # Step 4: Timing: A brief, neutral pause to settle the arm before initiating the pick-up.
    env.wait(steps=50)

    # Step 5: Lower the arm, activate suction, and lift the cup in a controlled, steady motion.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=150, force=200)
    env.activate_suction()
    env.wait(30)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=200, force=200)

    # Step 6: Timing: A brief, neutral pause after lifting, confirming the cup is securely held.
    env.wait(steps=50)

    # Step 7: Follow Through: Hold the cup steadily in a neutral 'present' position, then slightly adjust to a ready state, concluding the action.
    # Hold steadily (already at this position, so it's a subtle re-settle)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=100, force=200)
    # Slightly adjust to a ready state (e.g., slightly back and up)
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.35], steps=150, force=200)
    env.wait(70)