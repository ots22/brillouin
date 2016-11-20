import numpy as np
import brillouin as bz
import matplotlib.pyplot as plt

def reflect(arr,axis=0,sign=1):
    """Reflect the elements of a numpy array along a specified axis about the first element."""
    refl_idx = axis * [slice(None)] + [slice(None,0,-1), Ellipsis]
    return np.concatenate((arr[tuple(refl_idx)],arr), axis=axis)

def make_lattice(min,max,lattice_vectors):
    """Return some points from a 2-d lattice (with the origin first)."""
    xs = np.roll(np.arange(min[0],max[0]),max[0])
    ys = np.roll(np.arange(min[1],max[1]),max[1])
    lattice = np.dstack(np.meshgrid(xs,ys)).reshape(-1,2)
    lattice = np.matmul(lattice,lattice_vectors)
    return lattice

if __name__=='__main__':
    # Calculate for image points in the first quadrant only: use
    # reflective symmetry for the rest
    img_max = (2.0, 2.0)
    res = 0.001

    img_xs_full = np.arange(-img_max[0], img_max[0], res)
    img_ys_full = np.arange(-img_max[1], img_max[1], res)
    img_xs_symm = np.arange(0, img_max[0], res)
    img_ys_symm = np.arange(0, img_max[1], res)
    image_pts_symm = np.dstack(np.meshgrid(img_xs_symm, img_ys_symm))

    # square_lattice = make_lattice(min=(-3,-3), max=(5,5),
    #                               lattice_vectors=np.eye(2))
    # sq_bril_zones = bz.brillouin_zone_index(image_pts_symm, square_lattice)
    # sq_bril_zones = reflect(reflect(sq_bril_zones, axis=0), axis=1)   
    # plt.pcolormesh(img_xs_full, img_ys_full,
    #                sq_bril_zones, cmap=plt.get_cmap('Paired'))
    # plt.axes().set_aspect('equal')
    # plt.show()

    hexagonal_lattice_vectors = np.array([[1.0, 0.0],
                                          [np.cos(np.pi/3.0), np.sin(np.pi/3.0)]])
    hexagonal_lattice_pts = make_lattice(min=(-4,-3), max=(6,6),
                                         lattice_vectors=hexagonal_lattice_vectors)
    hex_bril_zones = bz.brillouin_zone_index(image_pts_symm, hexagonal_lattice_pts)
    hex_bril_zones = reflect(reflect(hex_bril_zones, axis=0), axis=1)   

    plt.pcolormesh(img_xs_full, img_ys_full,
                   hex_bril_zones, cmap=plt.get_cmap('Paired'))
    plt.axes().set_aspect('equal')
    plt.show()
