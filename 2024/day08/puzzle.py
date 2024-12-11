"""
2024/day08
"""

import itertools
import numpy as np

from aoc.util import read_grid_array, pos_in_grid


map = read_grid_array('input.txt')
n_rows, n_cols = map.shape

# part 1
# find all distinct antenna identifiers and collect
# all coordinates of a type of antennas
res1 = set()
antennas = dict()

for i in range(n_rows):
    for k in range(n_cols):
        key = str(map[i,k])
        if key != '.':
            pos = np.array([i,k])
            if key in antennas:
                _l = antennas[key]
                _l.append(pos)
                antennas[key] = _l
            else:
                antennas[key] = [pos,]

# mix all pairs of antennas within the set
# calculate positions of antinodes from distance and slope
# of two antenna points and check if they are on the map
for ants in antennas.values():
    for a, b in itertools.combinations(ants, 2):
        #print(a, b)
        delta = b - a
        n1 = a - delta
        n2 = b + delta
        #print(n1, n2)

        if pos_in_grid(map.shape, n1):
            res1.add(tuple(n1))
        if pos_in_grid(map.shape, n2):
            res1.add(tuple(n2))

print(len(res1))
