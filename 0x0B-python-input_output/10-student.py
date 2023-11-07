#!/usr/bin/python3
"""The module defines a class Student."""

class Student:
    """Represent a Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
            """

            self.first_name = first_name
            self.last_name = last_name
            self.age = age

            def to_json(self, attrs=None):
        """Get a dictionary representation of Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
         a_dict = vars(self)
        if type(attrs) == list and all(isinstance(i, str) for i in attrs):
            new_dict = {}
            for key in filter(lambda key: key in a_dict, attrs):
                new_dict[key] = a_dict[key]
            return new_dict

        return a_dict
