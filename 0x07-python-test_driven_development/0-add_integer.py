#!/usr/bin/python3
"""
This is the addition module and it works like this:
>>> add_integer(17, 77)
94
"""


def add_integer(a, b=98):
    """This method sum two digits and
    returns the sum of the two digits
    """

    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    addition = a + b
    return addition
