"""
2024/day09
"""

from aoc.util import read_whole_file

def relax(inp):
    """
    Expand the description string into blocks and spaces
    Spaces are represented as -1 in the output array
    """
    ret = list()
    is_data = True
    n = 0
    for i in inp:
        if is_data:
            ret.extend(int(i)*[n,])
            n += 1
        else:
            ret.extend(int(i)*[-1,])
        is_data = not is_data

    return ret


def compress_and_checksum(inp):
    """
    Move the blocks to the most-left free position
    and calculate the checksum in one run
    """

    bw_idx = -1
    cs = 0
    n = len(inp)

    for i in range(n):

        if inp[i] == -1:
            while inp[bw_idx] == -1:
                bw_idx -= 1

            # bw_idx is negative!
            if i >= n + bw_idx:
                break

            inp[i] = inp[bw_idx]
            inp[bw_idx] = -1

        cs += i*inp[i]

    return inp, cs


data = read_whole_file('input_min.txt').strip()

# part 1
r1 = relax(data)
r2, ret1 = compress_and_checksum(r1)
print(ret1)

# part 2
