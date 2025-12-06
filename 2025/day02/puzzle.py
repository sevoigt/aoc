"""
2025/day02
"""

class IdRange:
    def __init__(self, raw_range):
        self.start, self.end = [int(i) for i in raw_range.split('-')]

    def __repr__(self):
        return f'<IdRange: {self.start} - {self.end}>'

    def is_invalid_1(self, value):
        s = str(value)
        if divmod(len(s), 2) == 1:
            return False 
            
        idx = int(len(s)/2)
        return s[:idx] == s[idx:]

    def is_invalid_2(self, value):
        s = str(value)
        
        for i in range(1, int(len(s)/2) + 1):
            part = s[:i]
            if s.count(part) * len(part) == len(s):
                return True

        return False


with open('input.txt') as f:
    ids = [IdRange(i) for i in f.read().split(',')]


res1 = 0
res2 = 0

for i in ids:
    for k in range(i.start, i.end+1):
        if i.is_invalid_1(k):            
            res1 += k
        if i.is_invalid_2(k):
            res2 += k


print(f'part 1: {res1}')
print(f'part 2: {res2}')

