from exceptions import NoLeavingException, NoWallRununing
from coins import Coins

class GameBoard:
  def __init__(self):
    self.winningRow = 1
    self.winningColumn = 0
    self.coinList = [Coins(1,1)]
    # Thought you could confuse me with your list formatting, huh? :)
    self.board = [
      ["🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫"],
      ["🟩", "⬛", "⬛", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫", "⬛", "⬛", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "⬛", "🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "🟫", "🟫", "🟫", "🟫"],
      ["🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫"],
      ["🟫", "🟫", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫", "🟫", "🟫", "🟫", "🟫", "⬛", "🟫", "🟫", "🟫", "🟫", "🟫", "⬛", "🟫"],
      ["🟫", "⬛", "⬛", "⬛", "🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "⬛", "🟫", "🟫", "🟫", "🟫", "🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫"],
      ["🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫", "⬛", "⬛", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "⬛", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "⬛", "🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "🟫", "⬛", "⬛", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "🟫", "🟫"],
      ["🟫", "⬛", "⬛", "⬛", "🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫", "⬛", "⬛", "⬛", "🟫", "⬛", "⬛", "⬛", "🟫"],
      ["🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫", "🟫", "🟫", "⬛", "🟫"],
      ["🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "🟫", "⬛", "🟫", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "🟦"],
      ["🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫", "🟫"],
    ] 
  def printBoard(self, playerRow, playerColumn):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if i == playerRow and j == playerColumn:
          print("👀", end="")
        else:
          print(self.board[i][j], end="")
      print("")
    for coin in self.coinList:
      self.board[coin.coinRow][coin.coinColumn] = '🟨'
    # changed the return False to a raised exception to avoid double error from movement else block in app.py
  def checkMove(self, testRow, testColumn):
      # if(self.board[testRow][testColumn].find("🟨") != -1):
      #     self.board[testRow][testColumn] = ("⬛")
      #     print('Coin Collected')
      # self.board[testRow][testColumn].remove("")
    if(self.board[testRow][testColumn].find("🟫") != -1):
      raise NoWallRununing
    if(self.board[testRow][testColumn].find("🟦") != -1):
      raise NoLeavingException
    return True
  # TODO
  # Return True if the player is in the winning column and row
  # Return False otherwise
  def checkWin(self, playerRow, playerColumn):
    if(playerRow == self.winningRow and playerColumn == self.winningColumn):
      return True            
    return False