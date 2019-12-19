#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set3 = [cnt for cnt in set_1 if cnt not in set_2]
    set3 += [cnt for cnt in set_2 if cnt not in set_1]
    return set3
