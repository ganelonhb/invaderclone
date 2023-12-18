"""Defines the means of creating an asset dictionary"""

from os import path, makedirs
from sys import platform
from glob import glob

_main_dir = path.split(path.abspath(__file__))[0]
_data_dir = path.join(_main_dir, "data")

UNIX_SYSTEMS = ["aix", "darwin", "freebsd", "linux", "openbsd"]
WINDOWS_SYSTEMS = ["win32", "win64", "cygwin", "msys", "nt"]

_docsdir = ".config" if platform in UNIX_SYSTEMS else "Documents"

_settingsdir = path.join(path.expanduser("~"), _docsdir, "invaderclone")

if not path.exists(path.join(_settingsdir, "themes")):
    makedirs(path.join(_settingsdir, "themes"))

FALLBACK_IMG = path.join(_data_dir, "missing.png")

# Electric Buzz retrieved from https://mixkit.co/free-sound-effects/error/
FALLBACK_SND = path.join(_data_dir, "missing.wav")

# Curses font retrieved from https://www.1001fonts.com/curses-font.html
FALLBACK_FNT = path.join(_data_dir, "curs.ttf")

class Theme:

    def __init__(self, name='default'):
        self._name = name
        self._assets_path = path.join(_data_dir, "themes", name)
        self._config_path = path.join(_settingsdir, "themes", name)

        self._asset_dictionary = {
            "title_icon": path.join("images", "title.png"),
            "gameover_icon": path.join("images", "gameover.png"),
            "hero": path.join("images", "hero.png"),
            "second_hero": path.join("images", "second_hero.png"),
            "neko": path.join("images", "enemy.png"),
            "titlefont": path.join("fonts", "title.ttf"),
            "title_music" : path.join("bgm", "title.ogg"),
            "leaderboard_music" : path.join("bgm", "leaderboard.ogg"),
            "gameover_music" : path.join("bgm", "game_over.ogg"),
            "game_music": path.join("bgm", "game.ogg"),
            "explosion": path.join("images", "explosion.png"),
            "explode": path.join("bgs", "explode.ogg"),
            "explode+kitty": path.join("bgs", "explode+kitty.ogg"),
            "pixelfont": path.join("fonts", "other.ttf"),
            "ast1": path.join("images", "asteroid1.png"),
            "ast2": path.join("images", "asteroid2.png"),
            "burst": path.join("images", "burst.png"),
            "playerbullet" : path.join("images", "goodbullet.png"),
            "enemybullet" : path.join("images", "badbullet.png"),
            "bg" : path.join("images", "bg.png")
        }

        self._enemies = []

        if path.exists(self._config_path):
            self._enemies = sorted(glob(path.join(self._config_path, "images", "enemy*.png")))
        elif path.exists(self._assets_path):
            self._enemies = sorted(glob(path.join(self._assets_path, "images", "enemy*.png")))

        self._obstacles = []

        if path.exists(self._config_path):
            self._obstacles = sorted(glob(path.join(self._config_path, "images", "obstacle*.png")))
        elif path.exists(self._assets_path):
            self._obstacles = sorted(glob(path.join(self._assets_path, "images", "obstacle*.png")))

    def get_obstacle(self, num):
        if len(self._obstacles) < num:
            return FALLBACK_IMG

        return self._obstacles[num]

    def num_obstacles(self):
        return len(self._obstacles)

    def get_enemy(self, num):
        if len(self._enemies) < num:
            return FALLBACK_IMG

        return self._enemies[num]

    def num_enemies(self):
        return len(self._enemies)

    def get(self, key, fallback):
        """Get an asset at a key"""

        if path.exists(self._config_path):
            val = self._asset_dictionary.get(key, fallback)
            val = path.join(self._config_path, val)
            return val if path.isfile(val) else fallback

        val = self._asset_dictionary.get(key, fallback)
        val = path.join(self._assets_path, val)

        return val if path.isfile(val) else fallback
