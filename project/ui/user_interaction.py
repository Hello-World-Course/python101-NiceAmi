# Initialize variables
name = None
board_size = None
number_of_mines = None

# Prompt user for their name
name = input("Hello, whats your name")

# Validate name length
if len(name) <= 2:
    print("Your name is too short")
else:
    # Prompt user for board size
    board_size_input = input(f"{name}, please choose board size")

    # Validate board size
    if not board_size_input.isdigit() or not (0 < int(board_size_input) < 26):
        print(f"{name}, you have entered illegal board size")
    else:
        board_size = int(board_size_input)

        # Calculate maximum number of mines
        max_mines = (board_size * board_size) // 2

        # Prompt user for number of mines
        number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate")

        # Validate number of mines
        if not number_of_mines_input.isdigit() or not (0 < int(number_of_mines_input) <= max_mines):
            print(f"{name}, you have entered illegal number of mines")
        else:
            number_of_mines = int(number_of_mines_input)

# Print final values
print(f'name = "{name}"')
print(f"board_size = {board_size}")
print(f"number_of_mines = {number_of_mines}")