from abc import ABC, abstractmethod


class Player(ABC):
    
    def __init__(self) -> None:
        super().__init__()
        
    @abstractmethod
    def make_move(self, board):
        pass
