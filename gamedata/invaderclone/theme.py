"""Defines the means of creating an asset dictionary"""

import errno

from os import path, makedirs, strerror
from sys import platform
from glob import glob

from .constants import SETTINGS_DIR, DATA_DIR

# missing.png created by ganelon, but inspired by the Source Engine's fallback texture.
FALLBACK_IMG = path.join(DATA_DIR, "missing.png")

# Electric Buzz retrieved from https://mixkit.co/free-sound-effects/error/
FALLBACK_SND = path.join(DATA_DIR, "missing.wav")

# Curses font retrieved from https://www.1001fonts.com/curses-font.html
FALLBACK_FNT = path.join(DATA_DIR, "curs.ttf")

def get_theme_dir(name):
    assets_path = path.join(DATA_DIR, "themes", name)
    config_path = path.join(SETTINGS_DIR, "themes", name)

    if path.exists(config_path):
        return config_path
    elif path.exists(assets_path):
        return assets_path

    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), f'niether {self._config_path} nor {self._assets_path}')

class Theme:

    def __init__(self, name='default'):

        if not path.exists(path.join(SETTINGS_DIR, "themes")):
            makedirs(path.join(SETTINGS_DIR, "themes"))

        self._name = name
        self._assets_path = path.join(DATA_DIR, "themes", name)
        self._config_path = path.join(SETTINGS_DIR, "themes", name)

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
        self._obstacles = []

        if path.exists(self._config_path):
            self._enemies = sorted(glob(path.join(self._config_path, "images", "enemy*.png")))
            self._obstacles = sorted(glob(path.join(self._config_path, "images", "obstacle*.png")))
            self._dir = self._config_path
        elif path.exists(self._assets_path):
            self._enemies = sorted(glob(path.join(self._assets_path, "images", "enemy*.png")))
            self._obstacles = sorted(glob(path.join(self._assets_path, "images", "obstacle*.png")))
            self._dir = self._assets_path
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), f'{self._config_path} or {self._assets_path}')

    def get_dir(self):
        return self._dir

    def get_obstacle(self, num):
        if len(self._obstacles) < num:
            return FALLBACK_IMG

        return self._obstacles[num]

    def get_obstacles(self):
        return self._obstacles

    def num_obstacles(self):
        return len(self._obstacles)

    def get_enemy(self, num):
        if len(self._enemies) < num:
            return FALLBACK_IMG

        return self._enemies[num]

    def get_enemies(self):
        return self._enemies

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
