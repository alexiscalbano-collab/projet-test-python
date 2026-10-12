"""Interface commune a tous les repositories."""

from abc import ABC, abstractmethod


# interface pour les repositories
class Repository(ABC):
    """Classe de base de tous les repositories."""

    @abstractmethod
    def ajouter(self, voiture):  # pragma: no cover
        """Ajoute une voiture."""
        pass

    @abstractmethod
    def lister(self):  # pragma: no cover
        """Renvoie toutes les voitures."""
        pass

    @abstractmethod
    def chercher(self, modele):  # pragma: no cover
        """Renvoie la voiture qui a ce modele."""
        pass

    @abstractmethod
    def supprimer(self, modele):  # pragma: no cover
        """Supprime la voiture qui a ce modele."""
        pass

    @abstractmethod
    def lister_motorisations(self):  # pragma: no cover
        """Renvoie tous les moteurs."""
        pass
