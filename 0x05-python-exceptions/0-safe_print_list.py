#!/usr/bin/python3

"""The function that prints x elements of a list."""
def safe_print_list(main_list =[], x=0):
    idx = 0
    for idx in range(x):
        try:
            print(main_list[idx], end="")
            idx += 1
            except IndexError:
                break
            print()
            return idx
