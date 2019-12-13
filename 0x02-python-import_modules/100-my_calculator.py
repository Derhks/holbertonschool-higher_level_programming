#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) == 4:
        num1 = int(argv[1])
        num2 = int(argv[3])
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(num1, num2, num1 + num2))
        exit(0)
    elif argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(num1, num2, num1 - num2))
        exit(0)
    elif argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(num1, num2, num1 * num2))
        exit(0)
    elif argv[2] == '/':
        print("{:d} / {:d} = {:.2f}".format(num1, num2, num1 / num2))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
