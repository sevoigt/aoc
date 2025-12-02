"""
2025/day01
"""

directions = {'L': -1, 'R': 1}

lines = open('input.txt', 'r').read().split('\n')[:-1]

index = 50
prev_index = 50

num_zeros1 = 0
num_zeros2 = 0

for i in lines:
    fac = directions[i[0]]
    step = int(i[1:])

    index += fac*step
    n, index = divmod(index, 100)

    if index == 0:
        num_zeros1 += 1

    if prev_index == 0 and n < 0:
        num_zeros2 += abs(n) - 1
    else:
        num_zeros2 += abs(n)

    if index == 0 and n <= 0:
        num_zeros2 += 1

    #print(f'{prev_index} : {fac*step} : {index} -> {num_zeros2}')
    prev_index = index

print(num_zeros1)   # 1011
print(num_zeros2)   # 5937
