from projet_dev_avance.voitures.core.interfaces import Motorisation


class Thermique(Motorisation):

    def __init__(self, reservoir, consommation_thermique):
        self._reservoir = reservoir  # en litres
        self._consommation_thermique = consommation_thermique  # en L/100km

    @property
    def type_motorisation(self):
        return "thermique"

    @property
    def reservoir(self):
        return self._reservoir

    @property
    def consommation_thermique(self):
        return self._consommation_thermique

    def get_type(self):
        return self.type_motorisation

    def afficher(self):
        return f"thermique, reservoir {self.reservoir} L, conso {self.consommation_thermique} L/100km"


class Electrique(Motorisation):

    def __init__(self, batterie, consommation_electrique):
        self._batterie = batterie  # en kWh
        self._consommation_electrique = consommation_electrique  # en kWh/100km

    @property
    def type_motorisation(self):
        return "electrique"

    @property
    def batterie(self):
        return self._batterie

    @property
    def consommation_electrique(self):
        return self._consommation_electrique

    def get_type(self):
        return self.type_motorisation

    def afficher(self):
        return f"electrique, batterie {self.batterie} kWh, conso {self.consommation_electrique} kWh/100km"


class Hybride(Motorisation):

    def __init__(self, reservoir, consommation_thermique, batterie, consommation_electrique):
        self._reservoir = reservoir
        self._consommation_thermique = consommation_thermique
        self._batterie = batterie
        self._consommation_electrique = consommation_electrique

    @property
    def type_motorisation(self):
        return "hybride"

    @property
    def reservoir(self):
        return self._reservoir

    @property
    def consommation_thermique(self):
        return self._consommation_thermique

    @property
    def batterie(self):
        return self._batterie

    @property
    def consommation_electrique(self):
        return self._consommation_electrique

    def get_type(self):
        return self.type_motorisation

    def afficher(self):
        return (
            f"hybride, reservoir {self.reservoir} L, conso {self.consommation_thermique} L/100km"
            f", batterie {self.batterie} kWh, conso {self.consommation_electrique} kWh/100km"
        )