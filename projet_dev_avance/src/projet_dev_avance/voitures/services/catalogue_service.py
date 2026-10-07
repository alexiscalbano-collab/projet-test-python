from projet_dev_avance.voitures.utils import logguer

class CatalogueService:

    def __init__(self, repository):
        self.repository = repository

    @logguer
    def ajouter_voiture(self, voiture):
        self.repository.ajouter(voiture)

    @logguer
    def lister_voitures(self):
        return self.repository.lister()

    @logguer
    def chercher_voiture(self, modele):
        return self.repository.chercher(modele)

    @logguer
    def supprimer_voiture(self, modele):
        self.repository.supprimer(modele)

    @logguer
    def chercher_par_marque(self, marque):
        liste = []
        for v in self.repository.lister():
            if v.marque == marque:
                liste.append(v)
        return liste
