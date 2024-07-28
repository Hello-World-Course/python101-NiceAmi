# File: project/ui/user_interaction.py

# Get player name
name = input("Hello, whats your name\n")

# Get board size
board_size = int(input(f"{name}, please choose board size\n"))

# Get number of mines
number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate\n"))

# Print summary
print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")