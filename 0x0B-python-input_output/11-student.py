#!/usr/bin/python3
"""The modle defines a class Student."""


class Student:
    """Reprsent a Student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
            """

            self.first_name = first_name
            self.last_name = last_name
            self.age = age

            def to_json(self, attrs=None):
                """Get dictionary representation of student.

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

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            if k in vars(self):
                setattr(self, k, v)
