
from errors.reverci_exceptions import NoPossibleMovesError, MoveOnPlayerCellError
from model.turn_base_game import TurnBaseGame
from model.board import Board
from model.human_player import HumanPlayer
from model.ai_dumb_player import AiDumbPlayer
from model.ai_smart_player import AiSmartPlayer
from model.reverci_game_rules import ReverciRules


class ReverciGame(TurnBaseGame):
    
    def __init__(self, rules_params=None, size=8):
        super().__init__()
        self.board = Board(size)
        visuals = rules_params['visuals']
        if visuals:
            self.board.change_visuals(1, visuals[0])
            self.board.change_visuals(2, visuals[1])
        self.rules = ReverciRules(self.board, rules_params)
        self.current_player = HumanPlayer(size, 1)
        self.other_player = self.create_second_player(size, rules_params)
        self.size = size
        
    def change_player(self):
        self.current_player, self.other_player = self.other_player, self.current_player
    
    def create_second_player(self, size, rules_params):
        """_summary_

        Args:
            size (int): size of game board
            rules_params (dict): game parameters

        Returns:
            Player: player specified by params
        """
        if rules_params['game_mode'].pop() == '2':
            if rules_params['ai_type'].pop() == 'd': 
                player = AiDumbPlayer(size, 2)
            else:
                player = AiSmartPlayer(size, 2, int(rules_params['ai_level'].pop()), rules_params, self)
        else:
            player = HumanPlayer(size, 2)
        print(player)
        return player
        
    def make_move(self, possible_moves):
        # Using exceptions for logic is not a good style, I know. Learned it too late :)
        while True:
            try:
                discs_to_flip = self.current_player.make_move(self.rules, self.board, self.current_player.value, self.other_player.value, possible_moves)
                break
            except (NoPossibleMovesError, MoveOnPlayerCellError) as err:
                print(err)
                continue

        self.board.update_cell(discs_to_flip[0][0], discs_to_flip[0][1], self.current_player.value)
        if self.current_player.value == 1:
            self.rules.player_one_score += len(discs_to_flip[1]) + 1
            self.rules.player_two_score -= len(discs_to_flip[1])
        else:
            self.rules.player_two_score += len(discs_to_flip[1]) + 1
            self.rules.player_one_score -= len(discs_to_flip[1])
            
        for cell in discs_to_flip[1]:
            self.board.update_cell(cell[0], cell[1], self.current_player.value)


        
