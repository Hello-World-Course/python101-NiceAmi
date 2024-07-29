name = None
board_size = None
number_of_mines = None

name = input("Hello, whats your name")
if len(name) <= 2:
    print("Your name is too short")
else:
    board_size_input = input(f"{name}, please choose board size")
    if board_size_input.isdigit() and 0 < int(board_size_input) < 26:
        board_size = int(board_size_input)
        number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")
        max_mines = (board_size * board_size) // 2
        if number_of_mines_input.isdigit() and 0 < int(number_of_mines_input) <= max_mines:
            number_of_mines = int(number_of_mines_input)
        else:
            print(f"{name}, you have entered illegal number of mines")
    else:
        print(f"{name}, you have entered illegal board size")