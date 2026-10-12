"""Tests d'integration : recherche par marque."""


def test_find_by_brand(service_rempli):
    """Teste : find by brand."""
    voitures = service_rempli.chercher_par_marque("Renault")
    assert len(voitures) == 2


def test_find_no_result(service_rempli):
    """Teste : find no result."""
    assert service_rempli.chercher_par_marque("Ferrari") == []
