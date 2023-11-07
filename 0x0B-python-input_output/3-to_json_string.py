#!/usr/bin/python3
"""This module defines str to JSON function."""
import json

def to_json_string(my_obj):
    """Returns JSON representation of a str object."""
    return json.dumps(my_obj)
