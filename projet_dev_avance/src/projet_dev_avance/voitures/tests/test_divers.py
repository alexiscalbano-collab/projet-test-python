"""Tests des cas restants : voiture, erreurs et services."""

import pytest

from projet_dev_avance.voitures.core.exceptions import (
    DonneeInvalide,
    MotorisationInconnue,
    VoitureDejaPresente,
)
from projet_dev_avance.voitures.models.motorisations import Thermique
from projet_dev_avance.voitures.models.vehicules import Voiture
from projet_dev_avance.voitures.services import (
    MotorisationService,
    VoitureFactory,
)


def test_voiture():
    """Les infos d'une voiture et son affichage."""
    voiture = Voiture("Renault", "Clio", 2021, 80000, Thermique(60, 6),
                      280, "citadine")
    voiture.volume_coffre = 300
    assert voiture.type_vehicule == "Voiture"
    assert voiture.volume_coffre == 300
    assert voiture.categorie == "citadine"
    assert "Renault Clio (2021)" in voiture.afficher()
    with pytest.raises(ValueError):
        voiture.volume_coffre = -1


def test_puissance_pas_un_nombre():
    """Une puissance en texte est refusee."""
    with pytest.raises(DonneeInvalide):
        Thermique(50, 5, "110")


def test_moteur_inconnu():
    """Un type de moteur inconnu est refuse."""
    with pytest.raises(MotorisationInconnue):
        MotorisationService().creer("vapeur", 50, 5)


def test_valeur_negative():
    """Un nombre negatif est refuse par le decorateur valider."""
    with pytest.raises(DonneeInvalide):
        MotorisationService().creer("thermique", -50, 5)


def test_service_moteur_inconnu(service):
    """Le car service refuse un moteur inconnu."""
    with pytest.raises(MotorisationInconnue):
        service.creer({"type_moteur": "vapeur"})


def test_service_avec_puissance(service_rempli):
    """Le car service accepte une puissance et liste les voitures."""
    service_rempli.creer({
        "marque": "Peugeot", "modele": "208", "kilometrage": 1000,
        "annee": 2024, "type_moteur": "thermique", "reservoir": 44,
        "consommation": 5, "coffre": 311, "categorie": "citadine",
        "puissance": 100,
    })
    assert len(service_rempli.lister_voitures()) == 4


def test_doublon(service_rempli):
    """Ajouter deux fois la meme voiture est refuse."""
    voiture = service_rempli.chercher_voiture("Clio")
    with pytest.raises(VoitureDejaPresente):
        service_rempli.ajouter_voiture(voiture)


def test_texte_vide():
    """Un texte vide est refuse par le decorateur valider."""
    factory = VoitureFactory()
    with pytest.raises(DonneeInvalide):
        factory.creer("thermique", "", "Clio", 2021, 100, 280,
                      "citadine", 60, 6)
