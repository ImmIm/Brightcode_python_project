from abc import ABC, abstractmethod




class TurnBaseGame(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def change_player():
        pass
    
    @abstractmethod
    def make_move():
        pass

    