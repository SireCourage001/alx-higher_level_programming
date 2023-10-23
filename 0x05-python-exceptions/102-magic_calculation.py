#!/usr/bin/env python3

"""Magic_calculation"""
def magic_calculation(a, b):
    newVal  = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")

            newVal += a ** b / i
        except Exception:
            newVal = a + b
            break
    return newVal
