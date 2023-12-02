"""
day 1
puzzle part 2
"""


def combine(a, b):
    '''
    combine two digit-strings to a number
    '''

    a = digits_dict[a] if a in digits_dict else a
    b = digits_dict[b] if b in digits_dict else b

    return int(a + b)



digits_dict = {'zero'  : '0',
               'one'   : '1',
               'two'   : '2',
               'three' : '3',
               'four'  : '4',
               'five'  : '5',
               'six'   : '6',
               'seven' : '7',
               'eight' : '8',
               'nine'  : '9'}



numerals = list(digits_dict.keys())
digits = list(digits_dict.values())



fid = open('./input.txt')
lines = fid.readlines()


total = 0




for line in lines:

    numbers = list()

    for i in range(len(line)):

        char = line[i]

        # we found a numeric digit
        if char in digits:
            numbers.append(char)
            continue

        # check for numerals
        for k in numerals:
            try:
                if line[i:i+len(k)] == k:
                    numbers.append(k)
                    i += len(k)             # uhhh
            except IndexError:
                pass

    code = combine(numbers[0], numbers[-1])
    #print(line[:-1], '->', code)
    total += code


print('result:', total)
