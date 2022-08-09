import unittest
from random import randint
from model.board import Board
from model.board_cell import BoardCell


class BoardTest(unittest.TestCase):
    
    def setUp(self):
        self.board_class = Board(8)
        self.board = self.board_class.board
        
    def test_get_cell(self):
        cell = BoardCell(2)
        row = randint(0, 7)
        col = randint(0, 7)
        self.board[row][col] = cell
        
        self.assertEqual(self.board_class.get_cell(row, col), cell)
        
    def test_update_cell(self):
        cell = BoardCell(2)
        cell.change_look('B')
        row = randint(0, 7)
        col = randint(0, 7)
        self.board_class.update_cell(row, col, 2, 'B')
        self.assertEqual(self.board[row][col].look, cell.look)
        self.assertEqual(self.board[row][col].value, cell.value)