# Project Structure

- `main_gui.py`: Main execution entry point displaying the Tkinter GUI.
- `config.py`: Configuration settings, API keys, and model selections.
- `pybullet_env.py`: Simulator environment handling table, robot arm, cup instantiation.
- `planner.py`: High-level reasoning for motion plans based on prompts.
- `code_generator.py`: Generates the Python scripts that interact with PyBullet via RobotPrimitives.
- `primitives.py`: Defines the foundational robotic tasks exposed to the LLM.
- `few_shots/`: Examples utilized to instruct the language models efficiently.
- `docs/`: Core project governance documents.
- `artifacts/`: Automatically generated execution plans and verifiable outputs.
