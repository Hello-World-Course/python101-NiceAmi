def is_name_valid(name):
    return len(name) > 2

def is_board_size_valid(board_size):
    return 0 < board_size < 26

def is_number_of_mines_valid(board_size, number_of_mines):
    max_mines = (board_size * board_size) // 2
    return 0 < number_of_mines <= max_mines

def register_user():
    name = input("Hello, whats your name? ")
    if not is_name_valid(name):
        print("Your name is too short")
        return None, None, None

    board_size_input = input(f"{name}, please choose board size: ")
    try:
        board_size = int(board_size_input)
    except ValueError:
        print(f"{name}, you have entered illegal board size")
        return None, None, None

    if not is_board_size_valid(board_size):
        print(f"{name}, you have entered illegal board size")
        return None, None, None

    number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate: ")
    try:
        number_of_mines = int(number_of_mines_input)
    except ValueError:
        print(f"{name}, you have entered illegal number of mines")
        return None, None, None

    if not is_number_of_mines_valid(board_size, number_of_mines):
        print(f"{name}, you have entered illegal number of mines")
        return None, None, None

    return name, board_size, number_of_mines