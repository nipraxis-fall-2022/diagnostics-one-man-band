""" Scan outlier metrics
"""

# Any imports you need
import numpy as np
import nibabel as nib
import nipraxis as npx



def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the mean of the (voxel differences squared)).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumes in `img`.
    """

    data = img.get_fdata()
    voxels_by_time = data.reshape(-1, data.shape[-1])
    vol_diff = np.diff(voxels_by_time, axis=1)
    dvals = np.sqrt(np.mean(vol_diff **2, axis=0))
    
    return dvals


    # Hint: remember 'axis='.  For example:
    # In [2]: arr = np.array([[2, 3, 4], [5, 6, 7]])
    # In [3]: np.mean(arr, axis=1)
    # Out[2]: array([3., 6.])
    #
    # You may be be able to solve this in four lines, without a loop.
    # But solve it any way you can.
    # This is a placeholder, replace it to write your solution.
    raise NotImplementedError('Code up this function')
