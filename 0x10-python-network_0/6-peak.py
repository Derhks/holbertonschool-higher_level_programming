#!/usr/bin/python3


def find_peak(list_of_integers, itr=0, value=0):
    """This method find the peak of the list"""
    if len(list_of_integers) > 0:
        value = value
        if list_of_integers[itr] > value:
            value = list_of_integers[itr]
        if itr < len(list_of_integers) - 1:
            return find_peak(list_of_integers, itr + 1, value)
        return value
    else:
        return None
