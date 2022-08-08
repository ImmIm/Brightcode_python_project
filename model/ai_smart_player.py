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
        possible_moves = p_moves
        
            
        print(current_player, other_player)
        depth = self.level
        values = []
        for move in possible_moves:
            new_board = deepcopy(board)
            flipped = rules.check_validity_of_move(new_board, move[1], move[2], current_player, other_player)
            for flip in flipped:
                new_board.update_cell(flip[0],flip[1], current_player)
            if self.level % 2 == 0:
                board_value = self.minimax(new_board, current_player, other_player, self.level, 0)
            else:
                board_value = self.minimax(new_board, current_player, other_player, self.level - 1, 0)
            values.append((board_value, move[1], move[2]))
            
        best_move = max(values, key=lambda item: item[0])

        return ((int(best_move[1]), int(best_move[2])),rules.check_validity_of_move(board, int(best_move[1]), int(best_move[2]), current_player, other_player))
        
        
    def calculate_possible_moves(self, board, current_player, other_player):
        """

        Args:
            board (Board): game board
            current_player (int): value of current player
            other_player (int): value of opponent player

        Returns:
            set: number of flipped discs and row and col of this move
            {(5, 7, 2), (3, 7, 3), (3, 3, 7), (1, 0, 0), (8, 7, 0), (2, 7, 7)}
            [0] number of flips [1-2] row-col
        """
        possible_moves = set()
        changes = []
        for row in range(self.size):
            for col in range(self.size):
                if board.get_cell(row, col).value == other_player:
                    
                    for route in self.game.rules.ROUTES:
                        try:
                            if board.get_cell(row + route[0], col + route[1]).value == 0:
                                if (self.size - 1 >= row + route[0] >= 0) and (self.size - 1 >= col + route[1] >= 0):
                                    cell_near = (row + route[0], col + route[1])
                                    try:
                                        changes = self.game.rules.check_validity_of_move(board, cell_near[0], cell_near[1], current_player, other_player)
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
    
                                        
    def minimax(self, board, max_player, min_player, depth, n_autopasses):
        """_summary_

        Args:
            board (Board): game board
            max_player (int): value of max player
            min_player (int): value of min player
            depth (int): current depth for recursion
            n_autopasses (int): how many autopasses was already

        Returns:
            _type_: score of board on that moment of game
        """
        if depth == 0:
            return self.calculate_board_score(board, max_player)
        p_moves = self.calculate_possible_moves(board, max_player, min_player)
        if len(p_moves) == 0 and n_autopasses == 1:
            return self.calculate_board_score(board, max_player)
        else:
            n_autopasses = 1


        values = []
        for move in p_moves:
            new_board = deepcopy(board)
            flipped = self.game.rules.check_validity_of_move(new_board, move[1], move[2], max_player, min_player)
            for flip in flipped:
                new_board.update_cell(flip[0],flip[1], max_player)
            board_value = self.minimax(new_board, min_player, max_player, depth - 1, n_autopasses)
            values.append(board_value + len(p_moves) * 1.3)

        if not values:
            return self.calculate_board_score(board, max_player)
        if self.value == max_player:
            return max(values)
        else:
            return min(values)
    
    def calculate_board_score(self, board, current_player):
        """Calculates value of board for current player

        Args:
            board (Board): game board
            current_player (int): value of current player

        Returns:
            int: board score
        """
        board_score = 0
        for row in range(board.size):
            for col in range(board.size):
                if board.get_cell(row,col).value == current_player:
                    cell_value = self.calculate_cell_value(board, row,col, current_player)
                    board_score += cell_value
        return board_score
        

    def calculate_cell_value(self, board, row, col, current_player) -> int:
        """_summary_

        Args:
            board (Board): game board
            row (int): row of specific cell
            col (int): col of specific cell
            current_player (int): value of current player

        Returns:
            int: value of this cell
        """
        value: int = 1
        surrounded_value = 0
        CORNERS = [(0,0), (0, board.size - 1), (board.size - 1, 0), (board.size - 1, board.size - 1)]
        
        SIDES = [(0, i) for i in range(board.size - 1)] + [(board.size - 1, i) for i in range(board.size - 1)] + [(i, 0) for i in range(board.size - 1)] + [(i, board.size - 1) for i in range(board.size - 1)]
        
        ROUTES = self.game.rules.ROUTES
        
        # if cell in corners
        if (row, col) in CORNERS:
            value *= 2
        # if cell in sides 
        elif (row, col) in SIDES:
            value *= 1.5
            
        route_count = 0
        for route in ROUTES:
            route_count += 1
            if board.size - 1 >= row + route[0] >= 0 and board.size - 1 >= col + route[1] >= 0 and board.get_cell(row + route[0],col + route[1]).value == current_player:
                surrounded_value += 1
        
        if surrounded_value == (1 * route_count):
            value += 10
        else:
            value += surrounded_value
        
        return value
        
        
