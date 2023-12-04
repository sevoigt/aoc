"""
day 4
"""


def get_num_wins(line):
    win_nums, my_nums = line.split(':')[1].split('|')

    win_nums = set([int(i) for i in win_nums.split(' ') if i])
    my_nums = set([int(i) for i in my_nums.split(' ') if i])

    return len(set.intersection(win_nums, my_nums))


def get_num_cards(lines, start, stop):
    n = 0

    for i in range(start, stop):
        n += 1 + get_num_cards(lines, i+1, i+1+get_num_wins(lines[i]))

    return n



fid = open('input.txt')
lines = fid.readlines()



total = sum([int(2**(get_num_wins(line)-1)) for line in lines])
print("result part 1:", total)


cards = get_num_cards(lines, 0, len(lines))
print("result part 2:", cards)
