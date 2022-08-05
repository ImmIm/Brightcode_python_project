from errors.reverci_exceptions import InvalidVisualsKeyError

class BoardCell:
    # I understans that in should me variable, not constant, but realize it too late
    VISUALS = {1: 'X', 2: 'O', 0: " "}
    
    def __init__(self, value):
        self.value = value
        self.look = self.VISUALS[self.value]
        
    def change_look(self, look):
        """Changes visual representation of cell

        Args:
            look (str): Look of cell
        """
        self.look = look
        
    def default_look(self):
        """Makes cell look default
        """
        self.look = self.VISUALS[self.value]
        
    def update_cell(self, value, look=None):
        """Updates cell with given param's

        Args:
            value (int): logical value of cell
            look (str, optional): new visual representation of cell. Defaults to None if look default.

        """
        self.value = value
        if look:
            self.look = look
        else:
            self.look = self.VISUALS[value]
    
    @classmethod
    def change_default_visuals(cls, key, value):
        """Changes default visuals of cells

        Args:
            key (int): key for VISUALS dict
            value (str): new visual representation of key

        Raises:
            InvalidVisualsKeyError: Raises if key doesn't exist in VISUALS
        """
        if key in cls.VISUALS:
            cls.VISUALS[key] = value
        else:
            raise InvalidVisualsKeyError(key)