from copy import deepcopy
from random import randint

from model.ai_player import AiPlayer

class AiDumbPlayer(AiPlayer):
    """Class representing simple ai for game. It choise in 50% chance first possible move and in other 50% move with most discs flipped
    """
    
    def __init__(self, size, value) -> None:
        super().__init__()
        self.size = size
        self.value = value
        
    def make_move(self, rules, board, current_player, other_player, p_moves:set):
        """Function to return move 

        Args:
            rules (Rules): Rules of game
            board (Board: game board
            current_player (int): value of current player
            other_player (int): value of opponent player
            p_moves (set): set of possible moves

        Returns:
            tupple: best move to make and discs which should be flipped by this move
        """
        possible_moves = deepcopy(p_moves)
        maximum = 0
        best_move = None
        chance = randint(1,100)
        # Chance of first possible move
        if chance < 50:
            move = possible_moves.pop()
            return ((int(move[1]), int(move[2])),rules.check_validity_of_move(board, int(move[1]), int(move[2]), current_player, other_player))
        # Best possible move
        while True:
            if len(possible_moves) == 0:
                break
            item = possible_moves.pop()
            if item[0] > maximum:
                maximum = item[0]
                best_move = item
    
        return ((int(best_move[1]), int(best_move[2])),rules.check_validity_of_move(board, int(best_move[1]), int(best_move[2]), current_player, other_player))
        
