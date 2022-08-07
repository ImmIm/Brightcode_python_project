import re
from controller.reverci_controller import ReverciController

class GameControl:
    """Class to create Game Controller with chosen params and starts game
    """
    
    regs = {
        # Regular expressions for inputs
        'size' : '^([4-9]|([1][0-6]))',
        'rules' : '^[c|r]{1}',
        'mode' : '^[1-2]{1}',
        'AiType' : '^[d|s]{1}',
        'AiLevel' : '^[1-5]{1}',
        'show_tips' : '^[y|n]{1}',
        'change_look' : '^[y|n]{1}',
        'player_look' : '^\D{1}',
        'view' : '^[c|g]{1}'
    }
    
    
    def __init__(self) -> None:
        self.size = None
        self.rules = None
        self.mode = None
        self.ai_type = None
        self.ai_level = None
        self.show_tips = None
        self.change_player_look = None
        self.player_one_look = 'X'
        self.player_two_look = 'O'
        self.game_view = 'c'
        
        
    def create_game(self):
        """Gets info from user and fills data to create controller
        """
        self.size = int(self.get_info('Enter size of board from 4 to 16 inclusive.\n', self.regs['size']))
        self.rules = self.get_info('Enter rules you want to play. [c]lassical or [r]everse. \n', self.regs['rules'])
        self.mode = self.get_info('Enter mode to play. 1 for PvP, 2 for PvE \n', self.regs['mode'])
        if self.mode == 2:
            self.ai_type = self.get_info('Enter type of AI. [d]umd of [s]mart. \n', self.regs['AiType'])
        if self.ai_type in['s','S']:
            self.ai_level = self.get_info('Enter level of smart AI from 1 to 5 inclusive. \n', self.regs['AiLevel'])
        self.show_tips = self.get_info('Do you want to have tips in game? y/n \n', self.regs['show_tips'])
        self.change_player_look = self.get_info('Do you want to change how players look? y/n \n', self.regs['change_look'])
        if self.change_player_look in ['y', 'Y']:
            self.player_one_look = self.get_info('Set player one look. Any ONE sigh \n', self.regs['player_look'])
            self.player_two_look = self.get_info('Set player two look. Any ONE sigh \n', self.regs['player_look'])
        # self.game_view = self.get_info('What view you want to play? [c]onsole or [g]raphical \n', self.regs['view'])
        
        if self.show_tips in ['y', 'Y']:
            self.show_tips = True
        else:
            self.show_tips = False
        
        controller = ReverciController(self.size, self.mode,self.rules, self.show_tips, (self.player_one_look, self.player_two_look), self.game_view, self.ai_type, int(self.ai_level))
        controller.start_game()
        
    def _dev_create_game(self):
        controller = ReverciController(8, 2,'c', True, ('X', 'O'), 'c', 'd', 1)
        controller.start_game()
        
    def get_info(self, user_input_string:str, reg:str):
        """Helper function to get input and check it with regex

        Args:
            user_input_string (str): String wich be in input
            reg (str): regex with condition

        Returns:
            str: data to specific question
        """
        user_input = input(user_input_string)
        match = re.fullmatch(reg, user_input, re.I)
        if match:
            return match.group(0)
        else:
            while not match:
                user_input = input(user_input_string)
                match = re.fullmatch(reg, user_input, re.I)
            return match.group(0)
