"""
day 1
puzzle part 1
"""




fid = open('./input.txt')
lines = fid.readlines()


digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


total = 0


for line in lines:

    numbers = list(filter(lambda x: x in digits, line))
    total += int(numbers[0] + numbers[-1])


print('result:', total)
