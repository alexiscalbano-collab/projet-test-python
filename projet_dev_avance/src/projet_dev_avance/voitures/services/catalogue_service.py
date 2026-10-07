from projet_dev_avance.voitures.utils import logguer


class CatalogueService:
    """Point d'entree du catalogue : s'appuie sur le VehiculeService et le MotorisationService."""

    def __init__(self, vehicule_service, motorisation_service):
        self.vehicule_service = vehicule_service
        self.motorisation_service = motorisation_service

    @logguer
    def ajouter_voiture(self, voiture):
        self.vehicule_service.ajouter(voiture)

    @logguer
    def lister_voitures(self):
        return self.vehicule_service.lister()

    @logguer
    def chercher_voiture(self, modele):
        return self.vehicule_service.chercher(modele)

    @logguer
    def supprimer_voiture(self, modele):
        self.vehicule_service.supprimer(modele)

    @logguer
    def chercher_par_marque(self, marque):
        return self.vehicule_service.chercher_par_marque(marque)

    @logguer
    def lister_motorisations(self):
        return self.motorisation_service.lister()
