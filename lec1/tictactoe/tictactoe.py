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
    raise NotImplementedError
