#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set()
    sum1 = 0
    for cnt in range(len(my_list)):
        if my_list[cnt] not in new_list:
            new_list.add(my_list[cnt])
    for cnt in new_list:
        sum1 += cnt
    return sum1
