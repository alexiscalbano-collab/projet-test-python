"""Tests d'integration : creation de voitures."""

from projet_dev_avance.voitures.repositories import MemoireRepository
from projet_dev_avance.voitures.services import (
    CatalogueService,
    MotorisationService,
    VehiculeService,
)


def creer_service():
    """Cree un car service vide."""
    repository = MemoireRepository()
    return CatalogueService(
        VehiculeService(repository), MotorisationService(repository)
    )


def test_create_electric_vehicle():
    # Setup
    """Teste : create electric vehicle."""
    service = creer_service()
    data = {
        "marque": "Tesla",
        "modele": "Model 3",
        "kilometrage": 20000,
        "annee": 2022,
        "type_moteur": "electrique",
        "batterie": 60,
        "consommation": 15,
        "coffre": 425,
        "categorie": "berline",
    }
    expected_response = "Created"
    # Action
    result = service.creer(data)
    # Assert
    assert result == expected_response


def test_create_thermic_vehicle():
    # Setup
    """Teste : create thermic vehicle."""
    service = creer_service()
    data = {
        "marque": "Peugeot",
        "modele": "208",
        "kilometrage": 45000,
        "annee": 2020,
        "type_moteur": "thermique",
        "reservoir": 44,
        "consommation": 5,
        "coffre": 311,
        "categorie": "citadine",
    }
    expected_response = "Created"
    # Action
    result = service.creer(data)
    # Assert
    assert result == expected_response


def test_create_hybrid_vehicle():
    # Setup
    """Teste : create hybrid vehicle."""
    service = creer_service()
    data = {
        "marque": "Toyota",
        "modele": "Corolla",
        "kilometrage": 30000,
        "annee": 2021,
        "type_moteur": "hybride",
        "reservoir": 43,
        "consommation_thermique": 4.5,
        "batterie": 1.3,
        "consommation_electrique": 5.0,
        "coffre": 361,
        "categorie": "break",
    }
    expected_response = "Created"
    # Action
    result = service.creer(data)
    # Assert
    assert result == expected_response
