"""Tests des classes de motorisation."""

import pytest

from projet_dev_avance.voitures.models.motorisations import (
    Thermique,
    Electrique,
    Hybride,
)

# ---------- Thermique ----------


def test_thermique():
    # Setup
    """Teste : thermique."""
    moteur = Thermique(50, 5)
    # Assert
    assert moteur.type_motorisation == "thermique"
    assert moteur.reservoir == 50
    assert moteur.consommation_thermique == 5
    assert moteur.get_autonomy() == 1000
    assert moteur.afficher() == "thermique, reservoir 50 L, conso 5 L/100km"


# ---------- Electrique ----------


def test_electrique():
    # Setup
    """Teste : electrique."""
    moteur = Electrique(60, 5)
    # Assert
    assert moteur.type_motorisation == "electrique"
    assert moteur.batterie == 60
    assert moteur.consommation_electrique == 5
    assert moteur.get_autonomy() == 1200
    assert (
        moteur.afficher() == "electrique, batterie 60 kWh, conso 5 kWh/100km"
    )


# ---------- Hybride ----------


def test_hybride():
    # Setup
    """Teste : hybride."""
    moteur = Hybride(40, 4, 10, 10)
    # Assert
    assert moteur.type_motorisation == "hybride"
    assert moteur.reservoir == 40
    assert moteur.consommation_thermique == 4
    assert moteur.batterie == 10
    assert moteur.consommation_electrique == 10
    assert moteur.get_autonomy() == 1000 + 100
    assert moteur.afficher() == (
        "hybride, reservoir 40 L, conso 4 L/100km, "
        "batterie 10 kWh, conso 10 kWh/100km"
    )


# ---------- Les trois d'un coup ----------


@pytest.mark.parametrize(
    "moteur, type_attendu, autonomie_attendue",
    [
        (Thermique(50, 5), "thermique", 1000),
        (Electrique(60, 5), "electrique", 1200),
        (Hybride(40, 4, 10, 10), "hybride", 1100),
    ],
)
def test_les_trois_moteurs(moteur, type_attendu, autonomie_attendue):
    """Teste : les trois moteurs."""
    assert moteur.type_motorisation == type_attendu
    assert moteur.get_autonomy() == autonomie_attendue
