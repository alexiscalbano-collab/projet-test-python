"""Tests du repository MariaDB, avec une fausse base (pas besoin de Docker)."""

import pymysql
import pytest

from projet_dev_avance.voitures.core.exceptions import (
    VoitureDejaPresente,
    VoitureIntrouvable,
)
from projet_dev_avance.voitures.models.motorisations import Thermique
from projet_dev_avance.voitures.models.vehicules import Voiture
from projet_dev_avance.voitures.repositories import MariaDBRepository

LIGNE_CLIO = ("Renault", "Clio", 2021, 80000, 280, "citadine",
              "thermique", 60, 6, None, None)
LIGNE_ZOE = ("Renault", "Zoe", 2022, 10000, 338, "citadine",
             "electrique", None, None, 52, 17)
LIGNE_YARIS = ("Toyota", "Yaris", 2023, 5000, 286, "citadine",
               "hybride", 36, 3.8, 0.9, 4.0)


class FauxCurseur:
    def __init__(self, base):
        self.base = base
        self.lastrowid = 1

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def execute(self, sql, params=None):
        self.base.requetes.append((sql, params))

    def fetchone(self):
        return self.base.reponses.pop(0) if self.base.reponses else None

    def fetchall(self):
        return self.base.reponses.pop(0) if self.base.reponses else []


class FausseConnexion:
    def __init__(self):
        self.requetes = []
        self.reponses = []
        self.commits = 0
        self.rollbacks = 0

    def cursor(self):
        return FauxCurseur(self)

    def commit(self):
        self.commits += 1

    def rollback(self):
        self.rollbacks += 1

    def close(self):
        pass


@pytest.fixture(name="base")
def fixture_base(monkeypatch):
    """Remplace pymysql.connect par une fausse connexion."""
    connexion = FausseConnexion()
    monkeypatch.setattr(pymysql, "connect", lambda **kwargs: connexion)
    return connexion


def clio():
    return Voiture("Renault", "Clio", 2021, 80000, Thermique(60, 6),
                   280, "citadine")


def test_init_cree_les_tables(base):
    """A la creation, le repository cree les 2 tables."""
    MariaDBRepository()
    assert "CREATE TABLE" in base.requetes[0][0]
    assert base.commits == 1


def test_ajouter(base):
    """Ajouter une voiture enregistre le moteur puis la voiture."""
    repo = MariaDBRepository()
    repo.ajouter(clio())
    assert "INSERT INTO motorisations" in base.requetes[-2][0]
    assert "INSERT INTO vehicules" in base.requetes[-1][0]
    assert base.commits == 2


def test_ajouter_doublon(base):
    """Ajouter une voiture qui existe deja leve une erreur."""
    repo = MariaDBRepository()
    base.reponses = [(1,)]
    with pytest.raises(VoitureDejaPresente):
        repo.ajouter(clio())
    assert base.rollbacks == 1


def test_lister(base):
    """Lister transforme chaque ligne en voiture avec le bon moteur."""
    repo = MariaDBRepository()
    base.reponses = [[LIGNE_CLIO, LIGNE_ZOE, LIGNE_YARIS]]
    types = [v.motorisation.type_motorisation for v in repo.lister()]
    assert types == ["thermique", "electrique", "hybride"]


def test_chercher(base):
    """Chercher une voiture qui existe la renvoie."""
    repo = MariaDBRepository()
    base.reponses = [LIGNE_CLIO]
    assert repo.chercher("Clio").marque == "Renault"


def test_chercher_introuvable(base):
    """Chercher une voiture qui n'existe pas leve une erreur."""
    repo = MariaDBRepository()
    with pytest.raises(VoitureIntrouvable):
        repo.chercher("Golf")


def test_supprimer(base):
    """Supprimer efface la voiture puis son moteur."""
    repo = MariaDBRepository()
    base.reponses = [(5,)]
    repo.supprimer("Clio")
    assert "DELETE FROM motorisations" in base.requetes[-1][0]


def test_supprimer_introuvable(base):
    """Supprimer une voiture qui n'existe pas leve une erreur."""
    repo = MariaDBRepository()
    with pytest.raises(VoitureIntrouvable):
        repo.supprimer("Golf")
    assert base.rollbacks == 1


def test_lister_motorisations(base):
    """Lister les moteurs renvoie des objets moteur."""
    repo = MariaDBRepository()
    base.reponses = [[("electrique", None, None, 52, 17)]]
    assert repo.lister_motorisations()[0].batterie == 52


def test_vider(base):
    """Vider supprime les voitures et les moteurs."""
    repo = MariaDBRepository()
    repo.vider()
    assert "DELETE FROM motorisations" in base.requetes[-1][0]
