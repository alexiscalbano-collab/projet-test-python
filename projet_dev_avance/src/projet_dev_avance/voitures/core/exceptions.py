"""Erreurs propres au catalogue."""

# les erreurs de notre projet


class CatalogueErreur(Exception):
    """Erreur de base du catalogue."""


class VoitureIntrouvable(CatalogueErreur):
    """La voiture demandee n'existe pas."""


class VoitureDejaPresente(CatalogueErreur):
    """La voiture existe deja dans le catalogue."""


class DonneeInvalide(CatalogueErreur):
    """Une donnee n'est pas valide."""


class MotorisationInconnue(CatalogueErreur):
    """Le type de moteur n'existe pas."""
