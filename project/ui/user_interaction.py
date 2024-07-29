name = None
board_size = None
number_of_mines = None

# Get player name
name_input = input("Hello, whats your name")
if len(name_input) > 2:
    name = name_input
else:
    print("Your name is too short")
    exit()

# Get board size
if name:
    board_size_input = input(f"{name}, please choose board size")
    try:
        board_size_int = int(board_size_input)
        if 0 < board_size_int < 26:
            board_size = board_size_int
        else:
            print(f"{name}, you have entered illegal board size")
            exit()
    except ValueError:
        print(f"{name}, you have entered illegal board size")
        exit()

# Get number of mines
if board_size:
    mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")
    try:
        mines_int = int(mines_input)
        max_mines = (board_size * board_size) // 2
        if 0 < mines_int <= max_mines:
            number_of_mines = mines_int
        else:
            print(f"{name}, you have entered illegal number of mines")
            exit()
    except ValueError:
        print(f"{name}, you have entered illegal number of mines")
        exit()

# Print final status
if name and board_size and number_of_mines:
    print(f"name = \"{name}\"")
    print(f"board_size = {board_size}")
    print(f"number_of_mines = {number_of_mines}")