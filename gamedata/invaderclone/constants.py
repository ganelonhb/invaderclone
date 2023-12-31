"""constants for use in the game"""

from os import path
from sys import platform

UNIX_SYSTEMS = ["aix", "darwin", "freebsd", "linux", "openbsd"]
WINDOWS_SYSTEMS = ["win32", "win64", "cygwin", "msys", "nt"]

save_path = path.join(path.expanduser('~'), ".config", "invaderclone") if platform in UNIX_SYSTEMS else path.join(path.expanduser('~'), "Documents", "invaderclone")
file_name = path.join(save_path, "scores.pkle")

PLAYER_SIZE_MODIFIER = 12
ENEMY_SIZE_MODIFIER = 24

_main_dir = path.split(path.abspath(__file__))[0]
DATA_DIR = path.join(_main_dir, "data")

_docsdir = ".config" if platform in UNIX_SYSTEMS else "Documents"

SETTINGS_DIR = path.join(path.expanduser("~"), _docsdir, "invaderclone")

LEVELS_DIR = _main_dir
CUSTOM_LEVELS_DIR = path.join(SETTINGS_DIR, "custom_levels")
