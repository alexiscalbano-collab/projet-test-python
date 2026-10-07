from projet_dev_avance.voitures.models.motorisations import Thermique, Electrique, Hybride
from projet_dev_avance.voitures.core.exceptions import MotorisationInconnue
from projet_dev_avance.voitures.utils import logguer, valider


class MotorisationService:
    """Cree les moteurs et liste ceux qui sont enregistres."""

    def __init__(self, repository=None):
        self.repository = repository

    @logguer
    @valider
    def creer_thermique(self, reservoir, conso):
        return Thermique(reservoir, conso)

    @logguer
    @valider
    def creer_electrique(self, batterie, conso):
        return Electrique(batterie, conso)

    @logguer
    @valider
    def creer_hybride(self, reservoir, conso_thermique, batterie, conso_electrique):
        return Hybride(reservoir, conso_thermique, batterie, conso_electrique)

    def creer(self, type_moteur, *caracteristiques):
        if type_moteur == "thermique":
            return self.creer_thermique(*caracteristiques)
        if type_moteur == "electrique":
            return self.creer_electrique(*caracteristiques)
        if type_moteur == "hybride":
            return self.creer_hybride(*caracteristiques)
        raise MotorisationInconnue("motorisation inconnue : " + type_moteur)

    @logguer
    def lister(self):
        return self.repository.lister_motorisations()
