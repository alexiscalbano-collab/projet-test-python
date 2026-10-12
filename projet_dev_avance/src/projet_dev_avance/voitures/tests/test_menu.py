"""Tests du menu en ligne de commande."""

from projet_dev_avance.voitures.cli.menu import lancer_menu
from projet_dev_avance.voitures.services import VoitureFactory


def lancer(monkeypatch, service, reponses):
    """Lance le menu en simulant ce que l'utilisateur tape."""
    entrees = iter(reponses + ["0"])
    monkeypatch.setattr("builtins.input", lambda _: next(entrees))
    lancer_menu(service, VoitureFactory(service.motorisation_service))


def test_voir_chercher_supprimer(monkeypatch, capsys, service_rempli):
    """Choix 1, 3, 4 et 5 du menu."""
    lancer(monkeypatch, service_rempli,
           ["1", "3", "Zoe", "4", "Clio", "5"])
    sortie = capsys.readouterr().out
    assert "Toyota Yaris" in sortie
    assert "voiture supprimee" in sortie
    assert "au revoir" in sortie


def test_ajouter_les_trois_moteurs(monkeypatch, capsys, service):
    """Choix 2 : ajout d'une thermique, d'une electrique et d'une hybride."""
    lancer(monkeypatch, service, [
        "2", "thermique", "Peugeot", "208", "2020", "45000", "311",
        "citadine", "44", "5",
        "2", "electrique", "Tesla", "Model 3", "2022", "20000", "425",
        "berline", "60", "15",
        "2", "hybride", "Toyota", "Corolla", "2021", "30000", "361",
        "break", "43", "4.5", "1.3", "5",
    ])
    assert capsys.readouterr().out.count("voiture ajoutee") == 3
    assert len(service.lister_voitures()) == 3


def test_erreur_catalogue(monkeypatch, capsys, service):
    """Une voiture introuvable affiche une erreur sans planter."""
    lancer(monkeypatch, service, ["3", "Golf"])
    assert "erreur :" in capsys.readouterr().out


def test_erreur_pas_un_nombre(monkeypatch, capsys, service):
    """Taper du texte a la place d'un nombre affiche une erreur."""
    lancer(monkeypatch, service,
           ["2", "thermique", "Peugeot", "208", "abc"])
    assert "il fallait taper un nombre" in capsys.readouterr().out
