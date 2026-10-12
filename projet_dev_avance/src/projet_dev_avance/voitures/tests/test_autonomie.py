"""Tests de l'autonomie des moteurs."""

from projet_dev_avance.voitures.models.motorisations import (
    Thermique,
    Electrique,
    Hybride,
)


def test_get_autonomy_electric():
    # Setup
    """Teste : get autonomy electric."""
    battery = 60
    consumption = 5
    motor_electric = Electrique(battery, consumption)
    autonomy_theory = (battery * 100) / consumption
    # Action
    autonomy = motor_electric.get_autonomy()
    # Assert
    assert autonomy == autonomy_theory


def test_get_autonomy_thermique():
    # Setup
    """Teste : get autonomy thermique."""
    reservoir = 50
    consumption = 5
    motor_thermique = Thermique(reservoir, consumption)
    autonomy_theory = (reservoir * 100) / consumption
    # Action
    autonomy = motor_thermique.get_autonomy()
    # Assert
    assert autonomy == autonomy_theory


def test_get_autonomy_hybride():
    # Setup
    """Teste : get autonomy hybride."""
    reservoir = 40
    conso_thermique = 4
    battery = 10
    conso_electrique = 10
    motor_hybride = Hybride(
        reservoir, conso_thermique, battery, conso_electrique
    )
    autonomy_theory = (reservoir * 100) / conso_thermique + (
        battery * 100
    ) / conso_electrique
    # Action
    autonomy = motor_hybride.get_autonomy()
    # Assert
    assert autonomy == autonomy_theory


def test_get_autonomy_hybride_sans_conso_electrique():
    # Setup : conso electrique a 0, on compte que la partie thermique
    """Teste : get autonomy hybride sans conso electrique."""
    motor_hybride = Hybride(43, 4.5, 1.3, 0.0)
    autonomy_theory = (43 * 100) / 4.5
    # Action
    autonomy = motor_hybride.get_autonomy()
    # Assert
    assert autonomy == autonomy_theory
