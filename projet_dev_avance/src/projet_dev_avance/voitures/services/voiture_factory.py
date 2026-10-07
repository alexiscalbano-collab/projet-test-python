from projet_dev_avance.voitures.models.motorisations import Thermique, Electrique, Hybride
from projet_dev_avance.voitures.models.vehicules import Voiture
from projet_dev_avance.voitures.core.exceptions import MotorisationInconnue
from projet_dev_avance.voitures.utils import logguer, valider

class VoitureFactory:

    @logguer
    @valider
    def creer_thermique(self, marque, modele, annee, kilometrage, volume_coffre, categorie, reservoir, conso):
        moteur = Thermique(reservoir, conso)
        return Voiture(marque, modele, annee, kilometrage, moteur, volume_coffre, categorie)

    @logguer
    @valider
    def creer_electrique(self, marque, modele, annee, kilometrage, volume_coffre, categorie, batterie, conso):
        moteur = Electrique(batterie, conso)
        return Voiture(marque, modele, annee, kilometrage, moteur, volume_coffre, categorie)

    @logguer
    @valider
    def creer_hybride(self, marque, modele, annee, kilometrage, volume_coffre, categorie, reservoir, conso_thermique, batterie, conso_electrique):
        moteur = Hybride(reservoir, conso_thermique, batterie, conso_electrique)
        return Voiture(marque, modele, annee, kilometrage, moteur, volume_coffre, categorie)

    def creer(self, type_moteur, *infos):
        if type_moteur == "thermique":
            return self.creer_thermique(*infos)
        elif type_moteur == "electrique":
            return self.creer_electrique(*infos)
        elif type_moteur == "hybride":
            return self.creer_hybride(*infos)
        else:
            raise MotorisationInconnue("motorisation inconnue : " + type_moteur)
