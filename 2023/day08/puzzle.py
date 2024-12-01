"""
day 8
"""

import itertools
from functools import reduce



class Node(object):

    def __init__(self, name):
        self.name = name
        self.finish = name.endswith('Z')
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node {self.name}>'



def lcm(a, b):
    """
    least common multiple (kgV in German)
    """

    n = 1
    m = 1

    while m != 0:
        d, m = divmod(n*a, b)
        n += 1

    return d*b





fid = open('input.txt')
lines = fid.readlines()

directions = lines[0][:-1]
num_directions = len(directions)

nodes = dict()


for i in lines[2:]:
    node, dirs = i.split(' = ')
    left, right = dirs[1:-2].split(', ')

    nodes.update({node :(left, right)})


# part 1

next = 'AAA'
steps = 0

while next != 'ZZZ':
    d = divmod(steps, num_directions)[1]
    next = nodes[next][0] if directions[d] =='L' else nodes[next][1]
    steps += 1

print('result part 1:', steps)


# part 2

directions = [i == 'L' for i in directions]

# now every node has a link to its next left/right node
nodeobjs = dict()
for i in nodes.keys():
    nodeobjs.update({i : Node(i)})

for i in nodes.keys():
    nodeobjs[i].left = nodeobjs[nodes[i][0]]
    nodeobjs[i].right = nodeobjs[nodes[i][1]]


# find out the turnaround cycles for all start nodes, i.e. the number of
# steps it takes to get to each finish node. The least common multiple
# of the cycles is the solution

start_nodes = [nodeobjs[i] for i in nodeobjs.keys() if i.endswith('A')]
cycles = list()


for node in start_nodes:

    steps = 0
    last_hit = 0

    for left in itertools.cycle(directions):

        node = node.left if left else node.right
        steps += 1

        if node.finish:

            if steps == last_hit:
                cycles.append(steps)
                break

            last_hit = steps
            steps = 0


total2 = reduce(lambda x, y: lcm(x, y), cycles)

print('result part 2:', total2)

