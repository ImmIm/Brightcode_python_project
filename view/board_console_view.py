from view.board_view import BoardView
from model.board import Board

class BoardConsoleView(BoardView):

  def __init__(self, board: Board) -> None:
    super().__init__(board)
    self.board = board

  def draw_board(self):
    board_size = self.board.size
    header = '-' * (4 * board_size + 1)
    print(' ', end='')
    for i in range(board_size):
      print(f'  {i + 1} ', end='')
    print(' ') 
    print(' ' + header)
    for i in range(board_size):
      print(i + 1, end='')
      for j in range(board_size):
        cell = self.board.get_cell(i, j)
        print(f'| {cell.look} ', end='')
      print('|')
    print(header)