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

    if isinstance(a, (int, float)) is True:
        num_1 = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is True:
        num_2 = int(b)
    else:
        raise TypeError("b must be an integer")
    if isinstance(num_1, int) and isinstance(num_2, int):
        return num_1 + num_2
