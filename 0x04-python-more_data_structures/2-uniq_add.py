#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    sum1 = my_list[0]
    for cnt in range(len(my_list) - 1):
        if my_list[cnt] != my_list[cnt + 1]:
            sum1 += my_list[cnt + 1]
    return sum1
