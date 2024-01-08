""" Simple setup.py """

from os import path
from setuptools import setup

with open("README.md", "r") as f:
    DESCRIPTION=f.read()

setup(
    name="invaderclone",
    version="0.9.5",
    python_requires=">=3.5.0",
    description="A module Space Invaders clone in Python Pygame",
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=["invaderclone"],
    author="Zachary Worcester",
    author_email="zworcester0@csu.fullerton.edu",
    install_requires=["pygame"],
    url="https://github.com/ganelonhb/invaderclone",
    py_modules = ["invaders"],
    package_data = {"invaderclone" : ["data/*", "data/themes/default/bgm/*", "data/themes/default/bgs/*", "data/themes/default/fonts/*", "data/themes/default/images/*"]},
    include_package_data=True,
    entry_points= {
        'console_scripts' : [
            'invaderclone = invaders:main'
            ]
        }
    )
