#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """ Check if obj is an instance or inherited instance of a class.

    Args:
        obj (any): Obj to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
        """

        return  isinstance(obj, a_class)
