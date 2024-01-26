#!/usr/bin/python3

"""This module contains a fxn to find peak in an unsorted list of integers"""
def find_peak(list_of_integers):
"""
It returns peak value in the list of int specified by 'list_of_int'
"""
if not list of integers:
    return None

low = 0
high = len(list_of_integers) - 1

while low < high:
    mid = (low + high) // 2
    if list_of_integers[mid] < list_of_integers[mid + 1]:
	low = mid + 1
    else:
	high = mid
   
    return list_of_integers[low]



"""Complexity: 0(log(n))"""

