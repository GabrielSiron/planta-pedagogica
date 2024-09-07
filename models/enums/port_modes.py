from enum import Enum


class PortModes(Enum):
    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    ANALOG = 'ANALOG'
    PWM = 'PWM'
    POWER = 'POWER'
    GROUND = 'GROUND'
    UNAVAILABLE = 'UNAVAILABLE'