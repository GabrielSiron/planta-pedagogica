class ValueOutOfRange(Exception):
    pass


class InvalidPort(Exception):
    def __init__(self):
        super().__init__('Porta inválida')
        

class InvalidPortForBoard(Exception):
    def __init__(self):
        super().__init__('A placa selecionada não possui essa porta')
        

class InvalidBoard(Exception):
    def __init__(self) -> None:
        super().__init__('Placa inválida')
    

