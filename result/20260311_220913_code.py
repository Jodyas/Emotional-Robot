def execute(env):
    # Step 1: Detect and confirm the cup position on the table.
    cup_pos = env.get_object_position("cup")

    # Step 2: Anticipation: Tilt the suction cup to the side, hover slightly, and perform a slow, investigative wobble to show curiosity about the cup.
    # Hover above the cup, slightly to the side, with a curious tilt and gentle wobble.
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.35], steps=250, force=150, noise_amp=0.008, noise_freq=0.7, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold still for a dramatic beat, letting the audience 'read' the robot's curious pose.
    env.wait(80)

    # Step 4: Approach the cup slowly and cautiously, with a slight side-to-side sway, as if examining it closely. Keep the suction cup tilted curiously.
    # Move closer to the cup, maintaining the curious tilt and adding a gentle sway.
    env.move_to("cup", steps=300, force=120, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.3, 0])

    # Step 5: Timing: Pause directly above the cup, 'inspecting' it before attempting to grab.
    env.wait(60)

    # Step 6: Attempt to pick up the cup. Lower the arm, activate suction, and lift slightly. This is the initial, slightly clumsy attempt.
    # Lower to grab, then activate suction and lift a tiny bit.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=100, force=150, tilt=[0, 0.3, 0])
    env.activate_suction()
    env.wait(20)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.10], steps=80, force=150, tilt=[0, 0.3, 0])

    # Step 7: Exaggeration: Immediately after initial suction, move the arm down a tiny bit with a sudden jerk and slight jitter, simulating the cup slipping from the suction cup's grasp.
    # Simulate a slip: quick downward jerk with jitter.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.07], steps=40, force=250, noise_amp=0.02, noise_freq=1.5, tilt=[0, 0.3, 0])

    # Step 8: Briefly deactivate suction to emphasize the 'slip' and the moment of surprise.
    env.deactivate_suction()

    # Step 9: Timing: A brief moment of 'oh no!' or re-evaluation after the slip.
    env.wait(40)

    # Step 10: Re-attempt to pick up the cup, this time more carefully. Lower the arm slowly, activate suction, and lift gently with slight, careful jitters to show it's still slippery.
    # Re-attempt: move down slowly, activate suction, lift carefully with jitters.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=150, force=120, tilt=[0, 0.3, 0])
    env.activate_suction()
    env.wait(30)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=200, force=150, noise_amp=0.007, noise_freq=0.8, tilt=[0, 0.3, 0])

    # Step 11: Timing: Pause after successfully lifting, ensuring the audience sees the cup is now held, albeit carefully.
    env.wait(70)

    # Step 12: Follow Through: Bring the cup closer to the robot's 'body', holding it with continuous slight jitters to show its slippery nature. Tilt the suction cup again, as if still curiously examining the challenging object it just managed to secure.
    # Bring cup closer, maintaining jitters and curious tilt.
    env.move_to([cup_pos[0] - 0.15, cup_pos[1], cup_pos[2] + 0.30], steps=250, force=150, noise_amp=0.007, noise_freq=0.8, tilt=[0, 0.3, 0])
    env.wait(50)