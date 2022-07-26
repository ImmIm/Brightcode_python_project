from model.board_cell import BoardCell
from model.player import Player

class Board:

  def __init__(self, size) -> None:
    self.size = size

    # Allocate the board with empty squares
    middle = (size // 2) - 1
    self.board = [[BoardCell.EMPTY] * size for _ in range(size)]
    self.board[middle][middle], self.board[middle + 1][middle + 1] = Player.X, Player.X
    self.board[middle][middle + 1], self.board[middle + 1][middle] = Player.O, Player.O
    
    
  def get_cell(self, row, col):
    return self.board[row][col]

  def update_cell(self, row, col, value):
    self.board[row][col] = value