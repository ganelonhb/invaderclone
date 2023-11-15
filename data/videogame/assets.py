"""Defines the means of creating an asset dictionary"""

from os import path

_main_dir = path.split(path.abspath(__file__))[0]
_data_dir = path.join(_main_dir, "data")

FALLBACK_IMG = path.join(_data_dir, "missing.png")

# Electric Buzz retrieved from https://mixkit.co/free-sound-effects/error/
FALLBACK_SND = path.join(_data_dir, "missing.wav")

# Curses font retrieved from https://www.1001fonts.com/curses-font.html
FALLBACK_FNT = path.join(_data_dir, "curs.ttf")

class Theme:

    def __init__(self, name='default'):
        self._assets_path = path.join(_data_dir, "themes", name)

        self._asset_dictionary = {
            "title_icon": path.join(self._assets_path, "images", "title.png"),
            "gameover_icon": path.join(self._assets_path, "images", "gameover.png"),
            "hero": path.join(self._assets_path, "images", "hero.png"),
            "second_hero": path.join(self._assets_path, "images", "second_hero.png"),
            "neko": path.join(self._assets_path, "images", "enemy.png"),
            # BestTen retrieved from https://flopdesign.booth.pm/items/2747965
            "titlefont": path.join(self._assets_path, "fonts", "title.ttf"),
            "title_music" : path.join(self._assets_path, "bgm", "title_music.ogg"),
            "leaderboard_music" : path.join(self._assets_path, "bgm", "leaderboard_music.ogg"),
            "gameover_music" : path.join(self._assets_path, "bgm", "gameover_music.ogg"),
            "game_music": path.join(self._assets_path, "bgm", "game_music.ogg"),
            "explosion": path.join(self._assets_path, "images", "explosion.png"),
            # Explosion sound retrieved
            # from https://mixkit.co/free-sound-effects/explosion/
            "explode": path.join(self._assets_path, "bgs", "explode.ogg"),
            "explode+kitty": path.join(self._assets_path, "bgs", "explode+kitty.ogg"),
            # Press Start 2P Font retrieved from
            "pixelfont": path.join(self._assets_path, "fonts", "other.ttf"),
            "ast1": path.join(self._assets_path, "images", "asteroid1.png"),
            "ast2": path.join(self._assets_path, "images", "asteroid2.png"),
            "burst": path.join(self._assets_path, "images", "burst.png"),
            "playerbullet" : path.join(self._assets_path, "images", "playerbullet.png"),
            "enemybullet" : path.join(self._assets_path, "images", "playerbullet.png")
        }

    def get(self, key, fallback):
        """Get an asset at a key"""

        val = self._asset_dictionary.get(key, fallback)

        return val if path.isfile(val) else fallback
