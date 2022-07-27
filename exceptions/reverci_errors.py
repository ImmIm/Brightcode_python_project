class WrongMoveError(Exception):
    
    def __init__(self, move, player):
        super().__init__()
        self.move = move
        self.player = player
        
    def __str__(self) -> str:
        return super().__str__() + f'Move {self.move[0] + 1}, {self.move[1] + 1} for player {self.player} is incorrect'