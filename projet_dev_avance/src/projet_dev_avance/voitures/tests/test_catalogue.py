import pytest

from projet_dev_avance.voitures.repositories import MemoireRepository
from projet_dev_avance.voitures.services import CatalogueService, VoitureFactory
from projet_dev_avance.voitures.core.exceptions import VoitureIntrouvable, DonneeInvalide


def test_ajouter_et_chercher():
    service = CatalogueService(MemoireRepository())
    factory = VoitureFactory()
    voiture = factory.creer("thermique", "Renault", "Clio", 2020, 20000, 340, "citadine", 42, 5.0)
    service.ajouter_voiture(voiture)
    assert service.chercher_voiture("Clio").marque == "Renault"


def test_supprimer():
    service = CatalogueService(MemoireRepository())
    factory = VoitureFactory()
    service.ajouter_voiture(factory.creer("electrique", "Renault", "Zoe", 2021, 10000, 338, "citadine", 52, 17.0))
    service.supprimer_voiture("Zoe")
    with pytest.raises(VoitureIntrouvable):
        service.chercher_voiture("Zoe")


def test_valeur_negative():
    factory = VoitureFactory()
    with pytest.raises(DonneeInvalide):
        factory.creer("thermique", "Renault", "Clio", 2020, -5, 340, "citadine", 42, 5.0)
