from exceptions import NoLeavingException, NoWallRununing
from coins import Coin

class GameBoard:
  def __init__(self):
    self.winningRow = 1
    self.winningColumn = 0
    # List of coin objects, see Coins class in coins.py
    self.coins = [Coin(4, 15), Coin(13, 11), Coin(19, 4), Coin(7, 5), Coin(9, 13)]
    # Coin Collected Counter
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
  # add coins to the board using the Coins class
  def addCoins(self):
    for coin in self.coins:
      self.board[coin.coinRow][coin.coinColumn] = '🟨'

  # logic to collect coins, break for efficiency to stop loop on coin collection
  def collectCoin(self, playerRow, playerColumn):
    for coin in self.coins:
      if(playerRow == coin.coinRow and playerColumn == coin.coinColumn):
        self.board[coin.coinRow][coin.coinColumn] = '⬛'
        self.coins.remove(coin)
        self.coinsCollected += 1
        print('Coin Collected')
        break
    
  def printBoard(self, playerRow, playerColumn):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if i == playerRow and j == playerColumn:
          print("👀", end="")
        else:
          print(self.board[i][j], end="")
      print("")
      self.addCoins()
      # call collect coin function, passing the arguments for current playerRow and playerColumn
    self.collectCoin(playerRow,playerColumn)
    # call Counter
    print(f'Total Coins Collected: {self.coinsCollected}')

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