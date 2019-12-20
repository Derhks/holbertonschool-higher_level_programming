#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for cnt in range(len(str)):
        if cnt != n:
            new_str += str[cnt]
    return new_str
