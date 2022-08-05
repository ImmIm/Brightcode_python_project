##################################################################
# Board exceptions

class CellOutOfRangeError(Exception):
    """Raises if row or column greater that size of board
    """
    
    def __init__(self, row, col, size) -> None:
        super().__init__()
        self.row = row
        self.col = col
        self.size = size
        
    def __str__(self) -> str:
        return super().__str__() + f'Row {self.row}, col {self.col} is out of range {self.size}'
    
    
class InvalidCellValueError(Exception):
    """Raises if value is not supported
    """
    
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
        
    def __str__(self) -> str:
        return super().__str__() + f'Value {self.value} is not supported. Should be 0,1 or 2'
    
    
##################################################################
# BoardCell Exceptions

class InvalidVisualsKeyError(Exception):
    """Raises if key doesn't exist in VISUALS
    """
    
    def __init__(self, key) -> None:
        super().__init__()
        self.key = key
        
    def __str__(self) -> str:
        return super().__str__() + f'Key {self.key} is incorrect'
    
    
##################################################################  
#  Game Rules Ecxeptions

class WrongMoveError(Exception):
    """Raises if move for player is incorrect due to game rules
    """
    
    def __init__(self, move, player):
        super().__init__()
        self.move = move
        self.player = player
        
    def __str__(self) -> str:
        return super().__str__() + f'Move {self.move[0] + 1}, {self.move[1] + 1} for player {self.player} is incorrect '
    
class MoveOnPlayerCellError(WrongMoveError):
    """Raises if selected move is already occupied by player disc.
    """
    def __init__(self, move, player):
        super().__init__(move, player)
        
    def __str__(self) -> str:
        return super().__str__() + f'cause this cell is already occupied.'
    
    
class NoPossibleMovesError(WrongMoveError):
    """Raises if no possible moves are availible for this possition.
    """
    def __init__(self, move, player):
        super().__init__(move, player)
        
    def __str__(self) -> str:
        return super().__str__() + f'cause for this cell there in no moves availible.'