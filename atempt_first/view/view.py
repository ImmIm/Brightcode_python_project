from abc import ABC, abstractmethod

class View(ABC):
    
    def __init__(self) -> None:
        super().__init__()
        
    @abstractmethod
    def render():
        pass
    
    
    @abstractmethod
    def print_message(self, message):
        print(message)