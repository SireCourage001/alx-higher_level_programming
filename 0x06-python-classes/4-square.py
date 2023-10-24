#!/usr/bin/python3
class square:
    def __init__(self, size=0):
        """Init the instance attribute and raise exception if error
        """
        self.__size = size

        @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2
