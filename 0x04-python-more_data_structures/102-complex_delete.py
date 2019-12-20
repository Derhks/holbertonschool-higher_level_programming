#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = a_dictionary.copy()
    if value:
        for key in new_dic:
            if a_dictionary.get(key) == value:
                del a_dictionary[key]
        return a_dictionary
    return a_dictionary
