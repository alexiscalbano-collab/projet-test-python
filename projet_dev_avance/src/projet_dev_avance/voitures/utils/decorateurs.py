from projet_dev_avance.voitures.core.exceptions import DonneeInvalide


# decorateur pour logguer : affiche quand une fonction commence et finit
def logguer(fonction):
    def wrapper(*args, **kwargs):
        print("[LOG] debut de", fonction.__name__)
        resultat = fonction(*args, **kwargs)
        print("[LOG] fin de", fonction.__name__)
        return resultat
    return wrapper


# decorateur pour valider : refuse les textes vides et les nombres negatifs
def valider(fonction):
    def wrapper(*args, **kwargs):
        for valeur in args:
            if type(valeur) == str and valeur == "":
                raise DonneeInvalide("un texte ne peut pas etre vide")
            if (type(valeur) == int or type(valeur) == float) and valeur < 0:
                raise DonneeInvalide("un nombre ne peut pas etre negatif")
        return fonction(*args, **kwargs)
    return wrapper
