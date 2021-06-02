from exceptions import NoLeavingException, NoWallRununing
from gameboard import GameBoard
from player import Player
import traceback

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
player = Player(19, 20)


while True:
  board.printBoard(player.rowPosition, player.columnPosition)
  print('-----------------------------')
  selection = input("Make a move: ")
  # TODO
  # Move the player through the board
  # Check if the player has won, if so print a message and break the loop!
  # Conditional that checks the upcoming position and if it is valid, moves the player.
  try:
    if(selection == 'w' and board.checkMove(player.rowPosition - 1, player.columnPosition)):
      player.moveUp()
    elif(selection == 'a' and board.checkMove(player.rowPosition, player.columnPosition - 1)):
      player.moveLeft()
    elif(selection == 's' and board.checkMove(player.rowPosition + 1, player.columnPosition)):
      player.moveDown()
    elif(selection == 'd' and board.checkMove(player.rowPosition, player.columnPosition + 1)):
      player.moveRight()
    else:
      print('Error: Please enter a valid movement command!')

  except NoLeavingException:
    print('You can\'t leave, WIMP!')

  except NoWallRununing:
    print("Can\'t walk on walls, nerd!")

  # except IndexError:
  #   print('You can\'t leave, WIMP!')

  except:
    print('There was an error!')
    traceback.print_exc()

  # Game won logic, seems to work well.... for now! :)
  if(board.checkWin(player.rowPosition, player.columnPosition)):
    board.printBoard(player.rowPosition, player.columnPosition)
    print('-----------------------------')
    print('🎉Congrats, You have won!🎉')
    break
