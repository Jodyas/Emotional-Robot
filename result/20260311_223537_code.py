def execute(env):
    # Step 1: Detect and confirm the cup position on the table with an aggressive, focused tilt of the suction cup.
    cup_pos = env.get_object_position("cup")
    # Move slightly above the cup, with a strong downward/forward tilt to "look" aggressively.
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.25], steps=70, force=400, tilt=[0.3, 0.2, 0])
    env.wait(20) # A brief pause to "confirm"

    # Step 2: Anticipation: Jerk the arm aggressively and rapidly, shaking back and forth to show intense impatience and anger.
    # Jerk back slightly
    env.move_to([cup_pos[0] - 0.05, cup_pos[1], cup_pos[2] + 0.35], steps=30, force=500, noise_amp=0.05, noise_freq=1.5, tilt=[0.1, 0.4, 0])
    # Jerk forward aggressively
    env.move_to([cup_pos[0] + 0.05, cup_pos[1], cup_pos[2] + 0.30], steps=30, force=500, noise_amp=0.05, noise_freq=1.5, tilt=[0.1, -0.4, 0])
    # A final, more pronounced jerk back
    env.move_to([cup_pos[0] - 0.1, cup_pos[1], cup_pos[2] + 0.40], steps=40, force=600, noise_amp=0.08, noise_freq=2.0, tilt=[0.2, 0.5, 0])

    # Step 3: Timing: Hold still for a brief, tense moment, letting the anger build before the attack.
    env.wait(steps=70)

    # Step 4: Rush the arm directly above the cup with a fast, forceful, and slightly jerky movement, almost slamming into position.
    env.move_to("cup", steps=50, force=700, noise_amp=0.02, noise_freq=1.0, tilt=[0, 0, 0])

    # Step 5: Slam the arm down forcefully onto the cup, activate suction with an audible 'thwack', and yank the cup up quickly and aggressively.
    # Slam down
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.05], steps=25, force=800)
    # Activate suction
    env.activate_suction()
    env.wait(10) # Short wait for "thwack"
    # Yank up quickly and aggressively
    env.move_to([cup_pos[0], cup_pos[1], cup_pos[2] + 0.45], steps=40, force=750, noise_amp=0.03, noise_freq=1.5)

    # Step 6: Timing: Freeze! Hold the cup perfectly still for a dramatic beat – the moment of realization: 'Ouch! It's burning hot!'
    env.wait(steps=80)

    # Step 7: Exaggeration: Jerk the arm away violently and quickly to the side, as if recoiling from the heat in disgust and pain.
    # Jerk away to the side, with a strong tilt of disgust/pain
    env.move_to([cup_pos[0] + 0.25, cup_pos[1] + 0.35, cup_pos[2] + 0.30], steps=40, force=700, noise_amp=0.07, noise_freq=2.0, tilt=[-0.4, 0.6, 0])

    # Step 8: Release the cup abruptly and forcefully, letting it drop with a clatter. The suction cup recoils sharply.
    env.deactivate_suction()
    env.wait(10) # Short wait for the drop
    # Recoil sharply upwards and slightly back
    env.move_to([cup_pos[0] + 0.20, cup_pos[1] + 0.30, cup_pos[2] + 0.50], steps=20, force=600, tilt=[-0.2, 0.4, 0])

    # Step 9: Timing: A brief moment of shock and lingering pain after dropping the hot object. Hold still, slightly hunched.
    env.wait(steps=60)
    # Slight adjustment to a "hunched" posture
    env.move_to([cup_pos[0] + 0.15, cup_pos[1] + 0.25, cup_pos[2] + 0.45], steps=30, force=300, tilt=[0.3, 0.1, 0])
    env.wait(30)

    # Step 10: Follow Through: Violently shake the arm side to side, retracting it quickly, as if trying to shake off the pain from the burn, or expressing lingering anger at the hot cup.
    # Violent shaking and retraction
    for _ in range(3):
        env.move_to([cup_pos[0] + 0.4, cup_pos[1] + 0.4, cup_pos[2] + 0.7], steps=20, force=500, noise_amp=0.1, noise_freq=2.5, tilt=[0, 0.7, 0])
        env.move_to([cup_pos[0] + 0.3, cup_pos[1] + 0.5, cup_pos[2] + 0.6], steps=20, force=500, noise_amp=0.1, noise_freq=2.5, tilt=[0, -0.7, 0])
    # Final retraction to a "resting but still angry" position
    env.move_to([cup_pos[0] + 0.5, cup_pos[1] + 0.6, cup_pos[2] + 0.8], steps=50, force=400, tilt=[-0.1, 0.3, 0])
    env.wait(50)