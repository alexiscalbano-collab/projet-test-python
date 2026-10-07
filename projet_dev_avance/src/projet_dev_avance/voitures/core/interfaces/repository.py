from abc import ABC, abstractmethod


# interface pour les repositories
class Repository(ABC):

    @abstractmethod
    def ajouter(self, voiture):
        pass

    @abstractmethod
    def lister(self):
        pass

    @abstractmethod
    def chercher(self, modele):
        pass

    @abstractmethod
    def supprimer(self, modele):
        pass
