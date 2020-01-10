#!/usr/bin/python3


class Square:
    pass

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
               raise ValueError("size must be >= 0")
            self.__size = size # Private instance attribute
        else:
            raise TypeError("size must be an integer")


    def area(self): # Public instance method
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
               raise ValueError("size must be >= 0")
            self.__size = value # Private instance attribute
        else:
            raise TypeError("size must be an integer")

        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        for itr in range(self.__size):
            for itr in range(self.__size):
                print("#", end='')
            print()
