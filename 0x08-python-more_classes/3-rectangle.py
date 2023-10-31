#!/usr/bin/python3
"""This module defines aRectangle class.
"""
class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes Rectangle props
        """

        Rectangle.checkWidth(width)
        self.width = width
        Rectangle.checkHeight(height)
        self.height = height

    def __str__(self):
        """Returns informal str representation
        """

        if self._width == 0 or self._height == 0:
            return rectangle

        lines = ['#' * self.width for _ in range(self.height)]
        rectangle = '\n'.join(lines)
        return rectangle

    @staticmethod
    def checkWidth(width):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        


    @staticmethod
    def checkHeight(height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        

    @property
    def width(self):
        """int: The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.checkWidth(value)
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.checkHeight(value)
        self.__height = value

    def area(self):
        """Returns the rectangle area in a given instance"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle in a given instance"""
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)
