from projet_dev_avance.voitures.core.exceptions import CatalogueErreur


def lancer_menu(service, factory):
    choix = ""
    while choix != "0":
        print("")
        print("1 - voir les voitures")
        print("2 - ajouter une voiture")
        print("3 - chercher une voiture")
        print("4 - supprimer une voiture")
        print("0 - quitter")
        choix = input("ton choix : ")

        try:
            if choix == "1":
                for v in service.lister_voitures():
                    print(v.afficher())

            elif choix == "2":
                type_moteur = input("motorisation (thermique / electrique / hybride) : ")
                marque = input("marque : ")
                modele = input("modele : ")
                annee = int(input("annee : "))
                km = int(input("kilometrage : "))
                coffre = int(input("volume du coffre (L) : "))
                categorie = input("categorie (SUV, break...) : ")

                if type_moteur == "thermique":
                    reservoir = float(input("reservoir (L) : "))
                    conso = float(input("consommation (L/100km) : "))
                    voiture = factory.creer("thermique", marque, modele, annee, km, coffre, categorie, reservoir, conso)
                elif type_moteur == "electrique":
                    batterie = float(input("batterie (kWh) : "))
                    conso = float(input("consommation (kWh/100km) : "))
                    voiture = factory.creer("electrique", marque, modele, annee, km, coffre, categorie, batterie, conso)
                else:
                    reservoir = float(input("reservoir (L) : "))
                    conso_t = float(input("consommation thermique (L/100km) : "))
                    batterie = float(input("batterie (kWh) : "))
                    conso_e = float(input("consommation electrique (kWh/100km) : "))
                    voiture = factory.creer(type_moteur, marque, modele, annee, km, coffre, categorie, reservoir, conso_t, batterie, conso_e)

                service.ajouter_voiture(voiture)
                print("voiture ajoutee")

            elif choix == "3":
                modele = input("quel modele : ")
                print(service.chercher_voiture(modele).afficher())

            elif choix == "4":
                modele = input("quel modele : ")
                service.supprimer_voiture(modele)
                print("voiture supprimee")

        except CatalogueErreur as e:
            print("erreur :", e)
        except ValueError:
            print("erreur : il fallait taper un nombre")

    print("au revoir")
