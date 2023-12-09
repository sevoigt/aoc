"""
day 8
"""

import itertools
from joblib import delayed, Parallel


class Node(object):

    def __init__(self, name):
        self.name = name
        self.finish = name.endswith('Z')
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node {self.name}>'


class NodeIterator(object):

    def __init__(self):
        self.node = None
        self.iterator = None


    def catch_up(self, num_steps):
        delta = num_steps

        for left in self.iterator:
            self.node = self.node.left if left else self.node.right
            delta -= 1
            if delta == 0:
                break

        return self.node.finish




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
'''
next = 'AAA'
steps = 0

while next != 'ZZZ':
    d = divmod(steps, num_directions)[1]
    next = nodes[next][0] if directions[d] =='L' else nodes[next][1]
    steps += 1

print('result part 1:', steps)
'''

# part 2

directions = [i == 'L' for i in directions]

# now every node has a link to its next left/right node
nodeobjs = dict()
for i in nodes.keys():
    nodeobjs.update({i : Node(i)})

for i in nodes.keys():
    nodeobjs[i].left = nodeobjs[nodes[i][0]]
    nodeobjs[i].right = nodeobjs[nodes[i][1]]


# follow the first node until a 'Z' node is found, then do the same
# number of steps for all the other nodes and check if all are 'Z'.
# Otherwise continue to traverse first node until next 'Z'

next_nodes = [nodeobjs[i] for i in nodeobjs.keys() if i.endswith('A')]
first_node = next_nodes[0]
next_nodes = next_nodes[1:]

# iterator for every parallel node
node_iterators = list()
for i in next_nodes:
    ni = NodeIterator()
    ni.node = i
    ni.iterator = itertools.cycle(directions)
    node_iterators.append(ni)


jobs = len(next_nodes)
steps = 0
substeps = 0
last_hit = 0

import time

start = time.time()

for left in itertools.cycle(directions):

    first_node = first_node.left if left else first_node.right
    steps += 1

    if first_node.finish:

        # parallel - actually slower
        #finished = Parallel(n_jobs=jobs)(delayed(i.catch_up)(steps-last_hit) for i in node_iterators)

        # single thread
        finished = [i.catch_up(steps - last_hit) for i in node_iterators]

        if all(finished):
            break

        last_hit = steps


print(time.time()-start)
print('result part 2:', steps)

