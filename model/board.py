from model.board_cell import BoardCell
from errors.reverci_exceptions import CellOutOfRangeError, InvalidCellValueError

class Board:
  """A class wich contains game board and methods to work with
  """

  def __init__(self, size) -> None:
    self.size = size

    # Allocate the board with empty squares
    middle = (size // 2) - 1
    self.board = [[BoardCell(0) for _ in range(size)] for _ in range(size)]
    self.board[middle][middle], self.board[middle + 1][middle + 1] = BoardCell(1), BoardCell(1)
    self.board[middle][middle + 1], self.board[middle + 1][middle] = BoardCell(2), BoardCell(2)
    
    
  def get_cell(self, row, col):
    """Return a specific cell from board
    T = O(1)

    Args:
        row (int): Row of cell
        col (int): Column of cell

    Raises:
        CellOutOfRangeError: Raised if row or column is out of board's range.

    Returns:
        BoardCell: Cell object of e=inputed row and column
    """
    if row >= self.size or col >= self.size:
      raise CellOutOfRangeError(row, col, self.size)
    return self.board[row][col]

  def update_cell(self, row, col, value, look=None):
    """Updating cell of board
    t = O(1)

    Args:
        row (int): Row of cell
        col (int): Column of cell
        value (int [0,1,2]): Logical value of cell. 0 - Empty, 1 - Player 1, 2 - Player 2
        look (str, optional): Visual representation of cell. Defaults to None if needs a default look.

    Raises:
        CellOutOfRangeError: Raised if row or column is out of board's range.
        InvalidCellValueError: Raised if logical value is not in [0,1,2]
    """
    if row >= self.size or col >= self.size:
      raise CellOutOfRangeError(row, col, self.size)
    if value not in [1,2,0]:
      raise InvalidCellValueError(value)
    self.board[row][col].update_cell(value, look)
    
    
  def clear_board_from_tips(self):
    """Make all board cells to it's default look
    t = O(n^2)
    """
    for row in range(self.size):
      for col in range(self.size):
        self.board[row][col].default_look()
        
  def change_visuals(self, key, value):
    """changes default visuals of cells and update board to look default

    Args:
        key (int): key to internal VISUALS variable
        value (str): 1 character new representation of cell[value]
    """
    BoardCell.change_default_visuals(key, value)
    # I almost sure that this can be done much better way
    self.clear_board_from_tips()
        