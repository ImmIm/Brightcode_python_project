
from controller.controller import Controller
from model.reverci_game_rules import ReverciRules
from model.reverci_game import ReverciGame
from view.board_console_view import BoardConsoleView
from model.board_cell import BoardCell
from errors.reverci_exceptions import NoPossibleMovesError, MoveOnPlayerCellError
import os


class ReverciController(Controller):
     
    def __init__(self, size, mode, rules, tips, visuals, view):
        super().__init__()
        self.size = size
        self.mode = mode
        self.tips = tips
        self.visuals = visuals
        self.view = view
        self.rules = rules
        
    
    def start_game(self):
        
        game = ReverciGame({
        'start_position' : 'middle',
        'wining_case' : {self.rules},
        },self.size)
        
        game.rules.set_up_start()
        board_view = BoardConsoleView(game.board)
        while True:
            if self.tips:
                self.show_moves_tips(game)
            board_view.draw_board()
            game.make_move()
            game.change_player()
            game.board.clear_board_from_tips()
            # os.system('CLS')
        
            
            
    def update_board(self, move, changes):
       pass
    
    # I really don'n know where put this function in MVC :)
    # It show hints, how many disks will be flipped in that possition
    def show_moves_tips(self, game):
        
        for row in range(game.size):
            for col in range(game.size):
                if game.board.get_cell(row, col).value == game.other_player.value:
                    
                    for route in game.rules.ROUTES:
                        try:
                            if game.board.get_cell(row + route[0], col + route[1]).value == 0:
                                if row + route[0] > 0 and col + route[1]:
                                    cell_near = (row + route[0], col + route[1])
                                    try:
                                        changes = game.rules.check_validity_of_move(game.board, cell_near[0], cell_near[1], game.current_player.value, game.other_player.value)
                                        game.board.update_cell(cell_near[0], cell_near[1],0, len(changes))
                                    except (NoPossibleMovesError, MoveOnPlayerCellError):
                                        changes = [] 
                        except IndexError:
                            continue
                                                             
                                        
                                        
                                        
                                    
                     