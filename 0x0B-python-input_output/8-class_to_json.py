#!/usr/bin/python3
"""The module defines Python class to
JSON function."""
def class_to_json(obj):
    """Return dictionary represenation of simple data structure."""
   return obj.__dict__
