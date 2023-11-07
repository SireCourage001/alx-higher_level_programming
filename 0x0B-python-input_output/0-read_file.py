#!/usr/bin/python

"""This module defines a text file-reading function."""

def read_file(filename=""):
    """Print contents of UTF8 text file to STDOUT."""
    
    if not filename:
        return
    with open(filename, 'r' encoding="utf-8") as f:
        print(f.read(), end="")
