def execute(env):
    # Step 1: Detect and confirm the cup position on the table with a tense, focused posture.
    cup_pos = env.get_object_position("cup")
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=150, force=300, noise_amp=0.005, noise_freq=0.5, tilt=[0, 0.1, 0])

    # Step 2: Anticipation: Arm tenses, then performs a sharp, frustrated jerk to the side, showing initial anger and impatience.
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.35], steps=50, force=400, tilt=[0, 0.2, 0]) # Tense back
    env.move_to([cup_pos[0] + 0.2, cup_pos[1] + 0.1, cup_pos[2] + 0.4], steps=40, force=600, noise_amp=0.02, noise_freq=1.0, tilt=[0, -0.3, 0]) # Sharp jerk

    # Step 3: Timing: Hold the tense, slightly agitated pose for a dramatic beat, building up frustration.
    env.wait(steps=100)

    # Step 4: Angry approach: Arm lunges quickly and aggressively directly above the cup, with a slight, agitated jitter, suction cup angled down menacingly.
    env.move_to("cup", steps=70, force=700, noise_amp=0.015, noise_freq=1.2, tilt=[0, 0.2, 0])

    # Step 5: Angry grab: Slams down forcefully onto the cup, activates suction, then yanks the cup up sharply and quickly.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=30, force=800, tilt=[0, 0.1, 0]) # Slam down
    env.activate_suction()
    env.wait(10)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=50, force=700, tilt=[0, 0.1, 0]) # Yank up

    # Step 6: Timing: Freeze! A sudden, sharp pause immediately after lifting, as the robot 'realizes' the cup is burning hot. Suction cup tilts back in shock.
    env.wait(steps=40)
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=10, force=100, tilt=[-0.4, 0, 0]) # Quick tilt back in shock

    # Step 7: Recoil and drop: Arm jerks violently away from the table, flinging the cup to the side in a panicked, angry reaction to the heat.
    drop_x = cup_pos[0] + 0.4
    drop_y = cup_pos[1] + 0.4
    drop_z = cup_pos[2] + 0.3
    env.move_to([drop_x, drop_y, drop_z], steps=40, force=800, noise_amp=0.08, noise_freq=2.0, tilt=[0.2, -0.5, 0]) # Violent jerk away

    # Step 8: Release the cup with an angry, disgusted flick, as if throwing it away.
    env.deactivate_suction()
    env.wait(5)
    env.move_to([drop_x + 0.05, drop_y - 0.05, drop_z + 0.05], steps=10, force=500, tilt=[0.1, -0.6, 0]) # Flick motion

    # Step 9: Timing: A brief, stunned pause after the violent drop, a moment of lingering shock and anger.
    env.wait(steps=60)

    # Step 10: Follow Through: Arm thrashes violently side to side, shaking off the 'heat' and expressing lingering anger and frustration, perhaps ending with a frustrated slam onto the table.
    current_x = drop_x + 0.1
    current_y = drop_y - 0.1
    current_z = drop_z + 0.2
    for _ in range(3):
        env.move_to([current_x + 0.1, current_y, current_z], steps=20, force=600, noise_amp=0.07, noise_freq=2.5, tilt=[0, 0.5, 0])
        env.move_to([current_x - 0.1, current_y, current_z], steps=20, force=600, noise_amp=0.07, noise_freq=2.5, tilt=[0, -0.5, 0])
    env.move_to([current_x, current_y, cup_pos[2] + 0.05], steps=30, force=800, tilt=[0.3, 0, 0]) # Frustrated slam
    env.wait(30)