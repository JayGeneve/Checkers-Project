# 🕹️ Jay's Checkers Game

Welcome to **Jay's Checkers**, a complete 2-player checkers game built in Python with Pygame. This project showcases object-oriented programming, interactive graphics, and classic board game logic. It’s perfect for anyone interested in learning game development fundamentals or enhancing their Python skills with a fun project.



---

## 🧠 Project Overview

**Jay's Checkers** simulates a classic game of American checkers (also known as draughts) on an 8x8 board. Each player takes turns moving red and white pieces diagonally across the board, capturing opponent pieces, and promoting their own to kings.

The game demonstrates:
- Use of **Pygame** for rendering and game loop control.
- **OOP design** with classes for pieces, the board, and the game controller.
- Visual feedback with move highlights and king indicators.
- Encapsulated movement, jump, and capture logic.
- Turn-based interaction and win-state detection.

---

## 📁 Project Structure

checkers/
├── assets/
│ └── king.png # Image displayed on a piece when it becomes a king
├── board.py # Handles board setup, drawing squares/pieces, movement
├── constants.py # Global settings like colors, screen dimensions, and image loading
├── game.py # Manages game state, player turns, input logic
├── piece.py # Defines how each checker piece behaves
├── main.py # Entry point – runs the game loop and initializes components
└── README.md # Project documentation

markdown
Copy
Edit

---

## 🖥️ Game Features

### ✅ Core Mechanics
- **8x8 Checkerboard Grid**: Alternating red and black squares using `pygame.draw.rect`.
- **Piece Initialization**: Pieces are placed automatically at the beginning in standard formation.
- **Piece Movement**: Supports diagonal movement and capture rules.
- **King Promotion**: Automatically promotes pieces to king upon reaching the opposite end of the board.
- **Capture Mechanism**: Supports single and multiple jumps, including recursive jumps.

### 🧩 Visual Elements
- **Highlighted Moves**: Blue circles indicate valid move locations for a selected piece.
- **Crown Icon**: A `king.png` asset is rendered above crowned pieces.
- **Turn Display**: Internally managed turn-based play, switching between RED and WHITE.

### 🏁 Win Detection
When one player has no remaining pieces, a win message is triggered in the console and the game ends.

---

## 🧑‍💻 Installation & Running the Game

### 🔧 Prerequisites
- Python 3.8+
- `pygame` module

To install Pygame:
```bash
pip install pygame
▶️ Run Instructions
Clone the repository or download the source files:

bash
Copy
Edit
git clone https://github.com/yourusername/jays-checkers.git
cd jays-checkers
Ensure your assets/king.png file exists (used for king piece display).

Launch the game:

bash
Copy
Edit
python main.py
🕹️ Controls
Action	Input Method
Select a Piece	Left Click
Move a Piece	Left Click on a highlighted square
Exit the Game	Close the window (X)

🧱 Code Highlights
main.py
This is the game loop manager. It handles rendering, input collection, and manages frames per second:

python
Copy
Edit
while run:
    clock.tick(FPS)
    if game.winner() is not None:
        print(game.winner())
    ...
    game.update()
board.py
Handles drawing the board, tracking pieces, and computing valid moves:

python
Copy
Edit
def get_valid_moves(self, piece):
    ...
    if piece.color == RED or piece.king:
        moves.update(self._traverse_left(...))
game.py
Acts as the game manager, calling movement and win conditions:

python
Copy
Edit
def _move(self, row, col):
    if self.selected and ...:
        self.board.move(self.selected, row, col)
