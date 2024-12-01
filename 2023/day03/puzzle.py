"""
day 3

a bit messy indeed :)
"""


class Number(object):

    def __init__(self):
        self.num = None
        self.row = None
        self.col = None
        self.neighbours = ''
        self.block = None


    def is_part(self, lines, symbols):
        '''
        Determine the neighbourhood coordinates of this number and
        check wether it contains any symbol (in this case -> its a part)
        '''

        startidx = max(0, self.col-1)
        endidx = min(self.col+len(self), len(lines[self.row])) + 1

        # block format is [[row_min, row_max], [col_min, col_max]]
        self.block = [[self.row, self.row], [startidx, endidx-1]]

        self.neighbours += lines[self.row][startidx:endidx]

        if (self.row > 0):
            self.neighbours += lines[self.row-1][startidx:endidx]
            self.block[0][0] = self.row - 1

        if (self.row < (len(lines)-1)):
            self.neighbours += lines[self.row+1][startidx:endidx]
            self.block[0][1] = self.row + 1

        part = False

        for i in self.neighbours:
            if i in symbols:
                part = True
                break

        return part


    def in_block(self, row, col):
        '''
        Check wether a coordinate is within the neighbourhood-block of this number
        '''
        return row >= self.block[0][0] and row <= self.block[0][1] and \
               col >= self.block[1][0] and col <= self.block[1][1]


    def __repr__(self):
        return f'<Number: {self.num:>3} @ [{self.row}, {self.col}]>'

    def __len__(self):
        return len(str(self.num))



digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


fid = open('input.txt')

# get the symbols used in the schematic
cont = fid.read()
cont = cont.replace('\n', '')
cont = cont.replace('.', '')

for i in digits:
    cont = cont.replace(i, '')

symbols = set(cont)

# now read the lines for further processing
fid.seek(0)
lines = fid.readlines()


numbers = list()
stars = list()

# collect all numbers in the schematic with their start-coordinates [row, col]
for row in range(len(lines)):

    num = None

    for col in range(len(lines[row])):

        char = lines[row][col]

        if char in digits:
            if num is None:
                num = Number()
                num.row = row
                num.col = col
                num.num = char
            else:
                num.num += lines[row][col]

        if ((char == '.') or (char in symbols) or (char == '\n')) and (num is not None):
            num.num = int(num.num)
            numbers.append(num)

            num = None

        if (char == '*'):
            stars.append((row, col))


total = 0

for i in numbers:
    if i.is_part(lines, symbols):
        total += i.num

print('result part 1:', total)



gears = list()
total_gears = 0

for i in stars:

    matching_numbers = list()

    for number in numbers:
        if number.in_block(i[0], i[1]):
            matching_numbers.append(number)

    gears.append(matching_numbers)


for i in filter(lambda x: len(x) == 2, gears):
    total_gears += i[0].num * i[1].num


print('result part 2:', total_gears)
