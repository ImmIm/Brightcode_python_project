
from controller.controller import Controller
from model.board_cell import BoardCell
from model.reverci_game_rules import ReverciRules
from model.reverci_game import ReverciGame
import os


class ReverciController(Controller):
     
    game_rules = {
        'classic' : ReverciGame(),
        'reverse' : ReverciGame({
        'start_position' : 'middle',
        'wining_case' : 'reverse',
    })
    }
    
    
    def __init__(self, size, mode, tips, visuals, view):
        super().__init__()
        self.size = size
        self.mode = mode
        self.tips = tips
        self.visuals = visuals
        self.view = view
        
    
    def start_game(self):
       pass
            
            
    def update_board(self, move, changes):
       pass
    
    # I really don'n know where put this function in MVC :)
    # It show hints, how many disks will be flipped in that possition
    def show_moves_tips(self):
        
        for row in range(self.game.size):
            for col in range(self.game.size):
                if self.game.board.get_cell(row, col) == self.game.other_player:
                    
                    for route in self.game.rules.ROUTES:
                        try:
                            if self.game.board.get_cell(row + route[0], col + route[1]) == BoardCell.EMPTY:
                                if row + route[0] > 0 and col + route[1]:
                                    cell_near = (row + route[0], col + route[1])
                                    try:
                                        changes = self.game.rules.check_validity_of_move(self.game.board, cell_near[0], cell_near[1], self.game.current_player, self.game.other_player)
                                        self.game.board.update_cell(cell_near[0], cell_near[1], len(changes) * 10)
                                    except WrongMoveError:
                                        changes = [] 
                        except IndexError:
                            pass
                                                             
                                        
                                        
                                        
                                    
                                        
        
        
        
    def check_correct_move_input(self):
        
        possible_moves = [n for n in range(1, self.game.size + 1)]
        correct_input = False
        # Check for correct move input
        while not correct_input:
            
            moves = (input('Enter turn in format: row, column: ').split(','))
            try:
                row = int(moves[0])
                col = int(moves[1])
                if ((row in possible_moves) and (col in possible_moves)):
                    correct_input = True
            except ValueError:
                pass
            
            
        return (row - 1, col - 1)
    
    def get_full_correct_move(self):
        moves = self.check_correct_move_input()
        correct_flag = False
        
        while not correct_flag:
            try:
                changes = self.game.rules.check_validity_of_move(self.game.board, moves[0], moves[1], self.game.current_player, self.game.other_player)
                correct_flag = True
            except WrongMoveError:
                self.view.print_message('Your move is incorrect, try again!\n')
                moves = self.check_correct_move_input()
                
          
        return (moves, changes)
            
                