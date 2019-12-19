#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if cnt == search else cnt for cnt in my_list]
    return new_list
