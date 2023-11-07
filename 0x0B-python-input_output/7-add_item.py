#!/usr/bin/python3
"""The module add all arguments to a Python list and \ 
save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

        if __name__ == "__main__":
    from sys import argv
    from os import path

    filename = "add_item.json"
    a_list = []

    if path.exists(filename) and path.getsize(filename) > 0:
        a_list = load_from_json_file(filename)

    if len(argv) == 1:
        save_to_json_file(a_list, filename)
    else:
        a_list = a_list + argv[1:]
        save_to_json_file(a_list, filename)
