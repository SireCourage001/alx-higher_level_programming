#!/usr/bin/python3


"""Computes the square value of all integers of a matrix using map"""
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda i: i ** 2, x)), matrix))
