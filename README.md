# Tic-Tac-Toe AI with Minimax Algorithm

## Overview
This project implements an AI player for the game of Tic-Tac-Toe using the Minimax algorithm. The AI makes optimal moves, ensuring that it never loses a game (at worst, it will draw).

## Project Structure
- `tictactoe.py`: Contains the game logic and AI implementation
- `runner.py`: Provides the graphical interface (provided by CS50)
- `requirements.txt`: Lists project dependencies

## Requirements
- Python 3.12
- pygame (install using `pip3 install -r requirements.txt`)

## Installation
1. Clone or download this repository
2. Navigate to the project directory
3. Install required packages:
```bash
pip3 install -r requirements.txt
```

## Running the Game
To play against the AI:
```bash
python runner.py
```

## Game Rules
- The game is played on a 3x3 grid
- Players take turns placing their marks (X or O)
- First player uses X, second player (AI) uses O
- The first player to get 3 of their marks in a row (horizontally, vertically, or diagonally) wins
- If the grid is full and no player has won, the game is a draw

## Implementation Details
The AI uses the Minimax algorithm to:
- Explore all possible game states
- Choose moves that maximize its chances of winning
- Prevent the opponent from winning
- Force a draw when it cannot win

## File Descriptions
- `tictactoe.py`: Contains all game logic and AI implementation including:
  - Board state management
  - Player turn tracking
  - Move validation
  - Win condition checking
  - Minimax algorithm implementation
- `runner.py`: Handles the game's graphical interface and user interactions

## Author
Created by: zuzukobaladze
Last Updated: 2025-03-12
