from copy import deepcopy

from model.ai_player import AiPlayer

class AiDumbPlayer(AiPlayer):
    
    def __init__(self, size, value) -> None:
        super().__init__()
        self.size = size
        self.value = value
        
    def make_move(self, rules, board, current_player, other_player, p_moves:set):
        possible_moves = deepcopy(p_moves)
        print(current_player)
        maximum = 0
        best_move = None
        print(possible_moves)
        while True:
            if len(possible_moves) == 0:
                break
            item = possible_moves.pop()
            if item[0] > maximum:
                maximum = item[0]
                best_move = item
        
        print('printed best move ',(best_move[1] + 1, best_move[2] + 1))
        return ((best_move[1], best_move[2]),rules.check_validity_of_move(board, int(best_move[1]), int(best_move[2]), current_player, other_player))
        
