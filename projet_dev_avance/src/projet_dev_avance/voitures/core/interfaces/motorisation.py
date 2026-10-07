from abc import ABC, abstractmethod


# interface pour toutes les motorisations
class Motorisation(ABC):

    @property
    @abstractmethod
    def type_motorisation(self):
        pass

    @abstractmethod
    def afficher(self):
        pass
