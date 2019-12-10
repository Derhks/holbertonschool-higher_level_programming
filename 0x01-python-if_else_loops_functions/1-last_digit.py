#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = "and is greater than 5"
str3 = "and is less than 6 and not 0"

if number > 0:
    var = number % 10

    if var > 5:
        print("{:s} {:d} is {:d} {:s}".format(str1, number, var, str2))
    elif var < 6 and var != 0:
        print("{:s} {:d} is {:d} {:s}".format(str1, number, var, str3))
    else:
        print("{:s} {:d} is {:d} and is 0".format(str1, number, var))
elif number < 0:
    var = ((number * -1) % 10) * -1

    if var > 5:
        print("{:s} {:d} is {:d} {:s}".format(str1, number, var, str2))
    elif var < 6 and var != 0:
        print("{:s} {:d} is {:d} {:s}".format(str1, number, var, str3))
    else:
        print("{:s} {:d} is {:d} and is 0".format(str1, number, var))
