
from controller.controller import Controller
from model.reverci_game_rules import ReverciRules
from model.reverci_game import ReverciGame
from view.board_console_view import BoardConsoleView
from model.board_cell import BoardCell
from errors.reverci_exceptions import NoPossibleMovesError, MoveOnPlayerCellError, CellOutOfRangeError
import os
from datetime import datetime

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
        """Function with game loop with all calls
        """
        game = ReverciGame({
        'start_position' : 'middle',
        'wining_case' : {self.rules},
        'game_mode' : {self.mode},
        'ai_type' : {self.ai_type},
        'ai_level' : {self.ai_level},
        'visuals' : self.visuals
        },self.size)
        
        begin_time = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
        print(begin_time)
        game.rules.set_up_start()
        board_view = BoardConsoleView(game.board)
        autopassed = 0
        while True:
            # os.system('CLS')
            possible_moves = self.show_moves_tips(game)
            
            if len(possible_moves) == 0 and autopassed == 1:
                board_view.draw_board()
                winner = game.rules.define_winner()
                print(winner)
                end_time = datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
                self.generate_game_result_file(begin_time, winner)
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
        
    def generate_game_result_file(self, begin, result):
        """Takes time of the start of the game and result of game and creates log .txt file

        Args:
            begin (str): Contains time of start of the game
            result (str): Result of the game
        """
        end_time = datetime.now()
        file_name = end_time.strftime('%m_%d_%Y_%H_%M_%S') + '.txt'
        with open(file_name, 'w') as file:
            file.write('Game started: ' + begin + '\n')
            file.write('Game ended: ' + end_time.strftime('%m/%d/%Y, %H:%M:%S') + '\n')
            file.write('Result: ' + result + '\n')
        print('Created log file: ', file_name)
        
        
    # I really don'n know where put this function in MVC :)
    # It show hints, how many disks will be flipped in that possition
    def show_moves_tips(self, game):
        """Function loops for all enemy discs and calculates valid moves and what discs will be flipped by that move

        Args:
            game (Game): game class with logic of the game

        Returns:
            set: set of all possible moves and discs flipped by that move
            format: {(int, int, int)} where:
            [0] = number of flipped discs
            [1], [2] = row and column
        """
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
                                        
                                        
                                        
                                    
                     