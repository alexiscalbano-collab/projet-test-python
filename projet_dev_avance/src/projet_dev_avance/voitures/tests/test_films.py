"""Tests du module films."""

from projet_dev_avance.films.movies import (
    creer_film,
    add,
    chercher_film,
    supprimer_film,
)
from projet_dev_avance.films.notes import add as add_note, meilleure_note


def test_creer_film():
    """Teste : creer film."""
    film = creer_film("Inception;2010;Nolan")
    assert film == {
        "titre": "Inception",
        "annee": "2010",
        "realisateur": "Nolan",
    }


def test_ajouter_film():
    """Teste : ajouter film."""
    films = []
    add(films, "Inception", "2010", "Nolan")
    assert len(films) == 1
    assert films[0]["titre"] == "Inception"


def test_chercher_film():
    """Teste : chercher film."""
    films = [creer_film("film1;2010;real1"), creer_film("autre;2014;real2")]
    resultat = chercher_film(films, "film")
    assert len(resultat) == 1
    assert resultat[0]["titre"] == "film1"


def test_supprimer_film():
    """Teste : supprimer film."""
    films = [creer_film("film1;2010;real1")]
    supprimer_film(films, "film1")
    assert not films


def test_meilleure_note():
    """Teste : meilleure note."""
    notes = {}
    add_note(notes, "film1", 12)
    add_note(notes, "film2", 17)
    assert meilleure_note(notes) == ("film2", 17)
