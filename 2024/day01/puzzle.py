"""
2024/01
"""

import numpy as np

data = np.loadtxt('input.txt', dtype=np.int64)

l1 = data[:,0]
l2 = data[:,1]

l1.sort()
l2.sort()

# part 1
print(sum(np.abs(l2-l1)))

# part2
res = 0

for i in l1:
    res += i * len(l2[l2==i])

print(res)
