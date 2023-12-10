"""
day 10
"""

import numpy as np


directions = {'7' : (-1, -1),
              'F' : (-1,  1),
              '-' : ( 0,  1),
              '|' : (-1,  0),
              'L' : (),
              'J' : ()}


fid = open("input_min.txt")
lines = fid.readlines()

grid = np.array([list(i) for i in lines])
start = [int(i[0]) for i in np.where(grid == 'S')]

