from soupsieve import match
import re
from model.player import Player

class HumanPlayer(Player):
    
    
    def __init__(self, size, value) -> None:
        super().__init__()
        self.size = size
        self.value = value
        
    def make_move(self, rules, board, current_player, other_player, p_moves):
        user_input = input('Enter move in format *row, column*: ')
        match = re.fullmatch('(\d,\d|\d,* \d)',user_input)
        if match:
            move = match.group().split(',')
            m1 = int(move[0]) - 1
            m2 = int(move[1]) - 1
            return ((m1, m2),rules.check_validity_of_move(board, int(move[0]) - 1, int(move[1]) - 1, current_player, other_player))
        else:
            while not match:
                user_input = input('Enter move: ')
                match = re.fullmatch('(\d,\d|\d,* \d)', user_input)
            move = match.group().split(',')
            m1 = int(move[0]) - 1
            m2 = int(move[1]) - 1
            return ((m1, m2),rules.check_validity_of_move(board, int(move[0]) - 1, int(move[1]) - 1, current_player, other_player))
            
