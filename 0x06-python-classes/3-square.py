#!/usr/bin/python3


class Square:
    pass

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size  # Private instance attribute
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size
