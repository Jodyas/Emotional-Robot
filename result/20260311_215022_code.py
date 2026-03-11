def execute(env):
    # Step 1: Detect and confirm the cup's position on the table with a direct scan.
    cup_pos = env.get_object_position("cup")

    # Step 2: A brief, natural pause before initiating movement, allowing for clear action separation.
    env.wait(steps=50)

    # Step 3: Move the arm smoothly and directly above the cup, without hesitation or noise.
    env.move_to("cup", steps=250, force=200)

    # Step 4: Lower the arm steadily, activate suction, and lift the cup in a controlled, fluid motion.
    # Lower the arm to just above the cup
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=200, force=200)
    env.activate_suction()
    env.wait(steps=30) # Allow suction to engage
    # Lift the cup to a neutral holding height
    neutral_hold_height = cup_pos[2] + 0.35
    env.move_to([cup_pos[0], cup_pos[1], neutral_hold_height], steps=250, force=200)

    # Step 5: A short, stable pause after lifting the cup, confirming a successful pick-up.
    env.wait(steps=70)

    # Step 6: Follow Through: Hold the cup perfectly steady at a neutral height, signifying a clean and completed task.
    # Hold the current position perfectly steady
    env.wait(steps=100)