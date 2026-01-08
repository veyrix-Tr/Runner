# Pixel Runner

A 2D endless runner game built with Pygame featuring a pixel art aesthetic. The player controls a character that must jump over obstacles while the game speed and score increase over time.

## Core Concept

Pixel Runner is a classic side-scrolling endless runner where the player must time their jumps to avoid obstacles (snails and flies). The game features progressive difficulty with increasing score, animated sprites, and a retro pixel art style.

## Setup and Installation

### Prerequisites

- Python 3.11 or higher
- UV package manager (recommended) or pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/veyrix-Tr/Pixel-runner.git
cd Pixel-runner
```

2. Install dependencies using UV:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv add pygame
```

### Running the Game

The project includes two implementations:

#### Standard Implementation (main.py)
```bash
uv run main.py
```

#### Object-Oriented Implementation (main-class.py)
```bash
uv run main-class.py
```

Both versions offer identical gameplay but use different architectural approaches.

## Game Controls

- **Spacebar**: Jump
- **Mouse Click**: Jump (when clicking on player)
- **M Key**: Toggle background music on/off
- **Escape**: Exit game

## Game Features

- Progressive scoring system based on survival time
- Animated player character with walk and jump states
- Multiple obstacle types (ground-based snails and flying enemies)
- Background music and sound effects
- Game over screen with score display
- Restart functionality

## Implementation Details

### Standard Implementation (main.py)

The standard implementation uses a procedural approach with:
- Direct pygame surface manipulation
- Manual sprite animation and collision detection
- Event-driven game loop
- Separate functions for game mechanics

### Object-Oriented Implementation (main-class.py)

The OOP implementation utilizes pygame's sprite system:
- Player and Obstacle classes inheriting from pygame.sprite.Sprite
- Sprite groups for efficient rendering and collision detection
- Encapsulated game logic within class methods
- Cleaner separation of concerns

Both implementations share the same assets and provide identical gameplay experiences.

## Project Structure

```
pixel-runner/
├── main.py                 # Standard implementation
├── main-class.py          # Object-oriented implementation
├── graphics/              # Game assets
│   ├── Player/            # Player sprites
│   ├── snail/             # Snail obstacle sprites
│   ├── Fly/               # Flying enemy sprites
│   └── Sky.png, ground.png # Background assets
├── audio/                 # Sound files
│   ├── jump.mp3           # Jump sound effect
│   └── music.wav          # Background music
├── font/                  # Font files
│   └── Pixeltype.ttf      # Pixel font
└── README.md              # This file
```

## Development Notes

- Game runs at 60 FPS for smooth animation
- Obstacle spawn rate: every 1.5 seconds
- Player jump height and gravity tuned for responsive gameplay
- Score calculation: 1 point per 700ms survived
- Collision detection uses rectangular bounding boxes

## License

This project is open source and available under the MIT License.
