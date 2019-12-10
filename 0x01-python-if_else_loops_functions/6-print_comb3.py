#!/usr/bin/python3

for cnt1 in range(10):
    for cnt2 in range(10):
        if cnt1 != cnt2 and cnt1 < cnt2 and cnt1 < 8:
            print("{:d}{:d}, ".format(cnt1, cnt2), end='')
        elif cnt1 == 8 and cnt2 == 9:
            print("{:d}{:d}".format(cnt1, cnt2))
