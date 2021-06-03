from exceptions import NoLeavingException, NoWallRununing
from coins import Coins

class GameBoard:
  def __init__(self):
    self.winningRow = 1
    self.winningColumn = 0
    # self.coinList = [Coins(1,1)]
    self.coinRow = [4, 13, 19, 7, 9] #13, 19, 7, 9
    self.coinColumn = [16, 11, 4, 3, 13] #
    self.coinsCollected = 0
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
  
  def addCoins(self):
    counter = 0
    while counter < len(self.coinRow):
      self.board[self.coinRow[counter]][self.coinColumn[counter]] = '🟨'
      counter = counter + 1

  def collectCoin(self, playerRow, playerColumn):
    counter = 0
    while counter < len(self.coinRow):
      if(playerRow == self.coinRow[counter] and playerColumn == self.coinColumn[counter]):
        print('Coin Collected')
        self.coinRow.pop(counter)
        self.coinColumn.pop(counter)
        break
      else:
        counter = counter + 1
        # self.board[playerRow][playerColumn] = '⬛'
    
  def printBoard(self, playerRow, playerColumn):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if i == playerRow and j == playerColumn:
          print("👀", end="")
        else:
          print(self.board[i][j], end="")
      print("")
      self.addCoins()
    counter = 0
    while counter < len(self.coinRow):
      if(playerRow == self.coinRow[counter] and playerColumn == self.coinColumn[counter]):
        self.board[playerRow][playerColumn] = '⬛'
        self.coinRow.pop(counter)
        self.coinColumn.pop(counter)
        self.coinsCollected += 1
        print(f'Coin Collected ---- Total Collected: {self.coinsCollected}')
        break
      else:
        counter = counter + 1
      # self.collectCoin(playerRow, playerColumn)

    # changed the return False to a raised exception to avoid double error from movement else block in app.py
  def checkMove(self, testRow, testColumn):
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