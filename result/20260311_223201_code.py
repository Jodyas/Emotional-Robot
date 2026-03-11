def execute(env):
    # Step 1: Detect and confirm the cup's position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup slightly to the side, hovering in place, showing initial curiosity about the cup.
    # Move slightly above the cup, with a curious side-tilt.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=100, force=150, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold the curious pose for a dramatic beat, letting the audience 'read' the expression.
    env.wait(70)

    # Step 4: Approach the cup slowly and hesitantly, with a slight wobble, maintaining the curious side-tilt of the suction cup, as if examining it.
    env.move_to("cup", steps=150, force=120, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.3, 0])

    # Step 5: Timing: Pause directly above the cup, holding perfectly still, 'inspecting' it before attempting to grab.
    env.wait(50)

    # Step 6: Lower the arm to grab the cup, activate suction. Immediately after initial suction, briefly deactivate suction for a split second to simulate a 'slip', then quickly reactivate suction and lift the cup carefully.
    # Lower to grab
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=80, force=100, tilt=[0, 0.3, 0])
    env.activate_suction()
    env.wait(10) # Initial grab

    # Simulate a 'slip'
    env.deactivate_suction()
    env.wait(5) # Brief moment of release
    env.activate_suction()
    env.wait(15) # Re-establish firm grip

    # Lift the cup carefully
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.35], steps=120, force=150, tilt=[0, 0.3, 0])

    # Step 7: Timing: A brief pause after the 'slip' and successful pickup, showing a moment of recovery and careful re-stabilization.
    env.wait(40)

    # Step 8: Follow Through: Gently lift the cup higher, holding it with a slight, continuous tremor, reinforcing its 'slippery' nature. Bring it closer to the robot's 'gaze' for a final curious inspection, maintaining the side-tilt.
    # Lift higher and closer, with a continuous tremor and curious tilt
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.45], steps=180, force=150, noise_amp=0.01, noise_freq=0.5, tilt=[0, 0.3, 0])

    # Step 9: Conclude the sequence by holding the slippery cup carefully, still with a slight curious tilt, as if pondering its unusual texture.
    env.wait(100)