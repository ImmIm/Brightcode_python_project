from abc import ABC, abstractmethod


class Controller(ABC):
    
    def __init__(self) -> None:
        super().__init__()

        
    @abstractmethod    
    def start_game():
        pass