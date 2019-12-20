#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_sum = 0
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string:
        for roman in roman_string:
            for r_d in roman_d:
                if roman == r_d:
                    roman_sum += roman_d.get(r_d)
        return roman_sum
    return 0
