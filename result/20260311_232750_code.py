def execute(env):
    # Step 1: Detect and confirm the cup position on the table. The suction cup tilts slightly, as if observing with interest.
    cup_pos = env.get_object_position("cup")
    # Move to a hovering position above the cup, with a curious side-tilt
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.3], steps=200, force=150, tilt=[0, 0.3, 0])
    env.wait(50) # Hold the curious pose

    # Step 2: Anticipation: Slowly lean the arm forward, then pull back slightly, as if pondering or gathering courage to approach. The suction cup 'looks' at the cup.
    # Lean forward slightly, maintaining curious tilt
    env.move_to([cup_pos[0], cup_pos[1] + 0.05, cup_pos[2] + 0.25], steps=150, force=100, tilt=[0, 0.3, 0])
    # Pull back slightly, as if pondering
    env.move_to([cup_pos[0], cup_pos[1] - 0.02, cup_pos[2] + 0.3], steps=150, force=100, tilt=[0, 0.3, 0])

    # Step 3: Timing: Hold still for a dramatic beat, observing the cup with a curious tilt.
    env.wait(100) # Long dramatic pause

    # Step 4: Move the arm slowly and tentatively towards the cup, hovering just above it, as if inspecting it closely without touching. A slight 'poke' motion without contact.
    # Move very slowly towards the cup, maintaining curiosity
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=300, force=100, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.2, 0])
    # Slight "poke" motion without contact
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.12], steps=50, force=80, tilt=[0, 0.2, 0])
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=50, force=80, tilt=[0, 0.2, 0])

    # Step 5: Timing: Pause above the cup, 'sniffing' or examining it with a slight side-to-side wobble of the suction cup.
    # Wobble slightly side-to-side
    for _ in range(2):
        env.move_to([cup_pos[0] + 0.01, cup_pos[1], cup_pos[2] + 0.15], steps=40, force=70, tilt=[0, 0.2, 0.1])
        env.move_to([cup_pos[0] - 0.01, cup_pos[1], cup_pos[2] + 0.15], steps=40, force=70, tilt=[0, 0.2, -0.1])
    env.wait(50) # Pause after examination

    # Step 6: Lower the arm slowly, activate suction, and lift the cup gently. Immediately, a slight, sharp recoil as if surprised by the heat.
    # Lower slowly to pick up
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=200, force=100, tilt=[0, 0.1, 0])
    env.activate_suction()
    env.wait(20)
    # Lift gently
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.15], steps=100, force=150)
    # Sharp recoil as if surprised by heat (fast, short movement upwards and slightly back)
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.25], steps=40, force=300, tilt=[-0.1, 0, 0])

    # Step 7: Timing: Freeze! The moment of realization – 'Oh, it's hot!' The arm holds the cup still for a split second, then begins to tremble slightly.
    env.wait(80) # Freeze in surprise
    # Begin to tremble slightly
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.25], steps=50, force=150, noise_amp=0.01, noise_freq=0.5, tilt=[-0.1, 0, 0])
    env.wait(30)

    # Step 8: Exaggeration: Jerk the arm quickly to the side, away from the table, as if trying to get rid of the hot object.
    env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.2, cup_pos[2] + 0.4], steps=70, force=500, noise_amp=0.03, noise_freq=1.0, tilt=[0, 0.4, 0])

    # Step 9: Drop the cup suddenly and quickly due to the heat.
    env.deactivate_suction()
    env.wait(10) # Short wait for the cup to fall

    # Step 10: Timing: Moment of shock and surprise after dropping. Hold still, slightly recoiled.
    env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.2, cup_pos[2] + 0.4], steps=50, force=100, tilt=[0, 0.4, 0]) # Hold recoiled position
    env.wait(80)

    # Step 11: Follow Through: Rapidly shake the arm up and down, as if trying to cool off the 'burned' suction cup, perhaps 'blowing' on it with quick, short movements.
    # Rapidly shake arm up and down
    for _ in range(3):
        env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.2, cup_pos[2] + 0.5], steps=30, force=200, noise_amp=0.02, noise_freq=1.5, tilt=[0, 0.5, 0])
        env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.2, cup_pos[2] + 0.35], steps=30, force=200, noise_amp=0.02, noise_freq=1.5, tilt=[0, 0.5, 0])
    # Final "blowing" motion, moving slightly forward and back
    env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.25, cup_pos[2] + 0.4], steps=40, force=150, tilt=[0, 0.6, 0])
    env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.15, cup_pos[2] + 0.4], steps=40, force=150, tilt=[0, 0.6, 0])
    env.wait(50)