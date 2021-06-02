class Player:
  def __init__(self, intitalRow, initialColumn):
    self.rowPosition = intitalRow
    self.columnPosition = initialColumn

  # TODO
  def moveUp(self):
    self.rowPosition = self.rowPosition - 1
  # TODO
  def moveDown(self):
    self.rowPosition = self.rowPosition + 1

  # TODO
  def moveLeft(self):
    self.columnPosition = self.columnPosition - 1

  # TODO
  def moveRight(self):
    self.columnPosition = self.columnPosition + 1

  def collectCoin(self, rowPosition, columnPosition, coinRow, coinColumn, board):
    for i in range(len(board)):
      for j in range(len(board[i])):
        if(rowPosition and coinRow == '🟨' and columnPosition and coinColumn == '🟨'):
          print('⬛', end='')