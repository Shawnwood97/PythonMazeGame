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
