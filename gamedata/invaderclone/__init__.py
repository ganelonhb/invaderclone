"""Init file for the PyGame demo."""

from os import listdir, path

_this_dir = path.split(path.abspath(__file__))[0]
_this_dir_list = listdir(_this_dir)
_dont_do_this_list = ["__init__.py", "setup.py"]

_modules = [
            path.splitext(f)[0]
            for f in _this_dir_list
            if (f not in _dont_do_this_list and path.splitext(f)[1] == ".py")
            ]

__all__ = sorted(_modules)
