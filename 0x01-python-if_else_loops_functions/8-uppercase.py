#!/usr/bin/python3


def uppercase(str):
    for cnt1 in str:
        cnt2 = ord(cnt1)
        if cnt2 >= 97 and cnt2 <= 122:
            str1 = chr(cnt2 - 32)
        else:
            str1 = chr(cnt2)
        print("{:s}".format(str1), end='')
    print()
