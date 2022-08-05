from tenacity import DoAttempt
from model.board import Board
from model.reverci_game_rules import ReverciRules
import re
from view.board_console_view import BoardConsoleView
from controller.game_control import GameControl

# board = Board(8)

# view = BoardConsoleView(board)
# rules = ReverciRules(board)
# rules.set_up_start()

# view.draw_board()


game = GameControl()
game.create_game()