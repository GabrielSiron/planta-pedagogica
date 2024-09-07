from abc import ABC, abstractmethod

from utils.abcs.component import Component


class Pin(ABC):
    def __init__(self, allow_multiple_connections: bool = False):
        self.connected_to = []
        
    @abstractmethod
    def write(self):
        pass
    
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def value_is_in_range(self):
        pass
    
    def create_connection(self, component: Component):    
        if self.allow_multiple_connections or not self.connected_to:
            self.connected_to.append(component)
