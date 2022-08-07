
from controller.controller import Controller
from model.reverci_game_rules import ReverciRules
from model.reverci_game import ReverciGame
from view.board_console_view import BoardConsoleView
from model.board_cell import BoardCell
from errors.reverci_exceptions import NoPossibleMovesError, MoveOnPlayerCellError, CellOutOfRangeError
import os


class ReverciController(Controller):
     
    def __init__(self, size, mode, rules, tips, visuals, view, ai_type, ai_level):
        super().__init__()
        self.size = size
        self.mode = mode
        self.tips = tips
        self.visuals = visuals
        self.view = view
        self.rules = rules
        self.ai_type = ai_type
        self.ai_level = ai_level
        
    
    def start_game(self):
        
        game = ReverciGame({
        'start_position' : 'middle',
        'wining_case' : {self.rules},
        'game_mode' : {self.mode},
        'ai_type' : {self.ai_type},
        'ai_level' : {self.ai_level}
        },self.size)
        
        game.rules.set_up_start()
        board_view = BoardConsoleView(game.board)
        autopassed = 0
        while True:
            possible_moves = self.show_moves_tips(game)
            
            if len(possible_moves) == 0 and autopassed == 1:
                print(game.rules.define_winner())
                break
            if len(possible_moves) == 0:
                autopassed = 0
                autopassed += 1
                game.change_player()
                continue
            print(f'Now is player {game.current_player.value} turn')
            board_view.draw_board()
            game.make_move(possible_moves)
            game.change_player()
            if self.tips:
                game.board.clear_board_from_tips()
            board_view.draw_board()
            
            # os.system('CLS')
        
            
        
    # I really don'n know where put this function in MVC :)
    # It show hints, how many disks will be flipped in that possition
    def show_moves_tips(self, game):
        possible_moves = set()
        changes = []
        for row in range(game.size):
            for col in range(game.size):
                if game.board.get_cell(row, col).value == game.other_player.value:
                    
                    for route in game.rules.ROUTES:
                        try:
                            if game.board.get_cell(row + route[0], col + route[1]).value == 0:
                                if (game.size - 1 >= row + route[0] >= 0) and (game.size - 1 >= col + route[1] >= 0):
                                    cell_near = (row + route[0], col + route[1])
                                    try:
                                        changes = game.rules.check_validity_of_move(game.board, cell_near[0], cell_near[1], game.current_player.value, game.other_player.value)
                                        if len(changes) > 0:
                                            possible_moves.add((len(changes), cell_near[0], cell_near[1]))
                                        if self.tips:
                                            game.board.update_cell(cell_near[0], cell_near[1],0, len(changes))
                                    except (NoPossibleMovesError, MoveOnPlayerCellError):    
                                        changes = []
                            else:
                                continue
                        except CellOutOfRangeError:
                            continue

        return possible_moves                                              
                                        
                                        
                                        
                                    
                     