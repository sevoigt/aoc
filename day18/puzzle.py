"""day 18"""import numpy as npimport syssys.setrecursionlimit(100000)directions = {'U': (-1,  0),              'D': ( 1,  0),              'R': ( 0,  1),              'L': ( 0, -1)}def add_tuple(a, b):    return (a[0] + b[0], a[1] + b[1])def box_idx(pos):    """    Get list with indices of square box around pos    """    return (add_tuple(pos, (-1, -1)),            add_tuple(pos, (-1, 0)),            add_tuple(pos, (-1, 1)),            add_tuple(pos, (0, -1)),            add_tuple(pos, (0, 1)),            add_tuple(pos, (1, -1)),            add_tuple(pos, (1, 0)),            add_tuple(pos, (1, 1)))def save_grid(grid):    """    Save grid as plain text with 0 and 1    """    chars = {1: '0', 0: '.'}    f = open('grid.txt', 'w')    for i in range(grid.shape[0]):        for k in range(grid.shape[1]):            f.write(chars[grid[i, k]])        f.write('\n')    f.close()def fill(pos, grid):    """    recursively fill area surrounded by ones in an otherwise zero-array    -> works only with increased max recursion depth (100000 is ok)    """    for i in box_idx(pos):        if grid[i] == 0:            grid[i] = 1            fill(i, grid)def get_grid(steps):    """    Obtain max dimensions of grid and return shape of grid and start point    """    _w = 0    width_min = 0    width_max = 0        _h = 0    height_min = 0    height_max = 0    for d, n in steps:        if d == 'R':            _w += n        elif d == 'L':            _w -= n        elif d == 'D':            _h += n        elif d == 'U':            _h -= n        width_min = min(_w, width_min)        width_max = max(_w, width_max)        height_min = min(_h, height_min)        height_max = max(_h, height_max)    shape = (height_max - height_min + 1, width_max - width_min + 1)    start = (-height_min, -width_min)    return (shape, start)def calc_area(steps, h, height):    """    Calculate area by adding/subtracting the areas of rectangles formed    by the trench    """    p = 0    for i in range(len(steps)):        step = steps[i]        d = step[0]        d_pre = steps[i-1][0]        d_nxt = steps[(i+1)%len(steps)][0]        n = step[1]        peak = d_pre + d_nxt            delta = 0                if d == 'U':            h -= n        elif d == 'D':            h += n        elif d == 'R':            if peak == 'UD':                delta = (height - h) * (n+1)            elif peak == 'DU':                delta = (height - h) * (n-1)            else:                delta = (height - h) * n        elif d == 'L':            if peak == 'DU':                delta = - (height - h - 1) * (n+1)            elif peak == 'UD':                delta = - (height - h - 1) * (n-1)            else:                delta = - (height - h - 1) * n            p += delta    return pfid = open('input.txt')lines = fid.readlines()# part 1 - 'visual approach' (build grid, draw trench, draw fill area)steps = [(d, int(n)) for d, n, col in [i.strip().split(' ') for i in lines]]shape, pos = get_grid(steps)h0 = pos[0]'''# draw trenchgrid = np.zeros(shape, dtype=np.int8)for d, n in steps:    for k in range(n):        grid[pos] = 1        pos = add_tuple(pos, directions[d])# fill trench#pos0 = (1, 1)        # input_minpos0 = (100, 100)    # inputfill(pos0, grid)p1 = len(grid.flatten().nonzero()[0])print('result part 1', p1)'''#save_grid(grid)# part 1 - 'clever approach' (add/subtract rectangles)p1 = calc_area(steps, h0, shape[0])print('result part 1', p1)# part 2steps2 = []_dir = ('R', 'D', 'L', 'U')for i in lines:    d, n, col = i.strip().split(' ')    n = eval(f'0x{col[2:7]}')    d = _dir[int(col[7])]    steps2.append((d, n))shape, pos = get_grid(steps2)p2 = calc_area(steps2, pos[0], shape[0])print('result part 2', p2)