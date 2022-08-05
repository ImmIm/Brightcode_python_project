##################################################################
# Board exceptions

class CellOutOfRangeError(Exception):
    """Raised if row or column greater that size of board
    """
    
    def __init__(self, row, col, size) -> None:
        super().__init__()
        self.row = row
        self.col = col
        self.size = size
        
    def __str__(self) -> str:
        return super().__str__() + f'Row {self.row}, col {self.col} is out of range {self.size}'
    
    
class InvalidCellValueError(Exception):
    """Raised if value is not supported
    """
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value
        
    def __str__(self) -> str:
        return super().__str__() + f'Value {self.value} is not supported. Should be 0,1 or 2'
    
    
##################################################################
# BoardCell Exceptions

class InvalidVisualsKeyError(Exception):
    
    def __init__(self, key) -> None:
        super().__init__()
        self.key = key
        
    def __str__(self) -> str:
        return super().__str__() + f'Key {self.key} is incorrect'