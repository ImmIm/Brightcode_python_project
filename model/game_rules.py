from abc import ABC, abstractmethod

class GameRules(ABC):
    
    
    def __init__(self) -> None:
        super().__init__()
        
    @abstractmethod
    def check_validity_of_move():
        pass
    
    
    @abstractmethod
    def define_winner():
        pass