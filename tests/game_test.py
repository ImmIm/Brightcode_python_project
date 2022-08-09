import unittest
from model.reverci_game import ReverciGame
from model.ai_smart_player import AiSmartPlayer
from model.ai_dumb_player import AiDumbPlayer
from model.human_player import HumanPlayer


class GameTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = ReverciGame({
            'start_position': {'middle'},
            'wining_case': {'c'},
            'game_mode': {'2'},
            'ai_type': {'d'},
            'ai_level': {'3'},
            'visuals': ('X', 'O')
        })

    def test_change_player(self):
        player_one = 1
        player_two = 2
        self.game.change_player()
        self.assertEqual(self.game.current_player.value, player_two)
        self.assertEqual(self.game.other_player.value, player_one)

    def test_create_second_player(self):
        player = self.game.create_second_player(8, {
            'start_position': {'middle'},
            'wining_case': {'c'},
            'game_mode': {'2'},
            'ai_type': {'d'},
            'ai_level': {'3'},
            'visuals': ('X', 'O')
        })
        self.assertIsInstance(self.game.current_player, HumanPlayer)
        self.assertIsInstance(player, AiDumbPlayer)
        self.assertNotIsInstance(player, AiSmartPlayer)
