#!/usr/bin/python3
"""Defeines class-checking function."""
def is_same_class(obj, a_class):
    """Check if object is exactly an instance of a given class.

    Args: 
        obj (any): Obj to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - true.
        Otherwise - False.
        """
        if type(obj) == a_class:
            return True
        return False
