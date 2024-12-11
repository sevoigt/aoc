"""
2024/day07
"""

import itertools

def get_op_result(numbers, op):
    """
    op = tuple of operator characters
    """
    res = numbers[0]

    for idx, i in enumerate(op):
        if i == '+':
            res += numbers[idx+1]
        elif i == '*':
            res *= numbers[idx+1]
        elif i == '|':
            res = int(str(res)+str(numbers[idx+1]))
        else:
            raise ValueError('Unknown token: ', i)

    return res


results = list()
numbers = list()

with open('input.txt', 'r') as fid:
    for i in fid:
        _r, _o = i.split(':')
        results.append(int(_r))
        numbers.append([int(i) for i in _o.strip().split(' ')])


# part 1
res1 = 0
ok = set()

for i in range(len(results)):
    n = len(numbers[i])

    for ops in itertools.product('+*', repeat=n-1):
        if get_op_result(numbers[i], ops) == results[i]:
            res1 += results[i]
            ok.add(i)
            break

print(res1)


# part 2
# the indices that need to be reassessed
not_ok = set(range(len(results))).difference(ok)
res2 = 0

for i in not_ok:
    n = len(numbers[i])

    for ops in itertools.product('+*|', repeat=n-1):
        if get_op_result(numbers[i], ops) == results[i]:
            res2+= results[i]
            break

print(res1 + res2)
