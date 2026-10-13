"""Tests de l'API (routes /api/cars et /api/motors).

On remplace la base MariaDB par une fausse fonction requete,
comme ca les tests marchent sans Docker.
"""

import pymysql
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pymysql.err import IntegrityError

from projet_dev_avance import main as main_module
from projet_dev_avance.routers import cars, db, motors

VOITURE = {
    "marque": "Peugeot",
    "modele": "308",
    "annee": 2019,
    "kilometrage": 45000,
    "volume_coffre": 412,
    "categorie": "berline",
    "motorisation_id": 1,
}
MOTEUR = {"type": "thermique", "reservoir": 53, "consommation_thermique": 5.2}


@pytest.fixture(name="client")
def fixture_client():
    """Client de test branche sur les deux routers."""
    app = FastAPI()
    app.include_router(cars.router, prefix="/api")
    app.include_router(motors.router, prefix="/api")
    return TestClient(app)


def fausse_base(monkeypatch, lignes=(), nouvel_id=1, nb=1):
    """Remplace la base par une fonction qui renvoie toujours la meme chose."""
    def requete(_sql, _valeurs=()):
        return list(lignes), nouvel_id, nb

    monkeypatch.setattr(cars, "requete", requete)
    monkeypatch.setattr(motors, "requete", requete)


def base_qui_refuse(monkeypatch):
    """Simule une erreur de la base (doublon ou cle etrangere)."""
    def requete(sql, _valeurs=()):
        if sql.startswith("SELECT"):
            return [{"id": 1}], 0, 1
        raise IntegrityError(1452, "refuse")

    monkeypatch.setattr(cars, "requete", requete)
    monkeypatch.setattr(motors, "requete", requete)


def test_lister_voitures_et_moteurs(client, monkeypatch):
    """GET /api/cars et /api/motors renvoient les lignes de la base."""
    fausse_base(monkeypatch, lignes=[{"id": 1, **VOITURE}])
    assert client.get("/api/cars/").json()[0]["modele"] == "308"
    assert client.get("/api/motors/").status_code == 200


def test_creer_voiture_et_moteur(client, monkeypatch):
    """POST renvoie l'objet cree avec son id."""
    fausse_base(monkeypatch, nouvel_id=7)
    assert client.post("/api/cars/", json=VOITURE).json()["id"] == 7
    assert client.post("/api/motors/", json=MOTEUR).json()["id"] == 7


def test_voir_modifier_supprimer(client, monkeypatch):
    """GET, PUT et DELETE sur un id qui existe."""
    fausse_base(monkeypatch, lignes=[{"id": 1, **VOITURE}])
    assert client.get("/api/cars/1").json()["marque"] == "Peugeot"
    assert client.put("/api/cars/1", json=VOITURE).status_code == 200
    assert client.delete("/api/cars/1").status_code == 200
    assert client.get("/api/motors/1").status_code == 200
    assert client.put("/api/motors/1", json=MOTEUR).status_code == 200
    assert client.delete("/api/motors/1").status_code == 200


def test_bonus_moteur_de_la_voiture(client, monkeypatch):
    """GET /api/cars/1/motors renvoie le moteur de la voiture."""
    fausse_base(monkeypatch, lignes=[{"id": 1, **VOITURE}])
    assert client.get("/api/cars/1/motors").status_code == 200


def test_id_introuvable(client, monkeypatch):
    """Un id qui n'existe pas donne une 404."""
    fausse_base(monkeypatch, lignes=[], nb=0)
    assert client.get("/api/cars/99").status_code == 404
    assert client.delete("/api/cars/99").status_code == 404
    assert client.get("/api/motors/99").status_code == 404
    assert client.delete("/api/motors/99").status_code == 404


def test_base_refuse(client, monkeypatch):
    """Doublon ou moteur utilise : la base refuse, on renvoie une 400."""
    base_qui_refuse(monkeypatch)
    assert client.post("/api/cars/", json=VOITURE).status_code == 400
    assert client.put("/api/cars/1", json=VOITURE).status_code == 400
    assert client.delete("/api/motors/1").status_code == 400


def test_requete_sans_mariadb(monkeypatch):
    """Si MariaDB est eteint, on a un message clair."""
    def connexion_refusee(**_config):
        raise pymysql.err.OperationalError(2003, "connexion refusee")

    monkeypatch.setattr(db.pymysql, "connect", connexion_refusee)
    with pytest.raises(Exception) as erreur:
        db.requete("SELECT 1")
    assert "Connexion a MariaDB impossible" in erreur.value.detail


def test_requete_avec_mariadb(monkeypatch):
    """Avec une fausse connexion, requete renvoie les lignes."""
    class FauxCurseur:
        """Curseur qui ne fait rien."""

        lastrowid = 3
        rowcount = 1

        def __enter__(self):
            return self

        def __exit__(self, *_):
            return False

        def execute(self, *_):
            """Ne fait rien."""

        def fetchall(self):
            """Renvoie une ligne."""
            return [{"id": 3}]

    class FausseConnexion:
        """Connexion qui ne fait rien."""

        def cursor(self):
            """Renvoie le faux curseur."""
            return FauxCurseur()

        def commit(self):
            """Ne fait rien."""

        def close(self):
            """Ne fait rien."""

    monkeypatch.setattr(db.pymysql, "connect", lambda **_: FausseConnexion())
    assert db.requete("SELECT 1") == ([{"id": 3}], 3, 1)


def test_main_lance_le_serveur(monkeypatch):
    """main() lance uvicorn avec l'application."""
    lance = []
    monkeypatch.setattr(main_module.uvicorn, "run", lambda app, **_: lance.append(app))
    main_module.main()
    assert len(lance) == 1
