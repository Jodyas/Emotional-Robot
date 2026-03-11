def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup slightly to the side, hovering above the table, as if looking at the cup with curiosity.
    # Move to a point slightly above and to the side of the cup, with a curious tilt.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.3], steps=250, force=150, tilt=[0, 0.3, 0], noise_amp=0.005, noise_freq=0.5)

    # Step 3: Timing: Hold the curious pose for a dramatic beat, allowing the audience to read the expression.
    env.wait(100)

    # Step 4: Move the arm slowly and smoothly towards the cup, circling it slightly as if investigating its form. Maintain the curious tilt.
    # Move to one side of the cup
    env.move_to([cup_pos[0] - 0.05, cup_pos[1] + 0.05, cup_pos[2] + 0.2], steps=200, force=120, tilt=[0, 0.3, 0], noise_amp=0.003, noise_freq=0.4)
    # Move to the other side
    env.move_to([cup_pos[0] + 0.05, cup_pos[1] - 0.05, cup_pos[2] + 0.2], steps=200, force=120, tilt=[0, 0.3, 0], noise_amp=0.003, noise_freq=0.4)
    # Move directly above the cup
    env.move_to("cup", steps=200, force=120, tilt=[0, 0.3, 0], noise_amp=0.003, noise_freq=0.4)

    # Step 5: Timing: Pause directly above the cup, holding perfectly still, as if examining it closely before the attempt.
    env.wait(80)

    # Step 6: Lower the arm, activate suction, and lift the cup gently. This is the initial grab.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=150, force=100, tilt=[0, 0.3, 0]) # Lower gently
    env.activate_suction()
    env.wait(30)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=100, force=100, tilt=[0, 0.3, 0]) # Lift slightly

    # Step 7: Timing: A very brief pause after lifting, just before the slip.
    env.wait(20)

    # Step 8: Act Out Object Properties: Briefly deactivate suction to simulate the cup slipping from the grasp, causing a slight drop.
    env.deactivate_suction()
    env.wait(10) # Short wait to allow it to drop a tiny bit

    # Step 9: Exaggeration: Immediately perform a quick, jerky downward movement to 'catch' the slipping cup before it falls further.
    # Move quickly down to catch it, slightly below the previous lift height.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.03], steps=50, force=300, tilt=[0, 0.3, 0])

    # Step 10: Re-activate suction quickly and firmly, securing the cup after the slip. Lift it carefully.
    env.activate_suction()
    env.wait(20)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=250, force=150, tilt=[0, 0.3, 0]) # Lift carefully to a higher position

    # Step 11: Timing: Hold the cup steady after the successful re-grab, showing relief and stabilization.
    env.wait(70)

    # Step 12: Follow Through: Slowly bring the cup closer to the 'face' (suction cup), tilting it slightly from side to side as if still curiously examining its slippery nature, holding it very carefully.
    # Bring it closer and slightly lower, with a gentle side-to-side tilt for examination.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.25], steps=200, force=120, tilt=[0, 0.2, 0], noise_amp=0.005, noise_freq=0.5)
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.25], steps=150, force=120, tilt=[0, -0.2, 0], noise_amp=0.005, noise_freq=0.5)
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.25], steps=150, force=120, tilt=[0, 0.2, 0], noise_amp=0.005, noise_freq=0.5)
    env.wait(50)