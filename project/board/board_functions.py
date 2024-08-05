my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def is_on_board(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0])


def safe_set_Value(x, y, value, board):
    if is_on_board(x, y, board):
        board[x][y] = value
        return True
    return False
