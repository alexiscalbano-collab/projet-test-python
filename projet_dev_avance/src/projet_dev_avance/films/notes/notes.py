def add(notes, film, note):
    notes[film] = note
    print("note", note, "ajoutee pour", film)


def meilleure_note(notes):
    meilleur_film = ""
    meilleure = 0
    for film in notes:
        if notes[film] > meilleure:
            meilleure = notes[film]
            meilleur_film = film
    return meilleur_film, meilleure


notes = {}