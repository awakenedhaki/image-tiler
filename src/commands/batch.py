# DEPENDENCIES =================================================================
import click

from pathlib import Path
from service import tiler
from cv2 import imread, imwrite

# COMMAND ======================================================================
@click.command('batch')
@click.argument('ntiles', type = click.INT)
@click.argument('images-path',
                type = click.Path(
                    file_okay = False,
                    resolve_path = True,
                    exists = True,
                    path_type = Path
                ))
def batch(ntiles: int, images_path: str) -> None:
    '''
    Applies the `tiler` function to a directory containing image files.

    Params:
        ntiles (int): A square number that indicates the total number of tiles.
        images_path (pathlib.Path): Path to directory containig image files.
    '''
    # Create subdirectory for tiled images
    dest = images_path / 'tiled'
    if not dest.exists():
        dest.mkdir()

    # Tiling images
    # . Create tiled image destination path (filename)
    # . Reading image file into array of pixel values
    # . Applying `tiler` function
    # . Writing tiled images into created subdirectory
    for image_file in images_path.glob('*.*'):
        filename = dest / f'{image_file.name}_tiled{image_file.suffix}'
        image = imread(str(image_file))
        tiled_image = tiler(image, ntiles)
        imwrite(str(filename), tiled_image)