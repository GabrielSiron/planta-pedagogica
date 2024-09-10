from models.sensors.temperature.thermocouple import Thermocouple
from models.enums.port_modes import PortModes
from models.enums.arduino_ports import ArduinoMegaAnalogPorts

from utils.ports.analog_port import AnalogPort
from utils.ports.digital_port import DigitalPort
from utils.ports.power_terminal import PowerTerminal

from pyfirmata import ArduinoMega

from time import sleep
board = ArduinoMega('COM11')
vcc = PowerTerminal(board=board, mode=PortModes.POWER)
gnd = PowerTerminal(board=board, mode=PortModes.GROUND)

reles = [50, 51, 52, 53]
modulos_potencia = [5, 6, 7, 8]
reles = [
    DigitalPort(port=porta, board=board, mode='o') for porta in [50, 51, 52, 53]
]

valvula = [
    DigitalPort(port=porta, board=board, mode='o') for porta in [22, 23, 24, 25]
]

resistencia = DigitalPort(port=6, board=board, mode='p')

while True:
    valvula[0].write(1)
    sleep(1)
    valvula[0].write(0)
    sleep(0)

# thermo_input = AnalogPort(port=ArduinoMegaAnalogPorts.A8, board=board)