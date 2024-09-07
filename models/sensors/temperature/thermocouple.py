from typing import Any
from utils.abcs.pin import Pin
from utils.ports.analog_port import AnalogPort
from utils.ports.power_terminal import PowerTerminal

class Thermocouple:
    __component_name__ = 'Termopar'
    
    def __init__(self, power: PowerTerminal, ground: PowerTerminal, signal: AnalogPort):
        self.power = power
        self.ground = ground
        self.signal = signal
    
    def __setattr__(self, name: str, value: Any):
        if isinstance(value, Pin):
            value.create_connection(self)
        
    def calibrate(self, min: int, max: int):
        self.max = max
        self.min = min
    
    def read(self):
        value = self.signal.read()
        temperature = (value * self.min)/self.max #TODO: check formula
        return temperature
