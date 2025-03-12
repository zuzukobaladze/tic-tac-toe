# Tic-Tac-Toe Solution

This solution implements a Tic-Tac-Toe game in Python. The code provides functions to initialize the game board, determine the current player, identify possible actions, calculate the result of an action, check for a winner, determine if the game is over, evaluate the utility of a board state, and implement the minimax algorithm for optimal play.

## Functions

### `initial_state()`

Returns the starting state of the board as a 3x3 matrix filled with `EMPTY` values.

### `player(board)`

Determines which player has the next turn on the given board. Returns `X` if it's X's turn, and `O` if it's O's turn.

### `actions(board)`

Returns a set of all possible actions (i.e., empty cells) on the board.

### `result(board, action)`

Returns a deep copy of the board with the given action applied. Raises a `ValueError` if the action is invalid.

### `winner(board)`

Checks the board for a winner. Returns `X` if X has won, `O` if O has won, and `None` if there is no winner yet.

### `terminal(board)`

Returns `True` if the game is over (either because a player has won or the board is full), and `False` otherwise.

### `utility(board)`

Returns the utility of the board: `1` if X has won, `-1` if O has won, and `0` otherwise.

### `minimax(board)`

Implements the minimax algorithm to return the optimal action for the current player. Returns `None` if the game is over.

### `max_value_function(board)`

Helper function for the minimax algorithm to find the maximum utility value for X.

### `min_value_function(board)`

Helper function for the minimax algorithm to find the minimum utility value for O.

## Minimax Algorithm

The minimax algorithm is used to determine the optimal move for the current player. It recursively evaluates the possible future states of the board to choose the move that maximizes (for X) or minimizes (for O) the utility value.

- **Maximizing Player (X)**: Chooses the move with the highest minimum utility value.
- **Minimizing Player (O)**: Chooses the move with the lowest maximum utility value.

The algorithm uses two helper functions, `max_value_function` and `min_value_function`, to recursively evaluate the game tree and determine the optimal move.

## Example Usage

Here is an example of how to use the functions in this solution:

```python
# Initialize the board
board = initial_state()

# Get the current player
current_player = player(board)

# Get the set of possible actions
possible_actions = actions(board)

# Apply an action and get the resulting board
new_board = result(board, (0, 0))

# Check if the game is over
is_terminal = terminal(board)

# Get the utility of the board
board_utility = utility(board)

# Get the optimal action using minimax
optimal_action = minimax(board)
```

This solution provides a complete implementation of the Tic-Tac-Toe game with functions for game logic and an AI opponent using the minimax algorithm.
