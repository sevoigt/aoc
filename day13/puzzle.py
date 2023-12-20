"""
day 13
"""

import numpy as np


fid = open('input_min.txt')
blocks = fid.read()
blocks = blocks.replace('.', '0')
blocks = blocks.replace('#', '1')
blocks = blocks.split('\n\n')

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
pass