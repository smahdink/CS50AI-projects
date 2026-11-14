import tictactoe

X = "X"
O = "O"
EMPTY = None
board = [[O, EMPTY, X], [EMPTY, X, X], [O, EMPTY, EMPTY]]

# print(tictactoe.actions(board))
# print(tictactoe.result(board, (1, 2)))
# print(tictactoe.utility(tictactoe.result(board, (1, 2))))

# print(tictactoe.winner(board))
# print(tictactoe.terminal(board))
print(tictactoe.minimax(board))
