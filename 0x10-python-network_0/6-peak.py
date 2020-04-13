#!/usr/bin/python3
import yappi
"""
Function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
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

yappi.start() # Iniciamos la monitorización de yappi
find_peak([1, 2, 6, 4, 3]) # Llamada a la funcion de ejemplo
yappi.get_func_stats().print_all() # Mostramos las stats de ejecución
yappi.stop() # Paramos la monitorización de yappi
