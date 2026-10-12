"""Creer, ajouter, chercher et supprimer des films."""


def creer_film(texte):
    """Cree un film a partir d'un texte 'titre;annee;realisateur'."""
    infos = texte.split(";")
    film = {}
    film["titre"] = infos[0]
    film["annee"] = infos[1]
    film["realisateur"] = infos[2]
    return film


def add(films, titre, annee, realisateur):
    """Ajoute un film a la liste."""
    film = creer_film(titre + ";" + annee + ";" + realisateur)
    films.append(film)
    print("le film", titre, "a ete ajoute")


def chercher_film(films, mot):
    """Renvoie les films dont le titre contient le mot."""
    liste = []
    for f in films:
        if mot in f["titre"]:
            liste.append(f)
    return liste


def supprimer_film(films, titre):
    """Supprime le film qui a ce titre."""
    for f in films:
        if f["titre"] == titre:
            films.remove(f)
            print("le film", titre, "a ete supprime")
            return
    print("le film", titre, "n'existe pas")


films = []
