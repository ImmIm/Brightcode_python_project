from os import terminal_size
from controller.controller import Controller
from exceptions.reverci_errors import WrongMoveError
from model.board_cell import BoardCell
import os


class ReverciController(Controller):
    
    def __init__(self, view, game):
        super().__init__(view, game)
    
    def start_game(self):
        modes = [1,2,3]
        mode = None
        self.view.print_message('Welcome to Reverci game\n===============================')
        
            
        while mode not in modes:
            try:
                mode = int(input('Enter prefered game rules\n1) Classic  2) Reverce 3) Black hole\n'))
            except ValueError:
                continue
            
        self.view.print_message('Have a nice game, X player moves first')
        self.view.print_message('===============================')
        
        terminated = False
        
        
        
        # Game loop
        while True:
            if terminated:
                break
            self.game.board.clear_board_from_tips()
            self.show_moves_tips(self.game.current_player)
            self.view.board_view.draw_board()
            self.view.print_message(f'Player {self.game.current_player} now is your turn!\n')
            
            move = self.get_full_correct_move()
            self.update_board(*move)
            self.game.change_player()
            self.view.board_view.board = self.game.board
            # os.system('CLS')
            
            
            
            
            
            
    def update_board(self, move, changes):
        self.game.board.update_cell(move[0], move[1], self.game.current_player)  
        for item in changes:
            self.game.board.update_cell(item[0], item[1], self.game.current_player)
    
    # I really don'n know where put this function in MVC :)
    # It show hints, how many disks will be flipped in that possition
    def show_moves_tips(self, player):
        for row in range(self.game.size):
            for col in range(self.game.size):
                # print(self.game.board.get_cell(row, col))
                if self.game.board.get_cell(row, col) == player:
                    for route in self.game.rules.ROUTES:
                        cell_near = (row + route[0], col + route[1])
                        if self.game.board.get_cell(cell_near[0], cell_near[1]) == BoardCell.EMPTY:
                            try:
                                changes = self.game.rules.check_validity_of_move(self.game.board, cell_near[0], cell_near[1], player)
                                self.game.board.update_cell(cell_near[0], cell_near[1], len(changes) * 10)
                            except WrongMoveError:
                                changes = []
        
        
        
        
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
                changes = self.game.rules.check_validity_of_move(self.game.board, moves[0], moves[1], self.game.current_player)
                correct_flag = True
            except WrongMoveError:
                self.view.print_message('Your move is incorrect, try again!\n')
                moves = self.check_correct_move_input()
                
          
        return (moves, changes)
            
                