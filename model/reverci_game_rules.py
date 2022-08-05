from model.game_rules import GameRules
from model.board import Board
from errors.reverci_exceptions import  MoveOnPlayerCellError, NoPossibleMovesError

class ReverciRules(GameRules):
    classic_params = {
        'start_position' : 'middle',
        'wining_case' : 'classic',
    }

    ROUTES = [(0,-1), (-1,-1), (-1, 0),(-1, 1), (0, 1), (1,1), (1,0), (1,-1), (0,0)]
  
    def __init__(self, board:Board, params:dict=classic_params):
        super().__init__()
        self.params = params
        self.board = board
        self.player_one_score = 0
        self.player_two_score = 0
        self.size = board.size
        
    def set_up_start(self):
        """Set ups starting positions

        Args:
            size (int): size of board
        """
        middle = (self.size // 2) - 1
        if self.params['start_position'] == 'middle':
            self.board.update_cell(middle,middle,1)
            self.board.update_cell(middle + 1,middle + 1,1)
            self.board.update_cell(middle,middle + 1,2)
            self.board.update_cell(middle + 1,middle,2)
            self.player_one_score = 2
            self.player_two_score = 2
        elif self.params['start_position'] == 'reverce-middle':
            self.board.update_cell(middle,middle,2)
            self.board.update_cell(middle + 1,middle + 1,2)
            self.board.update_cell(middle,middle + 1,1)
            self.board.update_cell(middle + 1,middle,1)
            self.player_one_score = 2
            self.player_two_score = 2
        
    def check_validity_of_move(self, board:Board, row:int, col:int, player:int, opp_player:int):
        """Checks if turn is valid and if yes. returns all flipped discs list

        Args:
            board (Board): game board
            row (int): Row of move
            col (int): Column of move
            player (int): Current player
            opp_player (int): Opposite player

        Raises:
            MoveOnPlayerCellError: Raises if move in on player cell
            WrongMoveError: _description_

        Returns:
            list: list of all discs to be flipped
        """

        flipped_discs = []
        if board.get_cell(row,col).value in [1,2]:
            raise MoveOnPlayerCellError((row, col), player)
        
        for route in self.ROUTES:
            next_move = (row + route[0], col + route[1])
            try:
                next_cell = board.get_cell(next_move[0], next_move[1]) 
            except IndexError:
                continue
            flag_opp = False
            flipped_discs_tmp = []
            while True:
                if next_cell == opp_player:
                    flag_opp = True
                if ((next_cell == player) and flag_opp):
                    flipped_discs.append(flipped_discs_tmp)
                    flag_opp = False
                    break
                if next_cell == player:
                    break
                if not (next_cell in [1,2]):
                    break
                flipped_discs_tmp.append((next_move[0], next_move[1]))
                next_move = (next_move[0] +  route[0], next_move[1] + route[1])
                try:
                    next_cell = board.get_cell(next_move[0], next_move[1])
                except IndexError:
                    break
                
        flipped_discs = sum(flipped_discs, [])
        
        if flipped_discs:
            return flipped_discs
        else:
            raise NoPossibleMovesError((row, col), player)
    
    def define_winner(self):
        """Defines winner based on payers score

        Returns:
            int: Score of winner or 0 if draw
        """
        if self.params['wining_case'] == 'classic':
            if self.player_one_score > self.player_two_score:
                return self.player_one_score
            elif self.player_one_score < self.player_two_score:
                return self.player_two_score
            else:
                return 0
        elif self.params['wining_case'] == 'reverce':
            if self.player_one_score < self.player_two_score:
                return self.player_one_score
            elif self.player_one_score > self.player_two_score:
                return self.player_two_score
            else:
                return 0           
    