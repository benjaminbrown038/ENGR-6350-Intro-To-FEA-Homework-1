def N1D(xi, nn):
    """
    N1D: Shape functions for 1D element
    xi : location in parent domain [-1, 1]
    nn : number of nodes (2 or 3)

    Returns:
    N : list of shape function values
    """
    if nn == 2:
        N = [(1 - xi) / 2, (1 + xi) / 2]
    elif nn == 3:
        N = [xi * (xi - 1) / 2, 1 - xi**2, xi * (xi + 1) / 2]
    else:
        raise ValueError('Only 2-node or 3-node elements supported')
    
    return N


