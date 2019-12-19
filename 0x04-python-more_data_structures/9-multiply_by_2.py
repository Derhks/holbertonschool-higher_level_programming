#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for cnt in a_dictionary:
        new_dic[cnt] = a_dictionary.get(cnt) * 2
    return new_dic
