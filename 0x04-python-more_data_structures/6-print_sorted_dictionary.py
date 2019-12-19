#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for cnt in sorted(a_dictionary):
        print("{}: {}".format(cnt, a_dictionary[cnt]))
