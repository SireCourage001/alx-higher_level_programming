#!/usr/bin/python3
"""This module defines aRectangle class.
"""
class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes Rectangle props
        """

        self.width = width
        self.height = height

    def __str__(self):
        """Returns informal str representation
        """

        if self._width == 0 or self._height == 0:
            return ''
         record_str = ''
         for i in range(self._width):
             for j in range(self._height):
                 record_str += '#'
                 record_str += '\n'
                 return record_str[:-1]


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value


    @property
    def height(self):
        return self._height


    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value


    def area(self):
        """Finds the area of Rectangle instance
        """
        return self._width * self._height

    def perimeter(self):

        if self._width == 0 or self._height == 0
        return 0
    return 2 * (self._width + self._height)

