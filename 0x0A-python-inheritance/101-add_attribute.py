#!/usr/bin/python3
"""The ``101-add_attribute`` module
Defines a function that adds attributes to objects"""

def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible.

    Args:
        obj: Object to add the attribute to.
        attr_name: Name of the attribute to add.
        attr_value: Value of the attribute to add.

    Raises:
    TypeError: If new attribute could not be added.
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    if hasattr(obj, '__slots__') and attr_name not in obj.__slots__:
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
