#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    str = "Exception: Unknown format code 'd' for object of type 'str'"
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        print("{:s}".format(str), file=sys.stderr)
        return False
