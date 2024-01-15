"""
Tic Tac Toe Player
"""

import math
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
    count_x = 0
    count_o = 0

    for row in board:
        for action in row:
            if action == X:
                count_x += 1
            if action == O:
                count_o += 1
    if count_x==count_o:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==EMPTY:
                moves.add((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)
    result_board[action[0]][action[1]] = player(result_board)
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    transposed = [[row[i] for row in board] for i in range(len(board))]
    diagonal_up = []
    diagonal_down = []

    for i, row in enumerate(board):
        if all(action == X for action in row) or all(action == X for action in transposed[i]):
            return X
        if all(action == O for action in row) or all(action == O for action in transposed[i]):
            return O

    for i, row in enumerate(board):
        diagonal_up.append(row[i])
        diagonal_down.append(row[-i-1])

    if all(action == X for action in diagonal_up) or all(action == X for action in diagonal_down):
        return X
    if all(action == O for action in diagonal_up) or all(action == O for action in diagonal_down):
        return O
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count_empty = 0

    for row in board:
        for action in row:
            if action==EMPTY:
                count_empty+=1

    if count_empty==0:
        return True

    return winner(board) is not None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    if winner(board)==O:
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_move=(EMPTY,EMPTY)
    if player(board)==X:
        score = float('-inf')
        for action in actions(board):
            value=min(result(board, action))
            if value>score:
                score=value
                best_move=action
            
    if player(board)==O:
        score = float('inf')
        for action in actions(board):
            value=max(result(board, action))
            if value<score:
                score=value
                best_move=action

    return best_move

def max(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board): 
        value = min(result(board, action))
        if v < value:
            v = value
    return v

def min(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board): 
        value = max(result(board, action))
        if v > value:
            v = value
    return v