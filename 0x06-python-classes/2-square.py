#!/usr/bin/python3#!
"""This module defines a class square"""

class square:
    """This class contains a private instance attribute `__size`"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
