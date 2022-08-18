# Image Tiler CLI

An image tiler for generation of quadrants faciliating manual object counting.

## Installation

To start using the Image Tiler CLI, you will first have to clone this repository. Use the commond belwo to get started!

```{zsh}
$ git clone https://github.com/awakenedhaki/image-tiler-cli.git
```

After you have clone the repository in your machine, you need to install this packages dependencies. The Image Tiler CLI is build off of `opencv-python` and `click`.

If you are `poetry` installed in your machine, you can run the command below...

```{zsh}
$ poetry install
```

... Otherwise, you can use good 'ol `pip` to install the entire dependency tree.

```{zsh}
$ pip install -r requirements.txt 
```

You are not set up to use the Image Tiler CLI :grinning:

## Usage

Be sure that you python version is compatible with `3.9.13`.

To run the CLI, you can call it by starting with the `python` command, followed by the path to the `cli.py` script.

```
$ python <PATH>/cli.py
```

Afterwards, you will specify either the `singular` or `batch` command. If you are interested in tiling a single image, then the `singular` command is what you are looking for. If you'd like to tile more than one image, then place all the images in a single directory, and use the `batch` command.

```
$ python <PATH>/cli.py singluar <PATH_TO_IMAGE>
```

```
$ python <PATH>/cli.py batch <PATH_TO_IMAGES_DIRECTORY>
```

For recurrent use, you can also create an alias to call on the `cli.py` script.

```{zsh}
$ alias tiler="python <PATH>/cli.py"
```

## Project Structure

```
.
├── README.md
├── pyproject.toml
└── src
    ├── cli.py
    ├── commands
    │   ├── __init__.py
    │   ├── batch.py
    │   └── singular.py
    └── service
        ├── __init__.py
        └── tiler.py
```