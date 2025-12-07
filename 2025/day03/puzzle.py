"""
2025/day03
"""


def find_first(bat):
    first = max(bat)
    first_pos = bat.find(first)

    if first_pos == len(bat) - 1:
        first = max(bat[:-1])
        first_pos = bat.find(first)

    second = max(bat[first_pos+1:])
    return int(f'{first}{second}')


def find_second(start, res, n):
    #print(start)
    if n == 0:
        print(start, res)
        return res
    else:
        search_area = start[:-n]
        digit = max(search_area)
        res += digit
        idx = len(search_area) - search_area[::-1].find(digit)
        #print(res)
        return find_second(start[idx:], res, n-1)
    #return res


joltage_1 = 0
joltage_2 = 0


with open("input_min.txt") as f:
    for i in f:
        joltage_1 += find_first(i.strip())
        j2 = int(find_second(i.strip(), '', 12))
        print(j2)
        joltage_2 += j2


print(f'part 1: {joltage_1}')
print(f'part 2: {joltage_2}')
