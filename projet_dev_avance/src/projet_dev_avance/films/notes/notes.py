"""Ajouter des notes et trouver le meilleur film."""


def add(notes, film, note):
    """Ajoute une note a un film."""
    notes[film] = note
    print("note", note, "ajoutee pour", film)


def meilleure_note(notes):
    """Renvoie le film qui a la meilleure note."""
    meilleur_film = ""
    meilleure = 0
    for film in notes:
        if notes[film] > meilleure:
            meilleure = notes[film]
            meilleur_film = film
    return meilleur_film, meilleure


notes = {}
