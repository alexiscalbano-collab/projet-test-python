from projet_dev_avance.voitures.utils import logguer


class VehiculeService:
    """Gere les vehicules enregistres (ajout, liste, recherche, suppression)."""

    def __init__(self, repository):
        self.repository = repository

    @logguer
    def ajouter(self, vehicule):
        self.repository.ajouter(vehicule)

    @logguer
    def lister(self):
        return self.repository.lister()

    @logguer
    def chercher(self, modele):
        return self.repository.chercher(modele)

    @logguer
    def supprimer(self, modele):
        self.repository.supprimer(modele)

    @logguer
    def chercher_par_marque(self, marque):
        return [v for v in self.repository.lister() if v.marque == marque]
