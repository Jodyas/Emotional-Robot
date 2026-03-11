def execute(env):
    # Step 1: Detect and confirm the cup position on the table with an aggressive, focused tilt of the suction cup.
    cup_pos = env.get_object_position("cup")
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.30], steps=100, force=400, tilt=[0, 0.4, 0]) # Aggressive downward tilt

    # Step 2: Anticipation: A sharp, frustrated jerk of the arm, as if slamming a fist on the table, showing impatience and anger before even moving.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.10], steps=30, force=700, tilt=[0, 0.5, 0]) # Slam down
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.40], steps=30, force=700, tilt=[0, -0.5, 0]) # Jerk back up angrily

    # Step 3: Timing: Hold still for a dramatic beat after the angry jerk, letting the frustration sink in.
    env.wait(80)

    # Step 4: Move the arm quickly and forcefully towards the cup, but stop just above it, with an aggressive, downward-tilted suction cup, glaring at the object.
    env.move_to("cup", steps=100, force=600, tilt=[0, 0.3, 0]) # Move quickly, stop above, aggressive tilt

    # Step 5: Timing: Pause briefly above the cup, holding still, as if gathering the 'strength' or 'will' to deal with this heavy object.
    env.wait(50)

    # Step 6: Lower the arm very slowly and with significant, visible jitter, as if the cup's weight is already a struggle before contact. The suction cup droops slightly in frustration.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=400, force=800, noise_amp=0.02, noise_freq=0.3, tilt=[0.2, 0, 0]) # Slow, heavy, jittery descent, drooping tilt

    # Step 7: Activate suction. Then, lift the cup extremely slowly and with exaggerated, heavy trembling, struggling immensely to get it off the table. Hold it mid-air, visibly strained.
    env.activate_suction()
    env.wait(20) # Short wait for suction to engage
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.40], steps=500, force=900, noise_amp=0.03, noise_freq=0.4, tilt=[0.3, 0, 0]) # Extremely slow, heavy, trembling lift, strained tilt

    # Step 8: Timing: A long, strained pause after lifting, holding the heavy cup, trembling with effort and frustration.
    env.wait(150)

    # Step 9: Slowly and heavily move the cup a short distance to the side, as if it's a burdensome object that's difficult to maneuver. The movement is sluggish and jittery.
    side_pos = [cup_pos[0] + 0.2, cup_pos[1] + 0.1, cup_pos[2] + 0.35]
    env.move_to(side_pos, steps=450, force=850, noise_amp=0.025, noise_freq=0.35, tilt=[0.25, 0, 0]) # Sluggish, jittery move to side

    # Step 10: Follow Through: A final, angry, strained shake of the arm while still holding the cup, showing extreme frustration with its weight and the effort required.
    for _ in range(3): # Perform a few rapid, angry shakes
        env.move_to([side_pos[0] + 0.03, side_pos[1], side_pos[2] + 0.03], steps=20, force=700, noise_amp=0.05, noise_freq=1.5, tilt=[0.1, 0.1, 0])
        env.move_to([side_pos[0] - 0.03, side_pos[1], side_pos[2] - 0.03], steps=20, force=700, noise_amp=0.05, noise_freq=1.5, tilt=[-0.1, -0.1, 0])