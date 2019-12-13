#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    for lst in dir(hidden_4):
        line = "__"
        if lst[:2] != line:
            print("{:s}".format(lst))
        else:
            continue
