#!/usr/bin/python3

"""Module for 3-say_my_name
"""

def say_my_name(first_name, last_name=""):
    """Print out first_and_last name

    Args:
        first_name(string): First name
        last_name(string): Last name

    Raises:
        TypeError: when first_name or last_name is not a string

    Example:
        >>>say_my_name("Sire, Courage")
        My name is Sire Courage
        """
        

    #check the type of Args

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
