#!/usr/bin/python3
"""
This is the print_square module and it works like this:
>>> print_square(7)
#######
#######
#######
#######
#######
#######
#######

"""


def print_square(size):
    """This method print nth times the symbol "#" for nth rows
    """

    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for times in range(size):
            print("#", end="")
        print()
