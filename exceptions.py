# exception for when you try to leave through the entrance
class NoLeavingException(Exception):
  def __init__(self):
    super().__init__()

# exception for when you hit a wall
class NoWallRununing(Exception):
  def __init__(self):
    super().__init__()