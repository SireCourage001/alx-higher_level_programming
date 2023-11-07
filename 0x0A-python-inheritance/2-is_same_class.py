#!/usr/bin/python3
"""Defines class-checking function.
``2-is_same_class`` module"""

def is_same_class(obj, a_class):
    """Check if object is exactly an instance of a given class.

    Args: 
        obj (any): Obj to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - true.
        Otherwise - False.
        """
        return type(obj) ==  a_class
