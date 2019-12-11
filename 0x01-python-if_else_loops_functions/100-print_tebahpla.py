#!/usr/bin/python3

for cnt in range(122, 96, -1):
    if cnt % 2 == 0:
        str1 = chr(cnt)
    else:
        str1 = chr(cnt - 32)
    print("{:s}".format(str1), end='')
