#!/usr/bin/python3
for cnt in range(0, 100):
    if cnt != 99:
        print("{:02d}, ".format(cnt), end='')
    else:
        print("{:d}".format(cnt))
