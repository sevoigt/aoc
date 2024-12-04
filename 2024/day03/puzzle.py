"""
2024/day03
"""

import re

def product(mul_str):
    """
    Parse a mul(x,y) statement and return the product of the two factors
    """
    x, y = mul_str[4:-1].split(',')
    return int(x) * int(y)


mul = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
s = re.compile(mul)

# part 1
with open('input_min1.txt', 'r') as fid:
    source = fid.read()

res1 = sum([product(i) for i in s.findall(source)])
print(res1)


# part 2
with open('input.txt', 'r') as fid:
    source2 = fid.read()

dont = r'don\'t\(\)'
do = r'do\(\)'

t = f'({mul}|{dont}|{do})'
s2 = re.compile(t)

matches2 = s2.finditer(source2)

res2 = 0
active = True

for i in matches2:
    txt = i.group()

    if txt.startswith('do('):
        active = True
    elif txt.startswith('don'):
        active = False
    elif txt.startswith('mul') and active:
        res2 += product(txt)

print(res2)
