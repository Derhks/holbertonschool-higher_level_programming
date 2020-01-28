#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """This method initialize all the instance"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This method return
        [Square] (<id>) <x>/<y> - <size>"""

        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(__class__.__name__,
                                                     self.id, self.x, self.y,
                                                     self.width)

    @property
    def size(self):
        """This is the getter"""

        return self.width
        return self.height

    @size.setter
    def size(self, value):
        """This is the setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """This method update the attribute of the class"""

        my_list = ["id", "size", "x", "y"]
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
        representation of a Square"""

        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
