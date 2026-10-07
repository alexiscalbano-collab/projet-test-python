# les erreurs de notre projet


class CatalogueErreur(Exception):
    pass


class VoitureIntrouvable(CatalogueErreur):
    pass


class VoitureDejaPresente(CatalogueErreur):
    pass


class DonneeInvalide(CatalogueErreur):
    pass


class MotorisationInconnue(CatalogueErreur):
    pass
