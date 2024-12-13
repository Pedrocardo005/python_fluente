"""
vector2d.py: a simplistic class demonstrating some special methods

It is simplistic for didactic reasons. It lacks proper error handling,
especially in the ``__add__`` and ``__null__`` methods.

This example is greatly expanded later in the book.

Addition::

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

Absolute value::

    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

Scalar multiplication::

    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0
"""

import math


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Retorna a representação do objeto como string no console
    def __repr__(self):
        # Com o !r imprime o valor real, incluindo valores ocultos como caracteres especiais
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # Sobrescreve a adição
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # Sobrescreve a multiplicação
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
