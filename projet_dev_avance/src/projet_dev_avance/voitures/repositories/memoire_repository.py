"""Stockage des voitures en memoire."""

from projet_dev_avance.voitures.core.interfaces import Repository
from projet_dev_avance.voitures.core.exceptions import (
    VoitureIntrouvable,
    VoitureDejaPresente,
)


class MemoireRepository(Repository):
    """Repository qui garde les voitures dans une liste."""

    def __init__(self):
        """Demarre avec une liste de voitures vide."""
        self.voitures = []

    def ajouter(self, voiture):
        """Ajoute une voiture."""
        for v in self.voitures:
            if v.modele == voiture.modele:
                raise VoitureDejaPresente(
                    "la voiture " + voiture.modele + " existe deja"
                )
        self.voitures.append(voiture)

    def lister(self):
        """Renvoie toutes les voitures."""
        return self.voitures

    def chercher(self, modele):
        """Renvoie la voiture qui a ce modele."""
        for v in self.voitures:
            if v.modele == modele:
                return v
        raise VoitureIntrouvable("la voiture " + modele + " n'existe pas")

    def supprimer(self, modele):
        """Supprime la voiture qui a ce modele."""
        voiture = self.chercher(modele)
        self.voitures.remove(voiture)

    def lister_motorisations(self):
        """Renvoie tous les moteurs."""
        return [v.motorisation for v in self.voitures]
