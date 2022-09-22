# DEPENDENCIES =================================================================
from cv2 import line
from math import sqrt
from typing import Tuple
from numpy import ndarray


# CONSTANTS ====================================================================
DEFAULT_COLOR: Tuple[int, int, int] = (255, 255, 255)

    
# FUNCTIONS ====================================================================
def tiler(image: ndarray, ntiles: int) -> ndarray:
    '''
    Add horizontal and vertical lines creating `ntiles` tiles in an image.

    Params:
        image (ndarray): An array of pixel values representing an image.
        ntiles (int): The total number of tiles to be generated in an image

    Returns:
        (ndarray) The initial image, with horizontal and vertical lines to 
            create `ntiles` tiles.
    '''
    rows, columns, _ = image.shape

    # Determinig the number of tiles for each row and column
    ndivisors = sqrt(ntiles)
    # . Validating `ntiles` is a square number
    if (not ndivisors.is_integer()) or (ndivisors <= 1):
        raise ValueError(f'{ntiles} is not a square number.')
    ndivisors = int(ndivisors)

    # Spacing between horixontal and vertical lines
    row_interval = rows // ndivisors
    column_interval = columns // ndivisors

    # Starting vertical and horizontal coordinates
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