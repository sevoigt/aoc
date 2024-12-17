"""
Helper functions
"""

import numpy as np


def read_grid(fname):
    """
    Read a grid or map-like input file that contains a
    rectangular block of charachters

    Returns a list of lists where each charachter is an Element
    of the inner lists
    """

    with open(fname, 'r') as fid:
        grid = [list(i.strip()) for i in fid.readlines()]

    return grid


def read_grid_array(fname):
    """
    Same as read_grid but output converted to numpy array
    """
    return np.array(read_grid(fname))


def pos_in_grid(shape, pos):
    """
    <shape> must be a 2-tuple with the dimensions of the grid
    <pos> must be a 2-iterable of grid-indices
    Checks if pos is within grid-shape
    """
    return pos[0] > -1 and pos[1] > -1 and  \
           pos[0] < shape[0] and pos[1] < shape[1]


def read_whole_file(fname):
    """
    Just read the whole conent of the given file
    """
    with open(fname, 'r') as fid:
        return fid.read()
