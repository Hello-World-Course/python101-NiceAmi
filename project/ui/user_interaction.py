def is_name_valid(name):
    return len(name) > 2

def is_board_size_valid(board_size):
    board_size = int(board_size)
    return 0 < board_size < 26

def is_number_of_mines_valid(board_size, number_of_mines):
    board_size = int(board_size)
    number_of_mines = int(number_of_mines)
    max_mines = (board_size * board_size) // 2
    return 0 < number_of_mines <= max_mines

def register_user():
    name = input("Hello, what's your name? ")
    if not is_name_valid(name):
        print("Your name is too short")
        return None

    board_size = input(f"{name}, please choose board size: ")
    if not is_board_size_valid(board_size):
        print(f"{name}, you have entered illegal board size")
        return None

    board_size = int(board_size)

    number_of_mines = input(f"{name}, for board size {board_size}, choose number of mines to allocate: ")
    if not is_number_of_mines_valid(board_size, number_of_mines):
        print(f"{name}, you have entered illegal number of mines")
        return None

    number_of_mines = int(number_of_mines)

    return name, board_size, number_of_mines

# Example usage
user_info = register_user()
if user_info:
    user_name, user_board_size, user_num_mines = user_info
    print(f"name: {user_name}, board size: {user_board_size}, number of mines: {user_num_mines}")
