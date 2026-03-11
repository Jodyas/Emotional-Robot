def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Suction cup tilts slightly to the side, as if peering at the table, showing initial curiosity.
    # Hover slightly above the cup's general area, tilting to the side.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.4], steps=250, force=150, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold still for a brief moment, letting the audience register the curious pose.
    env.wait(70)

    # Step 4: Move the arm slowly and deliberately towards the cup's general area, with a slight side-to-side sway, as if cautiously exploring.
    # Move slightly left, then slightly right, then towards the cup.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.35], steps=200, force=120, tilt=[0, 0.2, 0])
    env.move_to([cup_pos[0] + 0.1, cup_pos[1], cup_pos[2] + 0.35], steps=200, force=120, tilt=[0, -0.2, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=300, force=150, tilt=[0, 0, 0]) # Straighten out as it gets closer

    # Step 5: Hover above the cup, tilting the suction cup left and right, as if examining it from different angles.
    # Hover directly above, then tilt left, then right.
    env.move_to("cup", steps=200, force=100, tilt=[0, 0.2, 0]) # Tilt left
    env.wait(30)
    env.move_to("cup", steps=200, force=100, tilt=[0, -0.2, 0]) # Tilt right
    env.wait(30)
    env.move_to("cup", steps=200, force=100, tilt=[0, 0, 0]) # Straighten again

    # Step 6: Timing: Hold the 'examining' pose above the cup.
    env.wait(80)

    # Step 7: Lower slightly to 'touch' the side of the cup very gently, then pull back slightly, as if testing its stability or texture.
    # Lower just above the cup's rim, then pull back up.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.02], steps=150, force=80, noise_amp=0.005, noise_freq=0.5) # Gentle touch
    env.wait(20)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.2], steps=150, force=100) # Pull back slightly

    # Step 8: Timing: Pause after the 'test', considering the next move.
    env.wait(100)

    # Step 9: Move directly above the cup, very slowly and smoothly, with a slight hesitant wobble before settling.
    env.move_to("cup", steps=400, force=120, noise_amp=0.008, noise_freq=0.8)

    # Step 10: Lower gently, activate suction, and lift the cup smoothly and carefully.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=250, force=100) # Lower gently
    env.activate_suction()
    env.wait(30) # Wait for suction to engage
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=300, force=150) # Lift smoothly

    # Step 11: Timing: Pause after lifting, holding the cup, allowing the audience to see it's secured.
    env.wait(100)

    # Step 12: Follow Through: Bring the cup closer to the 'body', tilting it slowly from side to side, as if inspecting its weight and form with continued curiosity.
    # Bring closer, then gently sway with tilt.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=200, force=150)
    env.wait(30)
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=150, force=100, tilt=[0, 0.15, 0]) # Tilt one way
    env.wait(30)
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=150, force=100, tilt=[0, -0.15, 0]) # Tilt the other way
    env.wait(30)
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.35], steps=150, force=100, tilt=[0, 0, 0]) # Return to neutral