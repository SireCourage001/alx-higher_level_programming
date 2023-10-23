#!/usr/bin/python3

"""The function divides 2 integers and prints the result."""

def safe_print_division(a, b):
    try:
        newVal = a / b
        except ZeroDivisionError:
            newVal = None
        finally:
            print("Inside result: {}".format(newVal))
            return newVal
