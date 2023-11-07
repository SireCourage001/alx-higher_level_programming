#!/usr/bin/python3
"""The module defines a JSON file-reading func."""
import json

def load_from_json_file(filename):
    """Creates Python object from JSON file."""
    with open(filename) as f:
        return json.load(f)
