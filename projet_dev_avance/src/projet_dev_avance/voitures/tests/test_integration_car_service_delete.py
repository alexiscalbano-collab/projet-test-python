"""Tests d'integration : suppression de voitures."""

import pytest

from projet_dev_avance.voitures.core.exceptions import VoitureIntrouvable


def test_delete_vehicle(service_rempli):
    """Teste : delete vehicle."""
    service_rempli.supprimer_voiture("Clio")
    with pytest.raises(VoitureIntrouvable):
        service_rempli.chercher_voiture("Clio")


def test_delete_unknown_vehicle(service_rempli):
    """Teste : delete unknown vehicle."""
    with pytest.raises(VoitureIntrouvable):
        service_rempli.supprimer_voiture("Golf")
