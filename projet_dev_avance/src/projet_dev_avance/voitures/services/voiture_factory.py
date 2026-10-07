from projet_dev_avance.voitures.models.vehicules import Voiture
from projet_dev_avance.voitures.services.motorisation_service import MotorisationService
from projet_dev_avance.voitures.utils import logguer, valider


class VoitureFactory:
    """Cree une voiture avec son moteur (le moteur est cree par le MotorisationService)."""

    def __init__(self, motorisation_service=None):
        # injection de dependance : on recoit le service deja cree
        self.motorisation_service = motorisation_service or MotorisationService()

    @logguer
    @valider
    def creer_voiture(self, marque, modele, annee, kilometrage, volume_coffre, categorie, moteur):
        return Voiture(marque, modele, annee, kilometrage, moteur, volume_coffre, categorie)

    def creer(self, type_moteur, marque, modele, annee, kilometrage, volume_coffre, categorie, *caracteristiques):
        moteur = self.motorisation_service.creer(type_moteur, *caracteristiques)
        return self.creer_voiture(marque, modele, annee, kilometrage, volume_coffre, categorie, moteur)
