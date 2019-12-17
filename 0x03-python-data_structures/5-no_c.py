#!/usr/bin/env python3
def no_c(my_string):
    my_list = list(my_string)
    for cnt in range(0, len(my_string)):
        if my_list[cnt] == 'c' or my_list[cnt] == 'C':
            my_list[cnt] = ""
    new_string = "".join(my_list)
    return new_string
