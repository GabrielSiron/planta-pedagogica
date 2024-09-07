from utils.abcs.pin import Pin
from pyfirmata import Board, util
from models.enums.port_modes import PortModes


class PowerTerminal(Pin):

    def __init__(self, board: Board, mode: PortModes):
        super().__init__()
        self.board = board
        self.allow_multiple_connections = True
        
    def write(self, value: bool):
        raise NotImplemented()
    
    def read(self):
        raise NotImplemented()
    
    def value_is_in_range(self):
        """power terminals do not implements write methods"""
        raise NotImplemented()