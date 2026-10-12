"""Tests du point d'entree de l'application."""

import pymysql

from projet_dev_avance.voitures import main as main_module
from projet_dev_avance.voitures.repositories import MemoireRepository


def sans_mariadb():
    """Simule une base MariaDB eteinte."""
    raise pymysql.err.OperationalError(2003, "connexion refusee")


def test_main_sans_mariadb(monkeypatch, capsys):
    """Sans MariaDB, le programme passe en memoire et ajoute 3 voitures."""
    monkeypatch.setattr(main_module, "MariaDBRepository", sans_mariadb)
    monkeypatch.setattr("builtins.input", lambda _: "0")
    main_module.main()
    sortie = capsys.readouterr().out
    assert "MariaDB n'est pas lance" in sortie
    assert "au revoir" in sortie


def test_main_avec_base_deja_remplie(monkeypatch, capsys):
    """Si la base a deja des voitures, on n'en rajoute pas."""
    repo = MemoireRepository()
    monkeypatch.setattr(main_module, "MariaDBRepository", lambda: repo)
    reponses = iter(["1", "0", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(reponses))
    main_module.main()
    main_module.main()
    assert len(repo.lister()) == 3
    assert "Peugeot 308" in capsys.readouterr().out
