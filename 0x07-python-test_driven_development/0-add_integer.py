#!/usr/bin/python3

"""0-add_integer
The function add_integer and returns the sum of two int.
"""
def add_integer(a, b=98):
    """add_two_integers"""

    if type(a) not in [int, float]:
        raise TypeError ("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError ("b must be an integer")

    return int(a) + int(b)
