# DEPENDENCIES =================================================================
import click

from service import tiler
from cv2 import imread, imwrite
from pathlib import Path


# COMMAND ======================================================================
@click.command()
@click.argument('ntiles', type = click.INT)
@click.argument('image-path',
                type = click.Path(
                    dir_okay = False,
                    resolve_path = True,
                    exists = True,
                    path_type = Path
                ))
def singular(ntiles: int, image_path: str) -> None:
    '''
    Applies `tiler` function to a single image.
    
    Params:
        ntiles (int): A square number that indicates the total number of tiles.
        image_path (pathlib.Path): Path to a single image file.
    '''
    # Createing the destination filename for the tiled image
    dest = image_path.parent / f'{image_path.name}_tiled{image_path.suffix}'
    # Reading image file into array of pixel values
    image = imread(str(image_path))
    # Applying tiler function
    tiled_image = tiler(image, ntiles)
    # Writing tiled image
    imwrite(str(dest), tiled_image)