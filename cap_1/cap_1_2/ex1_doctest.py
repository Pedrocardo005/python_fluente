"""
Exemplo para utilizar a biblioteca doctest

Use o -v no final do comando para imprimir detalhes. Ex:
python cap_1/cap_1_2/ex1.doctest.py -v
"""


def soma(a, b):
    """Retorna a soma dos números

    >>> soma(1,2)
    3
    >>> soma(4,3)
    7
    """
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Imprime somente o docstring
    # print(soma.__doc__)
