# DEPENDENCIES =================================================================
from cv2 import line
from math import sqrt
from typing import Tuple
from numpy import ndarray

# CONSTANTS ====================================================================
DEFAULT_COLOR: Tuple[int, int, int] = (255, 255, 255)
    
# FUNCTIONS ====================================================================
def tiler(image: ndarray, ntiles: int):
    rows, columns, _ = image.shape

    ndivisors = sqrt(ntiles)
    if (not ndivisors.is_integer()) or (ndivisors <= 1):
        raise ValueError(f'{ntiles} is not a square number.')
    ndivisors = int(ndivisors)

    row_interval = rows // ndivisors
    column_interval = columns // ndivisors

    vcoord, hcoord = 0, 0
    for _ in range(ndivisors):
        # Adding vertical line
        line(image,
             pt1 = (0, vcoord),
             pt2 = (columns, vcoord),
             color = DEFAULT_COLOR)
        vcoord += row_interval

        # Adding horizontal line
        line(image,
             pt1 = (hcoord, 0),
             pt2 = (hcoord, rows),
             color = DEFAULT_COLOR)
        hcoord += column_interval
    return image