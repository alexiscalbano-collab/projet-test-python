"""Factory qui cree les voitures."""

# une voiture a beaucoup d'infos, donc beaucoup de parametres
# pylint: disable=too-many-arguments,too-many-positional-arguments
from projet_dev_avance.voitures.models.vehicules import Voiture
from projet_dev_avance.voitures.services.motorisation_service import (
    MotorisationService,
)
from projet_dev_avance.voitures.utils import logguer, valider


class VoitureFactory:
    """Cree une voiture avec son moteur.

    Le moteur est cree par le MotorisationService.
    """

    def __init__(self, motorisation_service=None):
        # injection de dependance : on recoit le service deja cree
        """Recoit le service qui cree les moteurs."""
        self.motorisation_service = (
            motorisation_service or MotorisationService()
        )

    @logguer
    @valider
    def creer_voiture(
        self,
        marque,
        modele,
        annee,
        kilometrage,
        volume_coffre,
        categorie,
        moteur,
    ):
        """Cree une voiture avec un moteur deja cree."""
        return Voiture(
            marque,
            modele,
            annee,
            kilometrage,
            moteur,
            volume_coffre,
            categorie,
        )

    def creer(
        self,
        type_moteur,
        marque,
        modele,
        annee,
        kilometrage,
        volume_coffre,
        categorie,
        *caracteristiques
    ):
        """Cree le moteur puis la voiture."""
        moteur = self.motorisation_service.creer(
            type_moteur, *caracteristiques
        )
        return self.creer_voiture(
            marque,
            modele,
            annee,
            kilometrage,
            volume_coffre,
            categorie,
            moteur,
        )
