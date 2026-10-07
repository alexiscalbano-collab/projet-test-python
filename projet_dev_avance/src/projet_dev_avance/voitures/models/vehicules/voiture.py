from projet_dev_avance.voitures.core.interfaces import Vehicule


class Voiture(Vehicule):

    def __init__(self, marque, modele, annee, kilometrage, motorisation, volume_coffre, categorie):
        super().__init__(marque, modele, annee, kilometrage, motorisation)
        self._volume_coffre = volume_coffre  # en litres
        self._categorie = categorie  # SUV, break, citadine...

    @property
    def type_vehicule(self):
        return "Voiture"

    @property
    def volume_coffre(self):
        return self._volume_coffre

    @volume_coffre.setter
    def volume_coffre(self, valeur):
        if valeur < 0:
            raise ValueError("Le volume du coffre doit être positif")
        self._volume_coffre = valeur

    @property
    def categorie(self):
        return self._categorie

    def afficher(self):
        return (
            f"{self.marque} {self.modele} ({self.annee})"
            f" - {self.kilometrage} km"
            f" - {self.categorie}, coffre {self.volume_coffre} L"
            f" - {self.motorisation.afficher()}"
        )