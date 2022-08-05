from model.board import Board
from view.board_console_view import BoardConsoleView
from model.reverci_game_rules import ReverciRules
from model.player_enum import PlayerEnum
from view.reverci_console_view import ReverciConsoleView
from model.reverci_game import ReverciGame
from controller.reverci_controller import ReverciController

# Functions to define size of board and types of game




# init of MVC
game = ReverciGame(size=8)
board_view = BoardConsoleView(game.board)
view = ReverciConsoleView(board_view)
controller = ReverciController(view, game)


controller.start_game()
