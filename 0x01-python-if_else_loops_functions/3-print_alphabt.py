#!/usr/bin/python3

for cnt in range(97, 123):
    if cnt < 101 or cnt > 101 and cnt < 113 or cnt > 113:
        print("{:s}".format(chr(cnt)), end='')
