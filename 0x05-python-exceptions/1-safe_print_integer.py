#!/usr/bin/python3

try:
    def safe_print_integer(value):
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            return False
except ValueError:
    print("Sorry this value is not a integer")
