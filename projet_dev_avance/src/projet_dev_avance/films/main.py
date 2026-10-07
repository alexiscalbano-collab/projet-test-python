from projet_dev_avance.films.movies import add as add_film, creer_film, chercher_film, supprimer_film, films
from projet_dev_avance.films.notes import add as add_note, meilleure_note, notes


def ajouter():
    titre = input("titre du film : ")
    annee = input("annee du film : ")
    realisateur = input("realisateur du film : ")
    add_film(films, titre, annee, realisateur)


def chercher():
    mot = input("quel film tu cherches : ")
    resultat = chercher_film(films, mot)
    print(resultat)


def supprimer():
    nom = input("quel film tu veux supprimer : ")
    supprimer_film(films, nom)


def noter():
    film = input("quel film tu veux noter : ")
    note = int(input("quelle note : "))
    add_note(notes, film, note)


def meilleur():
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