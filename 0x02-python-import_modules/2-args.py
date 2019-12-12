#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
        for cnt in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(cnt, sys.argv[cnt]))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for cnt in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(cnt, sys.argv[cnt]))
