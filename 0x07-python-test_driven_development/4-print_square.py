#!/usr/bin/python3
"""Module for 4-print_square
"""

def print_square(size):
    """This function that prints a square with the character #

    Args:
    size(int): size of the square to print

    Raises:
        TypeError: if size is not and int
        ValueError: if size < 0
        """


        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        for _ in range(size):
            print('#' * size)
