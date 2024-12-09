"""
2024/day06
"""

import numpy as np

from aoc.util import read_grid_array

def is_outside(position, map):
    num_rows, num_cols = map.shape
    row = position[0]
    col = position[1]
    return row < 0 or col < 0 or row > (num_rows - 1) or col > (num_cols - 1)

map = read_grid_array("input.txt")

# part 1
visited = np.zeros(map.shape, dtype=np.int64)

directions = [
    np.array([-1,  0]), # up
    np.array([ 0,  1]), # right
    np.array([ 1,  0]), # down
    np.array([ 0, -1])] # left

# init
step_idx = 0
step = directions[step_idx]         # direction of next step
pos = np.where(map == '^')          # start position - start is always ^ ?
pos = np.array(pos).flatten()

i = 0

while True:
    visited[pos[0], pos[1]] = 1
    new_pos = pos + step

    if is_outside(new_pos, map):
        break

    if map[new_pos[0], new_pos[1]] == '#':
        step_idx = divmod(step_idx + 1, 4)[1]
        step = directions[step_idx]
    else:
        pos = new_pos


print(np.sum(visited))


# part 2 - brute force, just block each position on the known path and
# check if it ends up in a loop, not clever and slow as hell


def is_loop(start, map, block_row, block_col):
    """
    Walk through the map with an additional obstacle at (block_row, block_col)
    and check if it ends up in a loop or not
    We now store the direction at every position we visit to check
    if we were already there and heading in the same direction => loop

    Problem: Loop detection does not work with crossings, i.e. when we pass
    the same position multiple times from different directions

    Ugly workaround: we cannot visit more positions than we have in total on
    the map, thus just exit after n_max steps
    """

    vis = np.zeros(map.shape, dtype=np.int64) - 1

    step_idx = 0
    step = directions[step_idx]         # direction of next step
    pos = start

    n = 0
    n_max = map.shape[0] * map.shape[1]

    while True:

        if (vis[pos[0], pos[1]] == step_idx) or n > n_max:
            return True

        vis[pos[0], pos[1]] = step_idx
        new_pos = pos + step

        if is_outside(new_pos, map):
           return False

        if (map[new_pos[0], new_pos[1]] == '#') or \
           (new_pos[0] == block_row and new_pos[1] == block_col):
            step_idx = divmod(step_idx + 1, 4)[1]
            step = directions[step_idx]
        else:
            pos = new_pos

        n += 1

res2 = 0

pos = np.where(map == '^')          # start position
pos = np.array(pos).flatten()

for i in range(map.shape[0]):
    for k in range(map.shape[1]):

        # do not put obstacle on start position
        if i == pos[0] and k == pos[1]:
            continue

        if visited[i, k] == 1:
            res2 += int(is_loop(pos, map, i, k))

print(res2)
