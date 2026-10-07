from abc import ABC, abstractmethod


# interface pour toutes les motorisations
class Motorisation(ABC):

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def afficher(self):
        pass
