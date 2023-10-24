#!/usr/bin/python3
class square:
    """This class defines a square by private & public instance attribute;
    raises exception if error"""
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
        """The Method that returns the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using `#` signs"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
