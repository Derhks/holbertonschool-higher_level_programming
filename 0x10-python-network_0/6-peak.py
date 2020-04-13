#!/usr/bin/python3


def find_peak(list_of_integers):
    """This method find the peak of the list"""
    if len(list_of_integers) > 0:
        value = list_of_integers[0]
        max_value = value
        for cnt in range(len(list_of_integers)):
            if list_of_integers[cnt] > value:
                value = list_of_integers[cnt]
                for cnt2 in range(len(list_of_integers)):
                    if list_of_integers[cnt2] > value:
                        value = list_of_integers[cnt2]
        return value
    else:
        return None
