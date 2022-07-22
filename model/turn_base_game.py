from abc import ABC, abstractmethod




class TurnBaseGame(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    
    def __init__(self, player) -> None:
        super().__init__()
        self.player = player
    
    @abstractmethod
    def change_player():
        pass
    
    @abstractmethod
    def make_move():
        pass
    
    @abstractmethod
    def check_move_validity():
        pass
    
    @abstractmethod
    def define_winner():
        pass
    