"""
day 8
"""

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

next_nodes = [i for i in nodes.keys() if i.endswith('A')]
all_z = False
steps = 0
directions = [i == 'L' for i in directions]

while not all_z:
    _d, _m = divmod(steps, num_directions)
    left = directions[_m]
    next_nodes = [nodes[i][0] for i in next_nodes] if left else \
                 [nodes[i][1] for i in next_nodes] 
    all_z = sum([0 if i.endswith('Z') else 1 for i in next_nodes]) == 0 
    steps += 1
    
print('result part 2:', steps)
