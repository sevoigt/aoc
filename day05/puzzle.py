"""
day 5

numbers are too large to use a dict -> out of memory
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
    yeah its inefficient...
    """
    lines = block.split('\n')
    
    for line in lines[1:]:
        dest, src, num = get_numbers(line)
        if within(value, src, src+num-1):
            value = dest + (value-src)
            break
    
    return value


def create_dict(block):
    """
    Create a mapping dictionary for a block
    -> nice idea but runs out of memory 
    """
    d = dict()

    lines = block.split('\n')
    for line in lines[1:]:
        dest, src, num = get_numbers(line)
        d.update(zip(range(src, src+num), range(dest, dest+num)))

    return d

    


fid = open("input.txt")
c = fid.read()

blocks = c.split('\n\n')

seeds = get_numbers(blocks[0])

#block_dicts = [create_dict(i) for i in blocks[1:]]
locations = []

for i in seeds:

    # out of memory
    #for k in block_dicts:
    #    i = k[i] if i in k else i
    for k in blocks[1:]:
        i = convert(k, i)
    
    locations.append(i)

print("result part 1:", min(locations))