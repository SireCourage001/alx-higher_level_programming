#!/usr/bin/python3
"""Module for 101-locked_class
"""

class lockedClass:
    """Prevents user from dynamically creating a new instance attribute

    Only instance variable permitted is `first_name`
    """

    __slots___ = ["first_name"]

    def __init__(self, first_name=""):
        self.first_name = first_name
