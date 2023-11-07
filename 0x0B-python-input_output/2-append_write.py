#!/usr/bin/python3
"""This module defines file-appending function"""

def append_write(filename="", text=""):
    """Appends str to the end of UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
            Number of characters append.
            """

            with open(filename, "a", encoding="utf-8") as f:
                return f.write(text)
