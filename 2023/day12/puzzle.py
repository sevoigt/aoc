"""
day 12

part 1 super ugly...

maybe better use binary arithmetic (translating ./# to 0/1)

"""

import numpy as np
import functools


def is_match(springs, counters):

    groups = list()
    n = 0

    for char in springs:

        if char == '#':
            n += 1
        elif char == '.' and n != 0:
            groups.append(n)
            n = 0

    # last char was a '#'
    if n != 0:
        groups.append(n)

    return groups == counters


def iter_variants(n):
    """
    0 = .
    1 = #
    """

    num = 0
    num_digits = len(bin(2**(n-1)).split('b')[1])

    while num < 2**n:
        num_bin = bin(num).split('b')[1]
        num_bin = (num_digits - len(num_bin)) * '0' + num_bin
        num_bin = num_bin.replace('0', '.')
        num_bin = num_bin.replace('1', '#')

        yield num_bin

        num += 1



fid = open("input.txt")
lines = fid.readlines()


total = 0

for line in lines:
    springs, groups = line.strip().split()
    groups = [int(i) for i in groups.split(',')]
    springs = list(springs)

    loc_unknowns = np.where(np.array(springs)=='?')[0]
    num_unknowns = len(loc_unknowns)

    n = 0

    for i in iter_variants((num_unknowns)):
        spring_var = springs.copy()

        for k, idx in enumerate(loc_unknowns):
            spring_var[idx] = i[k]

        spring_var = functools.reduce(lambda x, y: x+y, spring_var)
        #print(spring_var)

        if is_match(spring_var, groups):
            n += 1

    total += n
    #print(n)

print('result part 1:', total)

