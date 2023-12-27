"""
day 14
"""

import numpy as np


fid = open('input_min.txt')
grid = fid.read()

grid = np.array([list(i) for i in grid.split('\n')])
print(grid)

# part 1
for i in range(1, grid.shape[0]):
    for k in range(grid.shape[1]):

        if grid[i, k] == 'O':
            for j in range(i-1, -1, -1):
                up = grid[j, k]

                if up != '.':
                    grid[j+1, k] = 'O'

                    if j != i:
                        grid[i, k] = '.'

                    break

        else:
            continue

print()
print(grid)
