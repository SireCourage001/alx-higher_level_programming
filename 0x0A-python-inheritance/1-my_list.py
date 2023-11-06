#!/usr/bin/python3
"""Defines inherited list class MyLists.
``1-my_list`` module."""

class MyList(list):
    """Executes sorted printing for built-in list class."""

    def print_sorted(self):
        """Print a list in ascending order."""

        newList = self[:]
        newList.sort()
        print("{}".format(newList))
