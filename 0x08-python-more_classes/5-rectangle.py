#!/usr/bin/python3


class Rectangle:
    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height  # This is a private instance attribute
        self.__width = width  # This is a private instance attribute

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property  # getter
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):  # Public instance method
        return self.__width * self.__height

    def perimeter(self):  # Public instance method
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        string = ""

        if self.__width == 0 or self.__height == 0:
            return string
        for row in range(self.__height):
            for times in range(self.__width):
                string = string + "#"
            if row + 1 < self.__height:
                string = string + "\n"
        return string

    # This function return a string object(representation)
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    # This method is called when a object gets destroyed
    def __del__(self):
        print("Bye rectangle...")
