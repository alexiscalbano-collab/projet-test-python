from projet_dev_avance.module_1 import hello_module_1
from projet_dev_avance.module_2 import add
from projet_dev_avance.math import multiply
from projet_dev_avance.text import to_upper_case


def dire_coucou():
    print(hello_module_1())
    print(add(1, 2))
    print(multiply(2, 3))
    print(to_upper_case("coucou"))


if __name__ == "__main__":
    dire_coucou()