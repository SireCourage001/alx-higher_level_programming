#!/usr/bin/python3
# 6-from_json_string.py
"""The module defines a JSON-to-object function."""
import json

def from_json_string(my_str):
    """Return Python object representation of a JSON str."""
    return json.loads(my_str)
