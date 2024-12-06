"""
2024/day05
"""

class Order:
    """
    Store sets with smaller and larger numbers for a value
    according to the rules
    """
    def __init__(self, val):
        self.value = val
        self.smaller = set()
        self.larger = set()

    def __repr__(self):
        return f'<{self.value}>'

    def __gt__(self, other):
        return other.value in self.smaller

    def __le__(self, other):
        return other.value in self.larger


def to_list(line, sep, type):
    """
    Convert separated values from a line to a list
    """
    return [type(i) for i in line.split(sep)]


def get_center(x):
    return x[int((len(x)-1) / 2)]


rules = list()
updates = list()

with open('input.txt', 'r') as fid:
    for line in fid:
        if '|' in line:
            rules.append(to_list(line, '|', int))
        if ',' in line:
            updates.append(to_list(line, ',', int))


# part 1
res1 = 0
incorrect = list()

# create a dictionary with smaller/larger lists for each number
rd = dict()

for a, b in rules:
    if a in rd:
        rd[a].larger.add(b)
    else:
        _ord = Order(a)
        _ord.larger.add(b)
        rd.update({a : _ord})

    if b in rd:
        rd[b].smaller.add(a)
    else:
        _ord = Order(b)
        _ord.smaller.add(a)
        rd.update({b: _ord})

for upd in updates:
    ok = True

    for i in range(len(upd)):
        bfore = set(upd[0:i])
        after = set(upd[i+1:])

        val = rd[upd[i]]
        ok &= bfore.issubset(val.smaller) and after.issubset(val.larger)

    if ok:
        res1 += get_center(upd)
    else:
        incorrect.append(upd)

print(res1)

# part 2
res2 = 0

for i in incorrect:
    obj = [rd[n] for n in i]
    obj.sort()
    res2 += get_center(obj).value

print(res2)
