#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename) as file:
        cnt = len(open(filename).readlines())
        cnt2 = 1
        if nb_lines <= 0 or nb_lines >= cnt:
            print(file.read(), end="")
        for line in file:
            if cnt2 <= nb_lines:
                print(line, end="")
            cnt2 += 1
