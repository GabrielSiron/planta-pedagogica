from abc import ABC, abstractmethod


class Component(ABC):
    
    @abstractmethod
    def method(self):
        pass
    