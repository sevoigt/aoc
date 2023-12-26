"""
day 13
"""

import numpy as np
import time


def find_symmetry(values):
    """
    Compare left and right value from starting point within
    array until either end of array is reached.
    """

    n = len(values)

    for i in range(n-1):
        sym = True
        for k in range(min(i+1, n-i-1)):
            if values[i-k] != values[i+k+1]:
                sym = False

        if sym:
            return i

    return -1


def find_matrix_symmetry(matrix):
    """
    Find symmetry in rows. Pass transposed matrix for symmetry in columns
    """
    n = matrix.shape[0]

    for i in range(n-1):
        sym = True
        for k in range(min(i+1, n-i-1)):
            if (matrix[i-k, :] != matrix[i+k+1, :]).any():
                sym = False

        if sym:
            return i+1

    return -1


fid = open('input.txt')
blocks = fid.read()
blocks = blocks.split('\n\n')
blocks = [np.array([list(i) for i in k.split('\n')]) == '.' for k in blocks]


# part 1
p1 = 0

for i in blocks:
    s_row = find_matrix_symmetry(i)
    s_col = find_matrix_symmetry(i.transpose())

    if s_row != -1:
        p1 += 100 * s_row

    if s_col != -1:
        p1 += s_col

print('result part 1:', p1)


# part 2
p2 = 0

for i in blocks:
    pass
