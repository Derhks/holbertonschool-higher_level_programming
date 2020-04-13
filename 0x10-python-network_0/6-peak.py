#!/usr/bin/python3


def find_peak(list_of_integers):
    """This method find the peak of the list"""
    if list_of_integers:
        lo = 0
        hi = len(list_of_integers)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            mi = int(mi)
            if hi == 1:
                return list_of_integers[0]
            if hi == 2:
                return max(list_of_integers)
            if list_of_integers[mi] >= list_of_integers[mi - 1] and\
               list_of_integers[mi] >= list_of_integers[mi + 1]:
                return list_of_integers[mi]
            if mi > 0 and list_of_integers[mi] < list_of_integers[mi + 1]:
                return find_peak(list_of_integers[mi:])
            if mi > 0 and list_of_integers[mi] < list_of_integers[mi - 1]:
                return find_peak(list_of_integers[:mi])
    else:
        return None
