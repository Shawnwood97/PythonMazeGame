from gameboard import GameBoard
from player import Player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2

# Set board to GameBoard
board = GameBoard()

# Set player to Player, passing args 3 and 2 for position on row/column
player = Player(3, 2)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the boardW
    # Check if the player has won, if so print a message and break the loop!

    if(selection == 'w'):
        player.moveUp()
    elif(selection == 'a'):
        player.moveLeft()
    elif(selection == 's'):
        player.moveDown()
    elif(selection == 'd'):
        player.moveRight()
    else:
        print('Error: Please enter a valid movement command!')
