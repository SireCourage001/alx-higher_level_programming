#!/usr/bin/python3

"""This module defines a Rectangle class
"""
class Rectangle:
    """A class Rectangle that defines the width & height
    """
    def __init__(self, width=0, height=0):
        """Initializes the width and height of a Rectangle
        """
       Rectangle.checkWidth(width)
       self.width = width
       Rectangle.checkHeight(height)
       self.height = height

    @property
    def __repr__(self):
        return f"Rectangle(width={self.__width}, height={self.__height})"

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
