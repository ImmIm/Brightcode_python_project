from model.player import Player

class AiPlayer(Player):
    
    def __init__(self) -> None:
        super().__init__()
        
    def make_move(self, board):
        return super().make_move(board)
    
    def pass_move(self):
        return super().pass_move()