#!/usr/bin/python3
"""This module defines a file-writing function"""

def write_file(filename="", text=""):
    """Write a str to UTF8 text file.

    Args:
        filename (str): Name of the file to write.
        text (str): Text to write to the file.
    Returns:
            Number of charcters written.
            """

            with open(filename, "w", encoding="utf-8") as f:
                return f.write(text)
