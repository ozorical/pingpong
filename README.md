# Ping Pong Game

This is a simple two-player Ping Pong game built with Python using the Pygame library. The game features smooth animations, ball physics, and score tracking.

## Features
- Two-player gameplay using keyboard controls
- Smooth ball movement with paddle collisions
- Score tracking
- Basic game reset on scoring

## Requirements
- Python 3.7 or higher
- Pygame (`pip install pygame`)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ping-pong-game.git
    cd ping-pong-game
    ```
2. Install dependencies:
    ```bash
    pip install pygame
    ```

## How to Play
1. Run the game:
    ```bash
    python main.py
    ```
2. Controls:
    - **Player 1** (Left Paddle): `W` (Up) and `S` (Down)
    - **Player 2** (Right Paddle): `Arrow Up` and `Arrow Down`
3. First to score wins the point, the ball resets, and the game continues.

## File Structure
- `main.py`: Handles the game loop and events.
- `game.py`: Controls the game logic and rendering.
- `paddle.py`: Contains paddle movement and drawing logic.
- `ball.py`: Manages ball physics and collisions.
- `settings.py`: Contains game constants like dimensions, colors, and paddle size.
