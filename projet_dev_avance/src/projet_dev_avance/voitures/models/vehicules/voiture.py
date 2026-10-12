"""Modele d'une voiture."""

# une voiture a beaucoup d'infos, donc beaucoup de parametres
# pylint: disable=too-many-arguments,too-many-positional-arguments
from projet_dev_avance.voitures.core.interfaces import Vehicule


class Voiture(Vehicule):
    """Une voiture du catalogue."""

    def __init__(
        self,
        marque,
        modele,
        annee,
        kilometrage,
        motorisation,
        volume_coffre,
        categorie,
    ):
        """Cree une voiture."""
        super().__init__(marque, modele, annee, kilometrage, motorisation)
        self._volume_coffre = volume_coffre  # en litres
        self._categorie = categorie  # SUV, break, citadine...

    @property
    def type_vehicule(self):
        """Renvoie le type de vehicule."""
        return "Voiture"

    @property
    def volume_coffre(self):
        """Renvoie le volume du coffre en litres."""
        return self._volume_coffre

    @volume_coffre.setter
    def volume_coffre(self, valeur):
        """Renvoie le volume du coffre en litres."""
        if valeur < 0:
            raise ValueError("Le volume du coffre doit être positif")
        self._volume_coffre = valeur

    @property
    def categorie(self):
        """Renvoie la categorie, par exemple SUV ou break."""
        return self._categorie

    def afficher(self):
        """Renvoie une description lisible."""
        return (
            f"{self.marque} {self.modele} ({self.annee})"
            f" - {self.kilometrage} km"
            f" - {self.categorie}, coffre {self.volume_coffre} L"
            f" - {self.motorisation.afficher()}"
        )
