"""Tests du module utilitaires."""

from projet_dev_avance.utilitaires.module_1 import hello_module_1
from projet_dev_avance.utilitaires.module_2 import add
from projet_dev_avance.utilitaires.math import multiply
from projet_dev_avance.utilitaires.text import to_upper_case


def test_hello():
    """Teste : hello."""
    assert hello_module_1() == "Hello module"


def test_add():
    """Teste : add."""
    assert add(1, 2) == 3


def test_multiply():
    """Teste : multiply."""
    assert multiply(2, 3) == 6


def test_to_upper_case():
    """Teste : to upper case."""
    assert to_upper_case("coucou") == "COUCOU"
