#!/usr/bin/python3
"""
This is the say_my_name module and it works like this:
>>> say_my_name("Julian", "Sandoval")
My name is Julian Sandoval
"""


def say_my_name(first_name, last_name=""):
    """This method concatena two string in a new string
    """

    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
