"""Interface commune a tous les vehicules."""

from abc import ABC, abstractmethod


class Vehicule(ABC):
    """Classe de base de tous les vehicules."""

    def __init__(self, marque, modele, annee, kilometrage, motorisation):
        """Enregistre les infos communes a tous les vehicules."""
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._motorisation = motorisation

    @property
    def marque(self):
        """Renvoie la marque."""
        return self._marque

    @property
    def modele(self):
        """Renvoie le modele."""
        return self._modele

    @property
    def annee(self):
        """Renvoie l'annee."""
        return self._annee

    @property
    def kilometrage(self):
        """Renvoie le kilometrage."""
        return self._kilometrage

    @property
    def motorisation(self):
        """Renvoie le moteur."""
        return self._motorisation

    @property
    @abstractmethod
    def type_vehicule(self):  # pragma: no cover
        """Renvoie le type de vehicule."""
        pass

    @abstractmethod
    def afficher(self):  # pragma: no cover
        """Renvoie une description lisible."""
        pass
