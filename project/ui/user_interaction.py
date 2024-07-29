name = None
board_size = None
number_of_mines = None
name_input = input("Hello, whats your name\n")
if len(name_input) > 2:
    name = name_input
    board_size_input = input(f"{name}, please choose board size\n")
    if board_size_input.isdigit() and 0 < int(board_size_input) < 26:
        board_size = int(board_size_input)
        max_mines = (board_size * board_size) // 2
        number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate\n")
        if number_of_mines_input.isdigit() and 0 < int(number_of_mines_input) <= max_mines:
            number_of_mines = int(number_of_mines_input)
        else:
            print(f"{name}, you have entered illegal number of mines")
            name = None
            board_size = None
    else:
        print(f"{name}, you have entered illegal board size")
        name = None
else:
    print("Your name is too short")

print(f"name = {name!r}")
print(f"board_size = {board_size}")
print(f"number_of_mines = {number_of_mines}")