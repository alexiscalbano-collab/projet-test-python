"""Service qui gere les vehicules."""

from projet_dev_avance.voitures.utils import logguer


class VehiculeService:
    """Gere les vehicules (ajout, liste, recherche, suppression)."""

    def __init__(self, repository):
        """Recoit le repository ou sont stockes les vehicules."""
        self.repository = repository

    @logguer
    def ajouter(self, vehicule):
        """Ajoute une voiture."""
        self.repository.ajouter(vehicule)

    @logguer
    def lister(self):
        """Renvoie tous les vehicules."""
        return self.repository.lister()

    @logguer
    def chercher(self, modele):
        """Renvoie la voiture qui a ce modele."""
        return self.repository.chercher(modele)

    @logguer
    def supprimer(self, modele):
        """Supprime la voiture qui a ce modele."""
        self.repository.supprimer(modele)

    @logguer
    def chercher_par_marque(self, marque):
        """Renvoie les voitures de cette marque."""
        return [v for v in self.repository.lister() if v.marque == marque]
