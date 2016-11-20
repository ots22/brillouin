import numpy as np

def rank_of_first(xs,axis=0):
    """Return the rank of the first item in a collection of items when sorted."""
    return np.argpartition(np.argsort(xs,axis=axis),0,axis=axis)[0,:]

def brillouin_zone_index(x, lattice):
    """Determine the index of the Brillouin zone in which a given point
    (or collection of points) lies.

    Arguments:
    x -- a numpy array whose last dimension represents spatial coordinates
    lattice -- a numpy array of whose first dimension indexes over
    lattice points, with the origin given as the first lattice point.
    """
    # calculate the distances from each lattice point to each point in x
    lat_norms = np.apply_along_axis(np.linalg.norm, -1,
                                    lattice[:,np.newaxis,np.newaxis,:] - x)
    # return the rank of the origin
    return rank_of_first(lat_norms)
