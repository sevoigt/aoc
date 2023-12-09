"""
day 8
"""


class Node(object):
    
    def __init__(self, name):
        self.name = name
        self.finish = name.endswith('Z')
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node {self.name}>'


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

all_z = False
steps = 0
directions = [i == 'L' for i in directions]

# now every node has a link to its next left/right node
nodeobjs = dict()
for i in nodes.keys():
    nodeobjs.update({i : Node(i)})

for i in nodes.keys():
    nodeobjs[i].left = nodeobjs[nodes[i][0]]
    nodeobjs[i].right = nodeobjs[nodes[i][1]]

next_nodes = [nodeobjs[i] for i in nodeobjs.keys() if i.endswith('A')]


while not all_z:
    _d, _m = divmod(steps, num_directions)
    left = directions[_m]
    next_nodes = [i.left for i in next_nodes] if left else \
                 [i.right for i in next_nodes] 
    all_z = sum([0 if i.finish else 1 for i in next_nodes]) == 0 
    steps += 1
    
print('result part 2:', steps)
