#!/usr/bin/python3
"""Sum all unique int in a list (once for each int)."""
def uniq_add(my_list=[]):
    result = 0
    for x in set(my_list):
        result += x
        return (result)

