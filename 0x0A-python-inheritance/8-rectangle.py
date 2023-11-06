#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent rectangle using BaseGeometry."""

    def ___init___(self, width, height):
        """Initialize a new rectangle

        Args:
            width (int): Width of the new Rectangle.
            height (int): Height of the new Rectangle.
            """

            self.integer_validator("width", height)
            self.__width = width
            self.integer_validator("height", height)
            self.__height = height
