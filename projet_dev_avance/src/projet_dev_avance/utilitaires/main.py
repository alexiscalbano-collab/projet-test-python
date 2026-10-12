"""Programme principal des utilitaires."""

from projet_dev_avance.utilitaires.module_1 import hello_module_1
from projet_dev_avance.utilitaires.module_2 import add
from projet_dev_avance.utilitaires.math import multiply
from projet_dev_avance.utilitaires.text import to_upper_case


def dire_coucou():
    """Affiche le resultat de chaque fonction utilitaire."""
    print(hello_module_1())
    print(add(1, 2))
    print(multiply(2, 3))
    print(to_upper_case("coucou"))


if __name__ == "__main__":
    dire_coucou()
