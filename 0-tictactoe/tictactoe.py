"""
Tic Tac Toe Player
"""

import copy
import math
from ast import Return
from queue import Empty
from turtle import resetscreen

X = "X"
O = "O"
EMPTY = None


class Node:
    def __init__(self, state, parent, action, utility):
        self.state = state
        self.parent = parent
        self.action = action
        self.utility = utility


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    played_turns = 0
    for list in board:
        for i in list:
            if i != EMPTY:
                played_turns += 1

    # if the number of played turns is odd it's O turn
    if played_turns & 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    actions = set()
    for i, col in enumerate(board):
        for j, row in enumerate(col):
            if row == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    resulting_board = copy.deepcopy(board)

    if resulting_board[action[0]][action[1]] == EMPTY:
        resulting_board[action[0]][action[1]] = player(board)
        return resulting_board
    else:
        raise NameError("Invalid value for board")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    # game is not over if there is any empty cell
    for row in board:
        for col in row:
            if col == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)

    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    res = []
    if terminal(board) is False:
        for action in actions(board):
            resulting_board = result(board, action)
            if terminal(resulting_board):
                res.append((action, utility(resulting_board)))
            else:
                res.append((action, maxvalue(result(board, action))))
        print(res)

        if player(board) == X:
            max = (-1, -2)
            for i, val in enumerate(res):
                if val[1] > max[1]:
                    max = (i, val[1])
            if max != (-1, -2):
                return res[max[0]][0]
        else:
            min = (-1, 2)
            for i, val in enumerate(res):
                if val[1] < min[1]:
                    min = (i, val[1])
            if min != (-1, 2):
                return res[min[0]][0]


def maxvalue(board):
    utils = []
    for action in actions(board):
        resulting_board = result(board, action)
        if terminal(resulting_board):
            utils.append((action, utility(resulting_board)))
        else:
            utils.append((action, maxvalue(resulting_board)))

    if player(board) == X:
        max = -1
        for i in utils:
            if i[1] > max:
                max = i[1]
        return max
    else:
        min = 1
        for i in utils:
            if i[1] < min:
                min = i[1]
        return min
