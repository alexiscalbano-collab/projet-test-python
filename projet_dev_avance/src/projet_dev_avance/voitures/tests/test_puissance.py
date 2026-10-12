"""Tests de la puissance des moteurs."""

import pytest

from projet_dev_avance.voitures.models.motorisations import Thermique
from projet_dev_avance.voitures.core.exceptions import DonneeInvalide


def test_puissance_conforme():
    """Teste : puissance conforme."""
    moteur = Thermique(50, 5, 110)
    assert moteur.puissance == 110


def test_puissance_non_conforme():
    """Teste : puissance non conforme."""
    with pytest.raises(DonneeInvalide):
        Thermique(50, 5, -110)
