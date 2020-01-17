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

    if type(a) is int or type(a) is float:
        num_1 = a
        if type(a) is float:
            num_1 = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) is int or type(b) is float:
        num_2 = b
        if type(b) is float:
            num_2 = int(b)
    else:
        raise TypeError("b must be an integer")
    if type(num_1) is int and type(num_2) is int:
        return num_1 + num_2
