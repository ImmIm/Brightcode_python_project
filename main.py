from model.board import Board
from view.board_console_view import BoardConsoleView

board = Board(8)

view = BoardConsoleView(board)

view.draw_board()