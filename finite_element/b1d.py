import numpy as np

def B1D(xi, nn):
    """
    B1D: Derivatives of 1D shape functions
    xi : location in parent domain [-1, 1]
    nn : number of nodes (2 or 3)

    Returns:
    B : list of shape function derivatives
    """
    if nn == 2:
        B = [-0.5, 0.5]
    elif nn == 3:
        B = [xi - 0.5, -2 * xi, xi + 0.5]
    else:
        raise ValueError('Only 2-node or 3-node elements supported')

    return B
