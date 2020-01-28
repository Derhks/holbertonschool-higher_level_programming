#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """This is the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This method initialize all the instance"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.y = y

        super().__init__(id)

    @property
    def width(self):
        """This is getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """This is setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """This is getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """This is setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """This is getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """This is setter"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """This is getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """This is setter"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """This method return the area"""

        return self.width * self.height

    def display(self):
        """This method print a rectangle using the symbol #"""

        for itr_1 in range(self.y):
            print()
        for itr_2 in range(self.height):
            for itr_3 in range(self.x):
                print(" ", end="")
            for itr_4 in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """This method return
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""

        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(__class__.__name__,
                                                          self.id, self.x,
                                                          self.y, self.width,
                                                          self.height)

    def update(self, *args, **kwargs):
        """This method update the attribute of the class"""

        my_list = ["id", "width", "height", "x", "y"]
        itr_1 = 0
        if args is not None and len(args) > 0:
            for itr_2 in my_list:
                setattr(self, itr_2, args[itr_1])
                if itr_1 < len(args) - 1:
                    itr_1 += 1
                else:
                    break
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This method returns the dictionary
        representation of a Rectangle"""

        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
