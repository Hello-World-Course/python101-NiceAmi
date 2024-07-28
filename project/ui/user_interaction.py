# Initialize parameters as None
name = None
board_size = None
number_of_mines = None

# Get the player's name
name = input("Hello, what's your name: ")

# Validate the player's name
if len(name) <= 2:
    print("Your name is too short")
else:
    # Get the board size
    board_size_input = input(f"{name}, please choose board size: ")

    # Validate the board size
    if not board_size_input.isdigit() or not (0 < int(board_size_input) < 26):
        print(f"{name}, you have entered illegal board size")
    else:
        board_size = int(board_size_input)

        max_mines = (board_size * board_size) // 2  # Using multiplication instead of exponentiation

        # Get the number of mines
        number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate: ")

        if not number_of_mines_input.isdigit() or not (0 < int(number_of_mines_input) <= max_mines):
            print(f"{name}, you have entered illegal number of mines")
        else:
            number_of_mines = int(number_of_mines_input)

            print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")
