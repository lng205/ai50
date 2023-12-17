"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    steps = 0
    for row in board:
        for cell in row:
            if cell:
                steps += 1

    # X first
    if steps % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acts.add((i,j))
    return acts


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board = deepcopy(board)
    board[action[0]][action[1]] = player(board)
    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = []
    for row in board:
        lines.append(row)

    # Get columns
    for i in range(3):
        lines.append([row[i] for row in board])

    # Get Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line == [X, X, X]:
            return X
        elif line == [O, O, O]:
            return O
    # No Match
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in board:
        for cell in row:
            if not cell:
                return False        
    # Board is full
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    score = {X:1, O:-1, None: 0}
    return score[winner(board)]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def best(board, alpha, beta):
        """
        Recursively find the best score that can be achieved from the given board state.

        This function is a helper for the minimax algorithm. It applies alpha-beta pruning to improve efficiency.

        Parameters:
        board (list of list of str): The current state of the game board.
        alpha (float): The best score that the maximizer can guarantee at current or higher levels.
        beta (float): The best score that the minimizer can guarantee at current or higher levels.

        Returns:
        int: The best score that can be achieved from the given board state.
        """ 

        if terminal(board):
            return utility(board)
        player_is_X = player(board) == X
        best_score = -math.inf if player_is_X else math.inf

        for action in actions(board):
            current_score = best(result(board, action), alpha, beta)
            if player_is_X:
                best_score = max(best_score, current_score)
                alpha = max(alpha, best_score)
            else:
                best_score = min(best_score, current_score)
                beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


    alpha, beta = -math.inf, math.inf
    scores = {action: best(result(board, action), alpha, beta) for action in actions(board)}
    return max(scores, key=scores.get) if player(board) == X else min(scores, key=scores.get)