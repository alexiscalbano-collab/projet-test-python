from projet_dev_avance.voitures.core.interfaces import Repository
from projet_dev_avance.voitures.core.exceptions import VoitureIntrouvable, VoitureDejaPresente

class MemoireRepository(Repository):

    def __init__(self):
        self.voitures = []

    def ajouter(self, voiture):
        for v in self.voitures:
            if v.modele == voiture.modele:
                raise VoitureDejaPresente("la voiture " + voiture.modele + " existe deja")
        self.voitures.append(voiture)

    def lister(self):
        return self.voitures

    def chercher(self, modele):
        for v in self.voitures:
            if v.modele == modele:
                return v
        raise VoitureIntrouvable("la voiture " + modele + " n'existe pas")

    def supprimer(self, modele):
        voiture = self.chercher(modele)
        self.voitures.remove(voiture)
