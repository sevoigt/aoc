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
