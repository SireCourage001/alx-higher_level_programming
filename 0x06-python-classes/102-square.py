#!/usr/bin/python3
class Square:
    def __init__(self, size=0):

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

    def __eq__(self, secArg):
        """checks for equality"""
        if isinstance(secArg, Square):
            return (self.__size == secArg.__size)
        return NotImplemented

    def __ne__(self, secArg):
        
        if isinstance(secArg, Square):
            return (self.__size != secArg.__size)
        return NotImplemented

    def __gt__(self, secArg):
        
        if isinstance(secArg, Square):
            return (self.__size > secArg.__size)
        return NotImplemented

    def __ge__(self, secArg):
        """Checks if self >= secArg"""
        if isinstance(secArg, Square):
            return self.__size >= secArg.__size
        return NotImplemented

    def __lt__(self, secArg):
        """Checks if self < secArg"""
        if isinstance(secArg, Square):
            return self.__size < secArg.__size
        return NotImplemented

    def __le__(self, secArg):
        """Checks if self <= secArg"""
        if isinstance(secArg, Square):
            return self.__size <= secArg.__size
        return NotImplemented
