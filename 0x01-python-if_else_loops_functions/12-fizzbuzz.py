#!/usr/bin/python3


def fizzbuzz():
    str1 = "Fizz"
    str2 = "Buzz"
    str3 = "FizzBuzz"
    for cnt in range(1, 101):
        if cnt % 3 == 0 and cnt % 5 == 0:
            print("{:s} ".format(str3), end='')
        elif cnt % 3 == 0:
            print("{:s} ".format(str1), end='')
        elif cnt % 5 == 0:
            print("{:s} ".format(str2), end='')
        else:
            print("{:d} ".format(cnt), end='')
