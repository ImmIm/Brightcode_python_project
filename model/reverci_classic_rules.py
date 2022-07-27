from model.game_rules import GameRules
from model.board_cell import BoardCell
from exceptions.reverci_errors import WrongMoveError
from model.player import Player


class ReverciClassicRules(GameRules):
    ROUTES = [(0,-1), (-1,-1), (-1, 0),(-1, 1), (0, 1), (1,1), (1,0), (1,-1)]
  
    def __init__(self) -> None:
        super().__init__()
        
    def check_validity_of_move(self, board, row, col, player, opp_player):
        change = []
        if board.get_cell(row,col) == player:
            raise WrongMoveError((row, col), player)
        
        for route in self.ROUTES:
            next_move = (row + route[0], col + route[1])
            try:
                next_cell = board.get_cell(next_move[0], next_move[1]) 
            except IndexError:
                pass
            flag_opp = False
            change_tmp = []
            while True:
                if next_cell == opp_player:
                    flag_opp = True
                if ((next_cell == player) and flag_opp):
                    change.append(change_tmp)
                    flag_opp = False
                    break
                if next_cell == player:
                    break
                if not (next_cell == Player.X or next_cell == Player.O):
                    break
                change_tmp.append((next_move[0], next_move[1]))
                next_move = (next_move[0] +  route[0], next_move[1] + route[1])
                try:
                    next_cell = board.get_cell(next_move[0], next_move[1])
                except IndexError:
                    break
                
        change = sum(change, [])
        
        if change:
            return change
        else:
            raise WrongMoveError((row, col), player)
    
    def define_winner():
        pass