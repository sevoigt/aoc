"""
day 13
"""

import numpy as np


def find_matrix_symmetry(matrix, s1=-1):
    """
    Find symmetry in rows. Pass transposed matrix for symmetry in columns
    s1 is the previously found symmetry that is skipped
    """
    n = matrix.shape[0]

    for i in range(n-1):
        sym = True
        for k in range(min(i+1, n-i-1)):
            if (matrix[i-k, :] != matrix[i+k+1, :]).any():
                sym = False

        if sym and (i+1) != s1:
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
    s0_row = find_matrix_symmetry(i)
    s0_col = find_matrix_symmetry(i.transpose())

    found = False

    for j in range(i.shape[0]):
        for k in range(i.shape[1]):
            _blk = i.copy()
            _blk[j, k] = not _blk[j, k]

            s_row = find_matrix_symmetry(_blk, s0_row)
            s_col = find_matrix_symmetry(_blk.transpose(), s0_col)

            if s_row != -1:
                p2 += 100 * s_row
                found = True
                break

            if s_col != -1:
                p2 += s_col
                found = True
                break

        if found:
            break

print('result part 2:', p2)
