from errors.reverci_exceptions import NoPossibleMovesError, MoveOnPlayerCellError
from model.turn_base_game import TurnBaseGame
from model.board import Board
from model.player_enum import PlayerEnum
from model.human_player import HumanPlayer
from model.ai_dumb_player import AiDumbPlayer
from model.reverci_game_rules import ReverciRules

class ReverciGame(TurnBaseGame):
    
    def __init__(self, rules_params=None, size=8):
        super().__init__()
        self.current_player = AiDumbPlayer(size, 1)
        self.other_player = AiDumbPlayer(size, 2)
        self.board = Board(size)
        self.rules = ReverciRules(self.board, rules_params)
        self.size = size
        
    def change_player(self):
        self.current_player, self.other_player = self.other_player, self.current_player
    
    
    def make_move(self, possible_moves):
        # Using exceptions for logic is not a good style, I know. Learned it too late :)
        while True:
            try:
                discs_to_flip = self.current_player.make_move(self.rules, self.board, self.current_player.value, self.other_player.value, possible_moves)
                print('discs to flip ',discs_to_flip)
                break
            except (NoPossibleMovesError, MoveOnPlayerCellError) as err:
                print(err)
                continue

        print(discs_to_flip[1])
        self.board.update_cell(discs_to_flip[0][0], discs_to_flip[0][1], self.current_player.value)
        for cell in discs_to_flip[1]:
            self.board.update_cell(cell[0], cell[1], self.current_player.value)


        
