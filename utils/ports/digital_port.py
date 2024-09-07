from utils.abcs.pin import Pin
from pyfirmata import Board, util
from models.enums.port_modes import PortModes


class DigitalPort(Pin):
    MIN = 0
    MAX = 255
    
    def __init__(self, port: int, board: Board, mode):
        super().__init__()
        self.board = board
        self.port = port
        self.board.digital[self.port].mode(PortModes.INPUT.name)
        self.allow_multiple_connections = False
        
        
    def on(self):
        self.board.digital[self.port].write(True)
        
    def off(self):
        self.board.digital[self.port].write(False)
        
    def write(self, value: bool):
        self.board.digital[self.port].write(value)
    
    def read(self):
        it = util.Iterator(self.board)
        it.start()
        self.board.digital[self.port].enable_reporting()
        read = self.board.digital[self.port].read()
        return read
