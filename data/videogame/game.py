"""Game objects to create PyGame based games."""

import os
import warnings

import pygame

from . import rgbcolors
from . import assets
from . import scene


def display_info():
    """Print out information about the display driver and video information."""
    print(f'The display is using the "{pygame.display.get_driver()}" driver.')
    print("Video Info:")
    print(pygame.display.Info())


# If you're interested in using abstract base classes, feel free to rewrite
# these classes.
# For more information about Python Abstract Base classes, see
# https://docs.python.org/3.8/library/abc.html


class VideoGame:
    """Base class for creating PyGame games."""

    def __init__(
        self,
        window_width=1820,
        window_height=1024,
        window_title="My Awesome Game",
        theme="default"
    ):
        """Initialize new game with given window size & window title."""
        pygame.init()
        pygame.joystick.init()
        self._window_size = (window_width, window_height)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(self._window_size)
        self._title = window_title
        pygame.display.set_caption(self._title)
        self._game_is_over = False
        if not pygame.font:
            warnings.warn("Fonts disabled.", RuntimeWarning)
        if not pygame.mixer:
            warnings.warn("Sound disabled.", RuntimeWarning)
        self._scene_graph = None

        self._theme = assets.Theme(theme)

        icon = pygame.image.load(self._theme.get("title_icon", assets.FALLBACK_IMG))
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

    def __init__(self, name="Invader Clone", enemy_rows=4, enemy_cols=8, difficulty_step=0.05, theme="default", powup=True, enable_multiplayer=True, width=1820, height=1024, stars=True, bg=False):
        """Init the Pygame demo."""
        super().__init__(window_title=name, window_width=width, window_height=height, theme=theme)

        self._main_dir = os.path.dirname(os.path.realpath(__file__))
        self._data_dir = os.path.join(self._main_dir, "data")

        self._difficulty_step = difficulty_step
        self._stars = stars
        self._bg = bg
        self._skin = theme

        self._enemy_rows = enemy_rows
        self._enemy_cols = enemy_cols

        print("Starting the game...")

        self.build_scene_graph()

    def build_scene_graph(self):
        """Build scene graph for the game demo."""

        the_screen = self._screen
        self._scene_graph = [
            scene.PolygonTitleScene(
                the_screen,
                self._title,
                title_color=rgbcolors.ghostwhite,
                soundtrack=self._theme.get("title_music", assets.FALLBACK_SND),
                skin=self._skin
                ),
            scene.ViolentShooterKillerScene(
                the_screen,
                soundtrack=self._theme.get("game_music", assets.FALLBACK_SND),
                num_rows=self._enemy_rows,
                num_cols=self._enemy_cols,
                stars=self._stars,
                bg=self._bg,
                skin=self._skin
                ),
            scene.LeaderboardScene(
                the_screen,
                0,
                0,
                soundtrack=self._theme.get("leaderboard_music", assets.FALLBACK_SND)
                ),
            scene.GameOverScene(
                the_screen,
                0,
                soundtrack=self._theme.get("gameover_music", assets.FALLBACK_SND),
                skin=self._skin
                )
        ]

    def run(self):
        """Run the game; the main game loop."""
        scene_iterator = self._scene_graph
        current_idx = 0

        diff = 1.0

        while not self._game_is_over:
            current_scene = scene_iterator[current_idx]
            current_scene.clock()
            current_scene.start_scene()

            while current_scene.is_valid():
                self._clock.tick(current_scene.frame_rate())
                for event in pygame.event.get():
                    current_scene.process_event(event)
                current_scene.update_scene()
                current_scene.draw()
                current_scene.render_updates()
                pygame.display.update()
            command = current_scene.end_scene()

            match command:
                case ['q']:
                    self._game_is_over = True
                case ['p']:
                    current_idx = 1
                case ['l', scr]:
                    self._scene_graph[3] = scene.GameOverScene(
                        self._screen,
                        scr,
                        soundtrack=self._theme.get("gameover_music", assets.FALLBACK_SND),
                        skin=self._skin
                    )
                    difficulty = 1.0
                    current_idx = 3
                case ['w', scr]:
                    current_idx = 3
                    self._scene_graph[3] = scene.LeaderboardScene(
                        self._screen,
                        scr[0],
                        scr[1],
                        scr[2],
                        soundtrack=self._theme.get("gameover_music", assets.FALLBACK_SND),
                        skin=self._skin
                        )
                    difficulty = 1.0
                case ['ly', scr]:
                    current_idx = 1
                    diff = diff + self._difficulty_step
                    self._scene_graph[1] = scene.ViolentShooterKillerScene(
                        self._screen,
                        self._theme.get("game_music", assets.FALLBACK_SND),
                        scr[0],
                        scr[1],
                        scr[2],
                        num_rows=self._enemy_rows,
                        num_cols=self._enemy_cols,
                        difficulty=diff,
                        stars=self._stars,
                        bg=self._bg,
                        skin=self._skin
                        )
                case ['gn']:
                    current_idx = 0
                    self._scene_graph[0] = scene.PolygonTitleScene(
                        self._screen,
                        self._title,
                        title_color=rgbcolors.ghostwhite,
                        soundtrack=self._theme.get("title_music", assets.FALLBACK_SND),
                        skin=self._skin
                    )
                    self._scene_graph[1] = scene.ViolentShooterKillerScene(
                        self._screen,
                        soundtrack=self._theme.get("game_music", assets.FALLBACK_SND),
                        num_rows=self._enemy_rows,
                        num_cols=self._enemy_cols,
                        difficulty=diff,
                        stars=self._stars,
                        bg=self._bg,
                        skin=self._skin
                        )
                    difficulty = 1.0
                case ['gy']:
                    current_idx = 1
                    self._scene_graph[1] = scene.ViolentShooterKillerScene(
                        self._screen,
                        soundtrack=self._theme.get("game_music", assets.FALLBACK_SND),
                        num_rows=self._enemy_rows,
                        num_cols=self._enemy_cols,
                        difficulty=diff,
                        stars=self._stars,
                        bg=self._bg,
                        skin=self._skin
                        )
                    difficulty = 1.0
        pygame.quit()
        return 0
