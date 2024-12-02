"""
2024/day02
"""

import numpy as np

def is_report_safe(levels: np.ndarray):
    deltas = levels[1:] - levels[:-1]
    abs_deltas = np.abs(deltas)
    return ((deltas < 0).all() or (deltas > 0).all()) and \
      (abs_deltas > 0).all() and (abs_deltas < 4).all()


def is_report_damped_safe(levels: np.ndarray):
    ok = 0

    for i in range(len(levels)):
        slice = np.hstack((levels[:i], levels[i+1:]))
        if is_report_safe(slice):
            ok += 1

    return ok > 0


with open('input.txt', 'r') as fid:
    reports = fid.readlines()

res1 = 0
res2 = 0

for i, r in enumerate(reports):
    levels = np.array(r.strip().split(), dtype=np.int64)

    # part 1
    if is_report_safe(levels):
        #print('s', i, levels)
        res1 += 1

    # part 2
    elif is_report_damped_safe(levels):
        #print('d', i, levels)
        res2 += 1


print(res1)
print(res2)
print(res1+res2)
