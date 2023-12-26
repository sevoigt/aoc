"""
day 13
"""

import numpy as np


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


fid = open('input_min.txt')
blocks = fid.read()
blocks = blocks.replace('.', '0')
blocks = blocks.replace('#', '1')
blocks = blocks.split('\n\n')


# part 1 - interpret rows and columns as binary numbers

# number representation of the rows within a block
rows = [np.array([eval(f'0b{k}') for k in i.split('\n')]) for i in blocks]

# numbers for columns
cols = list()

for blk in blocks:
    n_rows = blk.count('\n')+1
    n_cols = int((len(blk)-n_rows+1)/n_rows)
    blk_cols = [0] * n_cols

    lines = blk.split('\n')

    for i in range(n_cols):
        for k, line in enumerate(lines):
            blk_cols[i] |= int(line[i]) << k

    cols.append(np.array(blk_cols))


# now find symmetry
p1 = 0

for i in rows:
    s = find_symmetry(i)
    if s != -1:
        p1 += 100 * (s+1)

for i in cols:
    s = find_symmetry(i)
    if s != -1:
        p1 += s+1

print('result part 1:', p1)


# part 2 - meh, need a matrix for each block to make iteration easier
ba = [np.array([list(i) for i in k.split('\n')]) for k in blocks]
