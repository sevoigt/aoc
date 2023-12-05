"""
day 5

numbers are too large to use a mapping dict -> out of memory
"""


def get_numbers(line):
    """
    Get list of integer numbers from string. Numbers must be
    separated by spaces.
    """
    return [int(i) for i in line.split() if i.isdigit()]


def within(value, min_val, max_val):
    return min_val <= value <= max_val


def convert(block, value):
    """
    yeah its inefficient...but ok for part 1
    """
    lines = block.split('\n')

    for line in lines[1:]:
        dest, src, num = get_numbers(line)
        if within(value, src, src+num-1):
            value = dest + (value-src)
            break

    return value


def preprocess_block(block):
    """
    Preprocessing / caching to avoid parsing the block for each seed
    block is described by start, end and offset between src and dest
    """
    res = list()

    lines = block.split('\n')

    for line in lines[1:]:
        dest, src, num = get_numbers(line)
        res.append((src, src+num-1, dest-src))

    return res


def convert_pp(block, value):
    """
    Use cached block data
    """
    for line in block:
        if within(value, line[0], line[1]):
            value += line[2]
            break

    return value


fid = open("input.txt")
c = fid.read()

blocks = c.split('\n\n')


# part 1
seeds = get_numbers(blocks[0])

locations = []

for i in seeds:
    for k in blocks[1:]:
        i = convert(k, i)

    locations.append(i)

print("result part 1:", min(locations))


# part 2
ranges = list(zip(seeds[:-1], seeds[1:]))[::2]
block_data = [preprocess_block(i) for i in blocks[1:]]

smallest = 1e12

'''
for i in ranges:
    for j in range(i[0], i[0]+i[1]):
        for k in block_data:
            j = convert_pp(k, j)

        smallest = min(j, smallest)
'''


# brute force....

from joblib import Parallel, delayed
import time

def process(i):
    smallest = 1e12
    start = time.time()

    for j in range(i[0], i[0]+i[1]):
        for k in block_data:
            j = convert_pp(k, j)

        smallest = min(j, smallest)

    print('completed range', i, 'in', time.time()-start, 's')
    return smallest

results = Parallel(n_jobs=10)(delayed(process)(i) for i in ranges)

print("result part 2:", min(results))
