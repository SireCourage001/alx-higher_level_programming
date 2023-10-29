#!/usr/bin/python3

"""MOdule for 100-matrix_mul
"""
def matrix_mul(m_a, m_b):

"""Multiplies two matrix and returns the new_matrixing matrix

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The product of `m_a` and `m_b`.

    Raises:
        TypeError: If `m_a` or `m_b` is not a list,
            or if `m_a` or `m_b` is not a list of lists,
            or if one element of `m_a` or `m_b` is not an integer or a float,
            or if `m_a` or `m_b` is not a rectangle.
        ValueError: If `m_a` or `m_b` is empty,
            or if `m_a` and `m_b` can't be multiplied.

        Example:
            >>> matrix_mul([[3], [5]], [[2, 3]])
            [[6, 9], [10, 15]]
            """

            if m_a is None and m_b is None:
                return None

            if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")


    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")



if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")


    if not all(isinstance(n, (int, float)) for row in m_a for n in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(n, (int, float)) for row in m_b for n in row):
        raise TypeError("m_b should contain only integers or floats")



row_lens_in_a = [len(row) for row in m_a]
    if not all(curr_len == row_lens_in_a[0] for curr_len in row_lens_in_a):
        raise TypeError("each row of m_a must be of the same size")


    row_lens_in_b = [len(row) for row in m_b]
    if not all(curr_len == row_lens_in_b[0] for curr_len in row_lens_in_b):
        raise TypeError("each row of m_b must be of the same size")



if row_lens_in_a[0] != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")



 new_matrix = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

for i in range(len(new_matrix)):

    for j in range(len(new_matrix[0])):

        for k in range(len(m_b)):

            new_matrix[i][j] += m_a[i][k] * m_b[k][j]
            
            return new_matrix
