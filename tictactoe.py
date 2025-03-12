import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of X's and O's
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    # X moves first, so if equal number of X's and O's, it's X's turn
    return X if x_count <= o_count else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    # Check each cell in the board
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
                
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Verify action is valid
    if action not in actions(board):
        raise ValueError("Invalid action")
    
    # Create a deep copy of the board
    result_board = copy.deepcopy(board)
    i, j = action
    
    # Place the current player's mark
    result_board[i][j] = player(board)
    
    return result_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] is not EMPTY:
            return row[0]
    
    # Check columns
    for j in range(3):
        column = [board[i][j] for i in range(3)]
        if column.count(column[0]) == 3 and column[0] is not EMPTY:
            return column[0]
    
    # Check diagonals
    diagonal1 = [board[i][i] for i in range(3)]
    if diagonal1.count(diagonal1[0]) == 3 and diagonal1[0] is not EMPTY:
        return diagonal1[0]
    
    diagonal2 = [board[i][2-i] for i in range(3)]
    if diagonal2.count(diagonal2[0]) == 3 and diagonal2[0] is not EMPTY:
        return diagonal2[0]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there's a winner
    if winner(board) is not None:
        return True
    
    # Check if board is full
    return all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # X aims to maximize the utility
        best_value = float('-inf')
        best_action = None
        
        for action in actions(board):
            min_value = min_value_function(result(board, action))
            if min_value > best_value:
                best_value = min_value
                best_action = action
    else:
        # O aims to minimize the utility
        best_value = float('inf')
        best_action = None
        
        for action in actions(board):
            max_value = max_value_function(result(board, action))
            if max_value < best_value:
                best_value = max_value
                best_action = action
                
    return best_action

def max_value_function(board):
    """
    Helper function for minimax to find maximum utility value.
    """
    if terminal(board):
        return utility(board)
    
    value = float('-inf')
    for action in actions(board):
        value = max(value, min_value_function(result(board, action)))
    return value

def min_value_function(board):
    """
    Helper function for minimax to find minimum utility value.
    """
    if terminal(board):
        return utility(board)
    
    value = float('inf')
    for action in actions(board):
        value = min(value, max_value_function(result(board, action)))
    return value