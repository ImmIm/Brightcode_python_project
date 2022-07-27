from abc import ABC, abstractmethod


class Controller(ABC):
    
    def __init__(self, view, game) -> None:
        super().__init__()
        self.view = view
        self.game = game
        
    @abstractmethod    
    def start_game():
        pass