#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for cnt in matrix:
        for cnt1 in cnt:
            print("{:d} ".format(cnt1), end="")
            if cnt1 != cnt[-1]:
                print(end=' ')
        print()
