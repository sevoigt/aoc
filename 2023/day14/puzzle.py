"""
day 14
"""

import numpy as np


def tilt(matrix):
    """
    Roll the rocks north
    """

    for i in range(matrix.shape[0]):
        for k in range(matrix.shape[1]):

            if matrix[i, k] == 'O':

                for j in range(i-1, -1, -1):
                    up = matrix[j, k]

                    if up != '.':
                        matrix[i, k] = '.'
                        matrix[j+1, k] = 'O'
                        break

                    if up == '.' and j == 0:
                        matrix[i, k] = '.'
                        matrix[j, k] = 'O'
                        break
    return matrix


def calc_score(matrix):
    score = 0
    num_rows = matrix.shape[0]

    for i in range(num_rows):
        score += list(matrix[i, :]).count('O') * (num_rows - i)

    return score


def rot_right(matrix):
    """
    Spinning goes counterclockwise but we tilt always north
    and rotate the grid clockwise instead
    """
    return np.rot90(matrix, k=1, axes=(1, 0))


def spin(matrix):
    """
    Full spin in all directions, counterclockwise (N-W-S-E)
    """

    for i in range(4):
        matrix = tilt(matrix)
        matrix = rot_right(matrix)

    return matrix


fid = open('input.txt')
grid = fid.read()

grid = np.array([list(i) for i in grid.split('\n')])
#print(grid)

# part 1
grid = tilt(grid)
p1 = calc_score(grid)

#print()
#print(grid)
print('result part 1:', p1)


# part 2
scores = list()
for i in range(15):
    grid = spin(grid)

    score = calc_score(grid)

    #if score in scores:
        #print(i)
        #break

    scores.append(score)


# manual pattern recognition (scores repeat after n spins)
# p0 = offset, number of spins until pattern begins
# pp = score pattern
# for example input_min:
p0 = 2
pp = [69, 69, 65, 64, 65, 63, 68]

# for actual input
p0 = 92
pp = [96297, 96314, 96325, 96333, 96344, 96345, 96340, 96317, 96293]

p2 = pp[(1000000000-p0) % len(pp) - 1]
print('result part 2:', p2)
