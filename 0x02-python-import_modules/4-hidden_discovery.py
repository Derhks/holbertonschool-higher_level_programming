#!/usr/bin/python3

import hidden_4
for lst in dir(hidden_4):
    line = "__"
    if lst[:2] != line:
        print("{:s}".format(lst))
    else:
        continue
