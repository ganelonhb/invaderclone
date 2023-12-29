"""Init file for the PyGame demo."""

from os import listdir, path

__all__ = sorted(
    [
        path.splitext(f)[0] \
            for f in listdir(path.split(path.abspath(__file__))[0]) \
                if (
                    f not in ["__init__.py", "setup.py"]
                    and path.splitext(f)[1] == ".py"
                    )
            ]
            )
