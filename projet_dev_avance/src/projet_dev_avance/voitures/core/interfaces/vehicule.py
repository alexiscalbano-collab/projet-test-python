from abc import ABC, abstractmethod


class Vehicule(ABC):

    def __init__(self, marque, modele, annee, kilometrage, motorisation):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._motorisation = motorisation

    @property
    def marque(self):
        return self._marque

    @property
    def modele(self):
        return self._modele

    @property
    def annee(self):
        return self._annee

    @property
    def kilometrage(self):
        return self._kilometrage

    @property
    def motorisation(self):
        return self._motorisation

    @property
    @abstractmethod
    def type_vehicule(self):
        pass

    @abstractmethod
    def afficher(self):
        pass
