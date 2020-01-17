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
    else:
        num_1 = int(a)
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    else:
        num_2 = int(b)
    if type(num_1) is int and type(num_2) is int:
        return num_1 + num_2
