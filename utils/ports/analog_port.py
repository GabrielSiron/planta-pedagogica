from enum import Enum
from typing import Union, Any

from models.enums.arduino_ports import ArduinoMegaAnalogPorts, ArduinoAnalogPorts
from utils.abcs.pin import Pin
from pyfirmata import ArduinoMega, Arduino, Board, util

from utils.errors import InvalidBoard, InvalidPort, InvalidPortForBoard


class AnalogPort(Pin):
    MIN = 0
    MAX = 1023
    
    def __init__(self, port: Union[ArduinoMegaAnalogPorts, ArduinoAnalogPorts, Any], board: Union[Board, Any]):
        # if not isinstance(board, Board):
        #     raise InvalidBoard()
        
        # if not isinstance(port, Enum):
        #     raise InvalidPort()
        
        # if isinstance(board, ArduinoMega):
        #     if port not in ArduinoMegaAnalogPorts:
        #         raise InvalidPortForBoard()

        #     raise InvalidPortForBoard()
        
        # if isinstance(board, Arduino):
        #     if port not in ArduinoAnalogPorts:
        #         raise InvalidPort()

        super().__init__()
        
        self.max = Pin.ANALOG_MAX_LIMIT
        self.min = Pin.MIN
        self.board = board
        self.port = port.name
        self.allow_multiple_connections = False
        
    def write(self):
        """analog ports do not implements write methods"""
        raise NotImplementedError()
    
    def read(self):
        it = util.Iterator(self.board)
        it.start()
        self.board.analog[self.port].enable_reporting()
        read = self.board.analog[self.port].read()
        return read
    
    def value_is_in_range(self, value: int):
        return value in range(self.min, self.max)