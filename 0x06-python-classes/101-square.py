#!/usr/bin/python3
class Square:
     def __init__(self, size=0, position=(0, 0)):

         Square.check_size(size)
         self.__size = size

         Square.check_pos(position)
        self.__position = position

        @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):
        Square.check_size(value)
        self.__size = value

        def area(self):

            return self.__size ** 2

        @property
    def position(self):

        return self.__position

    @position.setter
    def position(self, value):
        Square.check_pos(value)
        self.__position = value

    def my_print(self):
        """Prints the sqr using `#` signs"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns the sqr  made using `#` signs"""

        sq_str = ""
        if self.__size == 0:
            return sq_str
        else:
            x, y = self.__position

            for _ in range(y):
                sq_str = sq_str + "\n"

            for _ in range(self.__size):
                if x:
                    sq_str = sq_str + (' ' * x)
                sq_str += ('#' * self.__size) + '\n'
            sq_str = sq_str[:-1]
            return sq_str

    @staticmethod
    def check_size(size):

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @staticmethod
    def check_pos(position):

        if type(position) != tuple or len(position) != 2 \
            or type(position[0]) != int or type(position[1]) != int \
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
