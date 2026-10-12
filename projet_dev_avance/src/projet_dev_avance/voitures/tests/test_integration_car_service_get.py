"""Tests d'integration : recuperation d'une voiture."""

import pytest

from projet_dev_avance.voitures.core.exceptions import VoitureIntrouvable


def test_get_vehicle(service_rempli):
    """Teste : get vehicle."""
    voiture = service_rempli.chercher_voiture("Clio")
    assert voiture.marque == "Renault"


def test_get_unknown_vehicle(service_rempli):
    """Teste : get unknown vehicle."""
    with pytest.raises(VoitureIntrouvable):
        service_rempli.chercher_voiture("Golf")
