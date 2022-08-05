from model.turn_base_game import TurnBaseGame
from exceptions.reverci_errors import WrongMoveError
from model.board import Board
from model.player import Player
from model.reverci_classic_rules import ReverciClassicRules

class ReverciGame(TurnBaseGame):
    
    def __init__(self, rules=ReverciClassicRules(), size=4):
        super().__init__()
        self.current_player = Player.X
        self.other_player = Player.O
        self.rules = rules
        self.board = Board(size)
        self.size = size
        
    def change_player(self):
        self.current_player, self.other_player = self.other_player, self.current_player
    
    # Сan raise WrongMoveError
    def make_move(self, row, col):
        return self.rules.check_validity_of_move(self.board, row, col, self.current_player)
