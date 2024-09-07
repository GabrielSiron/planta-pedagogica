from models.sensors.temperature.thermocouple import Thermocouple
from models.enums.port_modes import PortModes
from models.enums.arduino_ports import ArduinoMegaAnalogPorts

from utils.ports.analog_port import AnalogPort
from utils.ports.digital_port import DigitalPort
from utils.ports.power_terminal import PowerTerminal

from pyfirmata import ArduinoMega

config = {
    'digital' : tuple(x for x in range(54)),
    'analog' : tuple(x for x in range(16)),
    'pwm' : tuple(x for x in range(2,14)),
    'use_ports' : True,
    'disabled' : (0, 1, 14, 15)
}

board = '' # ArduinoMega('COM8')
vcc = PowerTerminal(board=board, mode=PortModes.POWER)
gnd = PowerTerminal(board=board, mode=PortModes.GROUND)
thermo_input = AnalogPort(port=ArduinoMegaAnalogPorts.A0, board=board)
