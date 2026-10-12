"""Fixtures partagees entre tous les fichiers de test.

pytest les trouve tout seul.
"""

import pytest

from projet_dev_avance.voitures.repositories import MemoireRepository
from projet_dev_avance.voitures.services import (
    CatalogueService,
    MotorisationService,
    VehiculeService,
)


@pytest.fixture(name="service")
def fixture_service():
    """Car service vide, avec un repository en memoire (sans MariaDB)."""
    repository = MemoireRepository()
    return CatalogueService(
        VehiculeService(repository), MotorisationService(repository)
    )


@pytest.fixture(name="service_rempli")
def fixture_service_rempli(service):
    """Car service avec 3 voitures deja dedans."""
    service.creer(
        {
            "marque": "Renault",
            "modele": "Clio",
            "kilometrage": 80000,
            "annee": 2021,
            "type_moteur": "thermique",
            "reservoir": 60,
            "consommation": 6,
            "coffre": 280,
            "categorie": "citadine",
        }
    )
    service.creer(
        {
            "marque": "Renault",
            "modele": "Zoe",
            "kilometrage": 10000,
            "annee": 2022,
            "type_moteur": "electrique",
            "batterie": 52,
            "consommation": 17,
            "coffre": 338,
            "categorie": "citadine",
        }
    )
    service.creer(
        {
            "marque": "Toyota",
            "modele": "Yaris",
            "kilometrage": 5000,
            "annee": 2023,
            "type_moteur": "hybride",
            "reservoir": 36,
            "consommation_thermique": 3.8,
            "batterie": 0.9,
            "consommation_electrique": 4.0,
            "coffre": 286,
            "categorie": "citadine",
        }
    )
    return service
