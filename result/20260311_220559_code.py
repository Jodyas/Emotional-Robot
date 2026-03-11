def execute(env):
    # Step 1: Detect and confirm the cup's position on the table with a direct scan.
    cup_pos = env.get_object_position("cup")

    # Step 2: A brief, neutral pause to signal readiness before initiating movement.
    env.wait(steps=70)

    # Step 3: Move the arm smoothly and directly above the cup, maintaining a steady pace.
    env.move_to("cup", steps=200, force=200)

    # Step 4: Lower the arm in a controlled manner, activate suction, and lift the cup smoothly.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=150, force=150)
    env.activate_suction()
    env.wait(steps=30)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=200, force=200)

    # Step 5: A short, neutral pause to confirm the cup is securely held.
    env.wait(steps=50)

    # Step 6: Follow Through: Move the arm to a stable, slightly raised, and centered holding position, signifying task completion.
    # Assuming a neutral holding position is slightly in front and elevated.
    env.move_to([0.0, 0.5, 0.5], steps=250, force=200)
    env.wait(steps=100)