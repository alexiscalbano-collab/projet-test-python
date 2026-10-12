"""Moteurs thermique, electrique et hybride."""

from projet_dev_avance.voitures.core.interfaces import Motorisation


class Thermique(Motorisation):
    """Moteur thermique (essence, diesel)."""

    def __init__(self, reservoir, consommation_thermique, puissance=None):
        """Cree un moteur thermique."""
        self._puissance = self._verifier_puissance(puissance)  # en ch
        self._reservoir = reservoir  # en litres
        self._consommation_thermique = consommation_thermique  # en L/100km

    @property
    def type_motorisation(self):
        """Renvoie le type de moteur."""
        return "thermique"

    @property
    def reservoir(self):
        """Renvoie la taille du reservoir en litres."""
        return self._reservoir

    @property
    def consommation_thermique(self):
        """Renvoie la consommation en L/100km."""
        return self._consommation_thermique

    def get_autonomy(self):
        # autonomie en km
        """Renvoie l'autonomie en km."""
        return (self.reservoir * 100) / self.consommation_thermique

    def afficher(self):
        """Renvoie une description lisible."""
        return (
            f"thermique, reservoir {self.reservoir} L, "
            f"conso {self.consommation_thermique} L/100km"
        )


class Electrique(Motorisation):
    """Moteur electrique."""

    def __init__(self, batterie, consommation_electrique, puissance=None):
        """Cree un moteur electrique."""
        self._puissance = self._verifier_puissance(puissance)  # en ch
        self._batterie = batterie  # en kWh
        self._consommation_electrique = consommation_electrique  # en kWh/100km

    @property
    def type_motorisation(self):
        """Renvoie le type de moteur."""
        return "electrique"

    @property
    def batterie(self):
        """Renvoie la taille de la batterie en kWh."""
        return self._batterie

    @property
    def consommation_electrique(self):
        """Renvoie la consommation en kWh/100km."""
        return self._consommation_electrique

    def get_autonomy(self):
        # autonomie en km
        """Renvoie l'autonomie en km."""
        return (self.batterie * 100) / self.consommation_electrique

    def afficher(self):
        """Renvoie une description lisible."""
        return (
            f"electrique, batterie {self.batterie} kWh, "
            f"conso {self.consommation_electrique} kWh/100km"
        )


class Hybride(Motorisation):
    """Moteur hybride (thermique + electrique)."""

    def __init__(
        self,
        reservoir,
        consommation_thermique,
        batterie,
        consommation_electrique,
        puissance=None,
    ):
        """Cree un moteur hybride."""
        self._puissance = self._verifier_puissance(puissance)  # en ch
        self._reservoir = reservoir
        self._consommation_thermique = consommation_thermique
        self._batterie = batterie
        self._consommation_electrique = consommation_electrique

    @property
    def type_motorisation(self):
        """Renvoie le type de moteur."""
        return "hybride"

    @property
    def reservoir(self):
        """Renvoie la taille du reservoir en litres."""
        return self._reservoir

    @property
    def consommation_thermique(self):
        """Renvoie la consommation en L/100km."""
        return self._consommation_thermique

    @property
    def batterie(self):
        """Renvoie la taille de la batterie en kWh."""
        return self._batterie

    @property
    def consommation_electrique(self):
        """Renvoie la consommation en kWh/100km."""
        return self._consommation_electrique

    def get_autonomy(self):
        # autonomie totale = partie thermique + partie electrique
        """Renvoie l'autonomie en km."""
        autonomie = (self.reservoir * 100) / self.consommation_thermique
        if self.consommation_electrique > 0:
            autonomie += (self.batterie * 100) / self.consommation_electrique
        return autonomie

    def afficher(self):
        """Renvoie une description lisible."""
        return (
            f"hybride, reservoir {self.reservoir} L, "
            f"conso {self.consommation_thermique} L/100km, "
            f"batterie {self.batterie} kWh, "
            f"conso {self.consommation_electrique} kWh/100km"
        )
