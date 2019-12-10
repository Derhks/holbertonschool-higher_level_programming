#!/usr/bin/python3


def islower(c):
    for cnt in range(ord('a'), ord('z') + 1):
        if ord(c) == cnt:
            return True
    return False
