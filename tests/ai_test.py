import unittest
from controller.reverci_controller import ReverciController
from model.ai_dumb_player import AiDumbPlayer
from model.board import Board


class DumbAiTest(unittest.TestCase):
    def setUp(self):
        self.controller = ReverciController(8, '2','c', True, ('X', 'O'), 'c', 's', 2)
        self.controller.game.rules.set_up_start()
   
    def test_make_move(self):
        res = self.controller.game.current_player.make_move(self.controller.game.rules, self.controller.game.board, 1, 2, self.controller.show_moves_tips(self.controller.game))
        self.assertIsInstance(res, tuple)
        self.assertIsInstance(res[0], tuple)
        self.assertIsInstance(res[0][0], int)
        self.assertIsInstance(res[0][1], int)
        self.assertIsInstance(res[1], list)
        
    