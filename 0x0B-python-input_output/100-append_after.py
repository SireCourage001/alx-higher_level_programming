#!/usr/bin/python3
"""The module for '100-append_after.py'"""

def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for within the file.
        new_string (str): String to insert.
        """

        if not search_string or not new_string:
            return

        with open(filename, 'r+', encoding="utf-8") as f:
        file_list = f.readlines()

        with open(filename, 'w') as fo:
        file_str = ""
        for line in file_list:
            file_str += line
            if search_string in line:
                file_str += new_string
        fo.write(file_str)
