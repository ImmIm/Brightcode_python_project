from model.turn_base_game import TurnBaseGame
from model.board import Board
from model.player_enum import PlayerEnum
from model.reverci_game_rules import ReverciRules

class ReverciGame(TurnBaseGame):
    
    def __init__(self, size=8):
        super().__init__()
        self.current_player = PlayerEnum.X
        self.other_player = PlayerEnum.O
        self.board = Board(size)
        self.rules = ReverciRules(self.board)
        self.size = size
        
    def change_player(self):
        self.current_player, self.other_player = self.other_player, self.current_player
    
    # Сan raise WrongMoveError
    def make_move(self, row, col):
        return self.rules.check_validity_of_move(self.board, row, col, self.current_player, self.other_player)
