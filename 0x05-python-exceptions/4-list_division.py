#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for cnt in range(list_length):
        try:
            div = (my_list_1[cnt] / my_list_2[cnt])
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div)
            div = 0
    return new_list
