#!/usr/bin/env python3
def no_c(my_string):
    my_list = list(my_string)
    for cnt in my_list:
        if cnt == 'c' or cnt == 'C':
            my_list.remove(cnt)
    new_string = "".join(my_list)
    return new_string
