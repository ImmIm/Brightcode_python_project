from copy import deepcopy
from errors.reverci_exceptions import NoPossibleMovesError, MoveOnPlayerCellError, CellOutOfRangeError


from model.ai_player import AiPlayer

class AiSmartPlayer(AiPlayer):
    
    def __init__(self, size : int, value : int, level: int, rules_params: set, game) -> None:
        super().__init__()
        self.size = size
        self.value = value
        self.level = level
        self.rules_params = deepcopy(rules_params)
        self.game = deepcopy(game)
        
    def make_move(self, rules, board, current_player, other_player, p_moves:set):
        possible_moves = self.calculate_possible_moves()
        depth = self.level
        for move in possible_moves:
            new_board = deepcopy(self.game.board)
            flipped = self.game.rules.check_validity_of_move(new_board, move[1], move[2], current_player.value, other_player.value)
            for move in flipped:
                new_board[move[1]][move[2]].update_cell(current_player.value)
            # board_value = minimax(new_board, current_player, other_player)
#           return the move with the highest board_value





        # return ((int(best_move[1]), int(best_move[2])),rules.check_validity_of_move(board, int(best_move[1]), int(best_move[2]), current_player, other_player))
        
        
    def calculate_possible_moves(self):
        possible_moves = set()
        changes = []
        for row in range(self.game.size):
            for col in range(self.game.size):
                if self.game.board.get_cell(row, col).value == self.game.other_player.value:
                    
                    for route in self.game.rules.ROUTES:
                        try:
                            if self.game.board.get_cell(row + route[0], col + route[1]).value == 0:
                                if (self.game.size - 1 >= row + route[0] >= 0) and (self.game.size - 1 >= col + route[1] >= 0):
                                    cell_near = (row + route[0], col + route[1])
                                    try:
                                        changes = self.game.rules.check_validity_of_move(self.game.board, cell_near[0], cell_near[1], self.game.current_player.value, self.game.other_player.value)
                                        if len(changes) > 0:
                                            possible_moves.add((len(changes), cell_near[0], cell_near[1]))
                                    except (NoPossibleMovesError, MoveOnPlayerCellError):    
                                        changes = []
                            else:
                                continue
                        except CellOutOfRangeError:
                            continue
                        
        # {(5, 7, 2), (3, 7, 3), (3, 3, 7), (1, 0, 0), (8, 7, 0), (2, 7, 7)}
        # [0] number of flips [1-2] row-col
        return possible_moves
    
                                        
    # def minimax(self, board, max_player, min_player, depth):
    #     if depth == 0:
    #         return
    #     if board is in terminal state:
    #         return 1/-1/0 if it is a win/loss/draw for the AI max_player

    #     values = []
    #     for each possible move for the max_player in the current board:
    #     new_board = the updated board after making the move
    #     board_value = minimax(new_board, min_player, max_player)
    #     values.append(board_value)

    #     if self == max_player:
    #     return max(values)
    #     else:
    #     return min(values)
    
    def calculate_board_score(self):pass
