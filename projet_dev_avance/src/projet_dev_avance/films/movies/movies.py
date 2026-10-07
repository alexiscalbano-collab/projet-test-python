def creer_film(texte):
    infos = texte.split(";")
    film = {}
    film["titre"] = infos[0]
    film["annee"] = infos[1]
    film["realisateur"] = infos[2]
    return film


def add(films, titre, annee, realisateur):
    film = creer_film(titre + ";" + annee + ";" + realisateur)
    films.append(film)
    print("le film", titre, "a ete ajoute")


def chercher_film(films, mot):
    liste = []
    for f in films:
        if mot in f["titre"]:
            liste.append(f)
    return liste


def supprimer_film(films, titre):
    for f in films:
        if f["titre"] == titre:
            films.remove(f)
            print("le film", titre, "a ete supprime")
            return
    print("le film", titre, "n'existe pas")


films = []