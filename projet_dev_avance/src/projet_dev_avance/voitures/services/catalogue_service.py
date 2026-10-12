"""Service principal du catalogue (car service)."""

from projet_dev_avance.voitures.utils import logguer
from projet_dev_avance.voitures.core.exceptions import MotorisationInconnue
from projet_dev_avance.voitures.services.voiture_factory import VoitureFactory


class CatalogueService:
    """Point d'entree du catalogue.

    S'appuie sur le VehiculeService et le MotorisationService.
    """

    def __init__(self, vehicule_service, motorisation_service):
        """Recoit les services dont le catalogue a besoin."""
        self.vehicule_service = vehicule_service
        self.motorisation_service = motorisation_service

    @logguer
    def ajouter_voiture(self, voiture):
        """Ajoute une voiture au catalogue."""
        self.vehicule_service.ajouter(voiture)

    @logguer
    def lister_voitures(self):
        """Renvoie toutes les voitures du catalogue."""
        return self.vehicule_service.lister()

    @logguer
    def chercher_voiture(self, modele):
        """Renvoie la voiture qui a ce modele."""
        return self.vehicule_service.chercher(modele)

    @logguer
    def supprimer_voiture(self, modele):
        """Supprime la voiture qui a ce modele."""
        self.vehicule_service.supprimer(modele)

    @logguer
    def chercher_par_marque(self, marque):
        """Renvoie les voitures de cette marque."""
        return self.vehicule_service.chercher_par_marque(marque)

    @logguer
    def lister_motorisations(self):
        """Renvoie tous les moteurs."""
        return self.motorisation_service.lister()

    @logguer
    def creer(self, data):
        """Cree une voiture depuis un dictionnaire et l'ajoute."""
        type_moteur = data["type_moteur"]
        if type_moteur == "thermique":
            caracteristiques = (data["reservoir"], data["consommation"])
        elif type_moteur == "electrique":
            caracteristiques = (data["batterie"], data["consommation"])
        elif type_moteur == "hybride":
            caracteristiques = (
                data["reservoir"],
                data["consommation_thermique"],
                data["batterie"],
                data["consommation_electrique"],
            )
        else:
            raise MotorisationInconnue(
                "motorisation inconnue : " + type_moteur
            )

        if "puissance" in data:
            caracteristiques = caracteristiques + (data["puissance"],)

        factory = VoitureFactory(self.motorisation_service)
        voiture = factory.creer(
            type_moteur,
            data["marque"],
            data["modele"],
            data["annee"],
            data["kilometrage"],
            data["coffre"],
            data["categorie"],
            *caracteristiques,
        )
        self.ajouter_voiture(voiture)
        return "Created"
