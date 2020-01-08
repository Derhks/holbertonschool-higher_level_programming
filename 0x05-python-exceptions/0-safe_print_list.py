#!/usr/bin/python3

try:
    def safe_print_list(my_list=[], x=0):
        cnt = 0
        for itr in my_list[0:x]:
            cnt += 1
            print('{}'.format(itr), end="")
        print()
        return cnt
except IndexError:
    print("Sorry that index doesn't exist")
