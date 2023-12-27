"""Scene objects for making games with PyGame."""

from sys import platform
from os import path, makedirs
import time

import pygame

from . import rgbcolors
from . import theme
from . import leaderboard

from .constants import save_path, file_name

# pylint: disable=too-many-instance-attributes
class Scene:
    """Base class for making PyGame Scenes."""

    def __init__(self, screen, background_color, soundtrack=None, skin="default"):
        """Scene initializer"""
        self._theme = theme.Theme(skin)

        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(background_color)
        self._frame_rate = 30
        self._is_valid = True
        self._soundtrack = soundtrack
        self._render_updates = None
        self._next_scene = None
        self._quit = False
        self._timestart = time.time()


        self._joysticks = None

        self._make_joysticks()

        if not path.exists(save_path):
            makedirs(save_path)
        if not path.exists(file_name):
            leaderboard.Leaderboard().save(save_path)

        self._leaderboard = leaderboard.create_leaderboard_from_pickle(
            file_name)

    def _make_joysticks(self):
        """make a list of joysticks"""
        if pygame.joystick.get_count() > 0:
            self._joysticks = [
                pygame.joystick.Joystick(x)
                for x in range(pygame.joystick.get_count())
                ]

    def clock(self):
        """Reset the scene clock."""

        self._timestart = time.time()

    def draw(self):
        """Draw the scene."""
        self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        """Process a game event by the scene."""
        if event.type == pygame.QUIT:
            self._quit = True
            self._is_valid = False
        if (
            event.type == pygame.JOYDEVICEADDED
            or
            event.type == pygame.JOYDEVICEREMOVED):
            self._make_joysticks()
        if (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            or
            event.type == pygame.JOYBUTTONDOWN and event.button == 8):
            self._is_valid = False
            self._quit = True

    def is_valid(self):
        """Is the scene valid? A valid scene can be used to play a scene."""
        return self._is_valid

    def update_scene(self):
        """Update the scene state."""

        pass

    def start_scene(self):
        """Start the scene."""
        if self._soundtrack:
            try:
                pygame.mixer.music.load(self._soundtrack)
                pygame.mixer.music.set_volume(0.2)
            except pygame.error as pygame_error:
                print("Cannot open the mixer?")
                print("\n".join(pygame_error.args))
                raise SystemExit("broken!!") from pygame_error
            pygame.mixer.music.play(-1)

    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

        if self._quit:
            return ["q"]

        return ["p"]

    def frame_rate(self):
        """Return the frame rate the scene desires."""
        return self._frame_rate

    @property
    def next_scene(self):
        """return the next scene, as set by each individual scene"""

        return self._next_scene


