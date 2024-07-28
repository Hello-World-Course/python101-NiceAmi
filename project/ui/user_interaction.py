# Initialize variables
name = None
board_size = None
number_of_mines = None

# Get player name
name_input = input("Hello, whats your name")
if len(name_input) > 2:
    name = name_input
else:
    print("Your name is too short")

# Get board size if name is valid
if name is not None:
    board_size_input = input(f"{name}, please choose board size")
    try:
        board_size_int = int(board_size_input)
        if 0 < board_size_int < 26:
            board_size = board_size_int
        else:
            print(f"{name}, you have entered illegal board size")
    except ValueError:
        print(f"{name}, you have entered illegal board size")

# Get number of mines if board size is valid
if board_size is not None:
    number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")
    try:
        number_of_mines_int = int(number_of_mines_input)
        max_mines = (board_size * board_size) // 2
        if 0 < number_of_mines_int <= max_mines:
            number_of_mines = number_of_mines_int
        else:
            print(f"{name}, you have entered illegal number of mines")
    except ValueError:
        print(f"{name}, you have entered illegal number of mines")

# Print final values
print(f'name = "{name}"')
print(f"board_size = {board_size}")
print(f"number_of_mines = {number_of_mines}")