"""
2024/day04
"""

def num_xmas(line):
    return line.count('XMAS') + line.count('SAMX')

def transpose(grid):
    """
    grid is a list of strings, where the string-index is one dimension
    and the list-index is the other dimension of the grid
    """

    # careful: explicitly create lists to get unique instances
    transposed = []
    for i in range(len(grid[0])):
        transposed.append([])

    for line in grid:
        for idx, char in enumerate(line):
            transposed[idx].append(char)

    # flatten inner lists to string again
    transposed = [''.join(i) for i in transposed]
    return transposed


def pivot(grid, reverse):
    """
    extract the diagonals
    """

    transposed = []
    for i in range(len(grid[0]) + len(grid) - 1):
        transposed.append([])

    for idx_row, line in enumerate(grid):
        _l = line[::-1] if reverse else line
        for idx_col, char in enumerate(_l):
            transposed[idx_row+idx_col].append(char)

    # flatten inner lists to string again
    transposed = [''.join(i) for i in transposed]
    return transposed


with open('input.txt', 'r') as fid:
    rows = fid.readlines()
    rows = [i.strip() for i in rows]

num_rows = len(rows)
num_cols = len(rows[0].strip())


# part 1
res1 = 0

# horizontal
for i in rows:
    res1 += num_xmas(i)

# vertical
cols = transpose(rows)
for i in cols:
    res1 += num_xmas(i)

# diagonal both ways
diag1 = pivot(cols, True)
for i in diag1:
    res1 += num_xmas(i)

diag2 = pivot(cols, False)
for i in diag2:
    res1 += num_xmas(i)

print(res1)


# part 2
res2 = 0
cross = ('MAS', 'SAM')
grid = rows

for idx_row in range(num_rows-2):
    for idx_col in range(num_cols-2):

        d1 = grid[idx_row][idx_col] + grid[idx_row+1][idx_col+1] + grid[idx_row+2][idx_col+2]
        d2 = grid[idx_row+2][idx_col] + grid[idx_row+1][idx_col+1] + grid[idx_row][idx_col+2]

        if d1 in cross and d2 in cross:
            res2 += 1

print(res2)
