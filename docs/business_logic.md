# Business Logic

## Core Workflows
1. **User Request Reception**: The user initiates a request specifying a robotic movement.
2. **Two-Stage Motion Generation**:
   - The **Planner** generates the conceptual flow and translates human goals to logical steps.
   - The **Code Generator** writes Python scripts to call primitives.
3. **Execution**: The generated code is run inside PyBullet's sandbox to visualize movements.

## Physics Constraints
- Simulated entities require proper dynamics (friction, mass, restitution) to avoid floating or unrealistic reactions when the robotic arm executes routines.
