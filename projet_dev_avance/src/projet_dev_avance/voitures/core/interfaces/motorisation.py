"""Interface commune a toutes les motorisations."""

from abc import ABC, abstractmethod

from projet_dev_avance.voitures.core.exceptions import DonneeInvalide

PUISSANCE_MAX = 1000  # en ch


# interface pour toutes les motorisations
class Motorisation(ABC):
    """Classe de base de tous les moteurs."""

    @property
    @abstractmethod
    def type_motorisation(self):  # pragma: no cover
        """Renvoie le type de moteur."""
        pass

    @abstractmethod
    def afficher(self):  # pragma: no cover
        """Renvoie une description lisible."""
        pass

    @property
    def puissance(self):
        """Renvoie la puissance en ch (ou None)."""
        return getattr(self, "_puissance", None)

    def _verifier_puissance(self, puissance):
        # la puissance est optionnelle,
        # mais si on la donne elle doit etre conforme
        if puissance is None:
            return None
        if type(puissance) not in (int, float):
            raise DonneeInvalide("la puissance doit etre un nombre")
        if puissance <= 0 or puissance > PUISSANCE_MAX:
            raise DonneeInvalide(
                "la puissance doit etre entre 1 et "
                + str(PUISSANCE_MAX)
                + " ch"
            )
        return puissance
