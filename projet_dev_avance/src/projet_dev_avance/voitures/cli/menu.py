"""Menu en ligne de commande pour gerer le catalogue de voitures."""

from projet_dev_avance.voitures.core.exceptions import CatalogueErreur


def afficher_menu():
    """Affiche les choix possibles."""
    print("")
    print("1 - voir les voitures")
    print("2 - ajouter une voiture")
    print("3 - chercher une voiture")
    print("4 - supprimer une voiture")
    print("5 - voir les motorisations")
    print("0 - quitter")


def saisir_moteur(type_moteur):
    """Demande les caracteristiques du moteur selon son type."""
    if type_moteur == "thermique":
        reservoir = float(input("reservoir (L) : "))
        conso = float(input("consommation (L/100km) : "))
        return (reservoir, conso)
    if type_moteur == "electrique":
        batterie = float(input("batterie (kWh) : "))
        conso = float(input("consommation (kWh/100km) : "))
        return (batterie, conso)
    reservoir = float(input("reservoir (L) : "))
    conso_t = float(input("consommation thermique (L/100km) : "))
    batterie = float(input("batterie (kWh) : "))
    conso_e = float(input("consommation electrique (kWh/100km) : "))
    return (reservoir, conso_t, batterie, conso_e)


def ajouter_voiture(service, factory):
    """Demande les infos d'une voiture a l'utilisateur et l'ajoute."""
    type_moteur = input("motorisation (thermique / electrique / hybride) : ")
    marque = input("marque : ")
    modele = input("modele : ")
    annee = int(input("annee : "))
    km = int(input("kilometrage : "))
    coffre = int(input("volume du coffre (L) : "))
    categorie = input("categorie (SUV, break...) : ")
    caracteristiques = saisir_moteur(type_moteur)

    voiture = factory.creer(
        type_moteur,
        marque,
        modele,
        annee,
        km,
        coffre,
        categorie,
        *caracteristiques,
    )
    service.ajouter_voiture(voiture)
    print("voiture ajoutee")


def executer_choix(choix, service, factory):
    """Lance l'action qui correspond au choix de l'utilisateur."""
    if choix == "1":
        for v in service.lister_voitures():
            print(v.afficher())
    elif choix == "2":
        ajouter_voiture(service, factory)
    elif choix == "3":
        modele = input("quel modele : ")
        print(service.chercher_voiture(modele).afficher())
    elif choix == "4":
        modele = input("quel modele : ")
        service.supprimer_voiture(modele)
        print("voiture supprimee")
    elif choix == "5":
        for m in service.lister_motorisations():
            print(m.afficher())


def lancer_menu(service, factory):
    """Boucle du menu : tourne jusqu'a ce que l'utilisateur tape 0."""
    choix = ""
    while choix != "0":
        afficher_menu()
        choix = input("ton choix : ")
        try:
            executer_choix(choix, service, factory)
        except CatalogueErreur as e:
            print("erreur :", e)
        except ValueError:
            print("erreur : il fallait taper un nombre")

    print("au revoir")
