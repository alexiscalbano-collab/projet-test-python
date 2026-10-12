"""Programme principal des films."""

from projet_dev_avance.films.movies import add as add_film, creer_film, chercher_film, supprimer_film, films
from projet_dev_avance.films.notes import add as add_note, meilleure_note, notes


def ajouter():
    """Demande un film a l'utilisateur et l'ajoute."""
    titre = input("titre du film : ")
    annee = input("annee du film : ")
    realisateur = input("realisateur du film : ")
    add_film(films, titre, annee, realisateur)


def chercher():
    """Demande un mot et affiche les films qui le contiennent."""
    mot = input("quel film tu cherches : ")
    resultat = chercher_film(films, mot)
    print(resultat)


def supprimer():
    """Demande un titre et supprime le film."""
    nom = input("quel film tu veux supprimer : ")
    supprimer_film(films, nom)


def noter():
    """Demande un film et une note, puis l'enregistre."""
    film = input("quel film tu veux noter : ")
    note = int(input("quelle note : "))
    add_note(notes, film, note)


def meilleur():
    """Affiche le film qui a la meilleure note."""
    film, note = meilleure_note(notes)
    print("le meilleur film est", film, "avec", note)


# films deja dans la liste
films.append(creer_film("film1;2010;realisateur1"))
films.append(creer_film("film2;2014;realisateur2"))
films.append(creer_film("film3;2001;realisateur3"))

ajouter()
chercher()
supprimer()
noter()
meilleur()
