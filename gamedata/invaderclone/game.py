"""Game objects to create PyGame based games."""

import os
import sys
import importlib
import warnings

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

import re

from copy import deepcopy

from . import rgbcolors
from . import theme
from .scene import Scene
from .polygon_title_scene import PolygonTitleScene
from .leaderboard_scene import LeaderboardScene
from .game_over_scene import GameOverScene
from .constants import LEVELS_DIR, CUSTOM_LEVELS_DIR

def display_info():
    """Print out information about the display driver and video information."""
    print(f'The display is using the "{pygame.display.get_driver()}" driver.')
    print("Video Info:")
    print(pygame.display.Info())

class VideoGame:
    """Base class for creating PyGame games."""

    def __init__(
        self,
        game_settings
    ):
        """Initialize new game with given window size & window title."""
        pygame.init()
        pygame.joystick.init()
        self._game_settings = game_settings
        gs = self._game_settings

        self._window_size = (gs["width"], gs["height"])
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(self._window_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._title = gs["name"]
        pygame.display.set_caption(self._title)
        self._game_is_over = False
        if not pygame.font:
            warnings.warn("Fonts disabled.", RuntimeWarning)
        if not pygame.mixer:
            warnings.warn("Sound disabled.", RuntimeWarning)
        self._scene_graph = None

        self._theme = theme.Theme(gs["theme"])

        icon = pygame.image.load(self._theme.get("title_icon", theme.FALLBACK_IMG))
        icon_img = pygame.transform.scale(icon, (128,128))
        pygame.display.set_icon(icon_img)

    @property
    def scene_graph(self):
        """Return the scene graph representing all the scenes in the game."""
        return self._scene_graph

    def build_scene_graph(self):
        """Build the scene graph for the game."""
        raise NotImplementedError

    def run(self):
        """Run the game; the main game loop."""
        raise NotImplementedError


class InvaderClone(VideoGame):
    """Show a colored window with a colored message and a polygon."""

    def __init__(self,
                game_settings
                ):
        """Init the Pygame demo."""
        super().__init__(game_settings)

        self._main_dir = os.path.dirname(os.path.realpath(__file__))
        self._data_dir = os.path.join(self._main_dir, "data")

        #print("Starting the game...")

        levels = [os.path.join(LEVELS_DIR, level) for level in os.listdir(LEVELS_DIR) if re.match(r'level[0-9]+.py', level)]

        if not os.path.exists(CUSTOM_LEVELS_DIR):
            os.makedirs(CUSTOM_LEVELS_DIR)

        levels = sorted(levels + [os.path.join(CUSTOM_LEVELS_DIR, level) for level in os.listdir(CUSTOM_LEVELS_DIR) if re.match(r'level[0-9]+.py', level) and level != "level0.py"])

        level_modules = {}
        self._level_classes = {}

        for level in levels:
            module_name, _ = os.path.splitext(os.path.basename(level))
            spec = importlib.util.spec_from_file_location(f"invaderclone.{module_name}", level)
            level_modules[f"invaderclone.{module_name}"] = importlib.util.module_from_spec(spec)
            sys.modules[f"invaderclone.{module_name}"] = level_modules[f"invaderclone.{module_name}"]
            spec.loader.exec_module(level_modules[f"invaderclone.{module_name}"])

            class_name = f"{module_name[0].upper()}{module_name[1:]}"
            self._level_classes[class_name] = getattr(sys.modules[f"invaderclone.{module_name}"], class_name)
        self.build_scene_graph()

    def build_scene_graph(self):
        """Build scene graph for the game demo."""

        the_screen = self._screen
        self._scene_dict = {
            "PolygonTitleScene" : PolygonTitleScene(
                the_screen,
                self._game_settings
                ),
            "LeaderboardScene" : LeaderboardScene(
                the_screen,
                self._game_settings
                ),
            "GameOverScene" : GameOverScene(
                the_screen,
                self._game_settings
                )
        }

        for level_name, LevelClass in self._level_classes.items():
            self._scene_dict[level_name] = LevelClass(the_screen, self._game_settings)

            if not isinstance(self._scene_dict[level_name], Scene):
                raise TypeError

    def run(self):
        """Run the game; the main game loop."""
        scene_iterator = self._scene_dict
        current_scene_string = "PolygonTitleScene"
        current_level = 0
        num_levels = len(self._level_classes.keys())

        while not self._game_is_over:
            current_scene = scene_iterator[current_scene_string]
            current_scene.clock()
            current_scene.start_scene()
            current_scene.update_settings()
            reference_settings = deepcopy(self._game_settings)

            while current_scene.is_valid():
                self._clock.tick(current_scene.frame_rate())
                for event in pygame.event.get():
                    current_scene.process_event(event)
                current_scene.update_scene()
                if reference_settings != self._game_settings:
                    current_scene.update_settings()
                current_scene.draw()
                pygame.display.update()
            command = current_scene.end_scene()
            current_scene.reset_scene()

            match command:
                case ['QUIT_GAME']:
                    self._game_is_over = True
                case ['CHANGE_SCENE', scene_name]:
                    current_scene_string = scene_name
                case ['CHANGE_LEVEL']:
                    if current_level != num_levels - 1:
                        current_level += 1
                    elif current_level != 0:
                        current_level = 0

                    game_settings = self._game_settings

                    dm = game_settings["current_difficulty_modifier"] + (game_settings["difficulty_step"] / 100)

                    game_settings["current_difficulty_modifier"] = dm

                    current_scene_string = f"Level{current_level}"
                case ['RST_CHANGE_SCENE', scene_name]:
                    game_settings = self._game_settings
                    game_settings["current_difficulty_modifier"] = 1.0
                    game_settings["current_score_p1"] = 0
                    game_settings["current_score_p2"] = 0
                    game_settings["current_lives_p1"] = deepcopy(game_settings["starting_lives"])
                    game_settings["current_lives_p2"] = deepcopy(game_settings["starting_lives"])
                    game_settings["oneups"] = []

                    current_level = 0

                    current_scene_string = scene_name
        pygame.quit()
        return 0
