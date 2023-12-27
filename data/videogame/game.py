"""Game objects to create PyGame based games."""

import os
import warnings

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

from . import rgbcolors
from . import theme
from . import scene
from .polygon_title_scene import PolygonTitleScene
from .leaderboard_scene import LeaderboardScene
from .game_over_scene import GameOverScene
from .level0 import Level0


def display_info():
    """Print out information about the display driver and video information."""
    print(f'The display is using the "{pygame.display.get_driver()}" driver.')
    print("Video Info:")
    print(pygame.display.Info())

class VideoGame:
    """Base class for creating PyGame games."""

    def __init__(
        self,
        window_width=1820,
        window_height=1024,
        window_title="My Awesome Game",
        theme_name="default"
    ):
        """Initialize new game with given window size & window title."""
        pygame.init()
        pygame.joystick.init()
        self._window_size = (window_width, window_height)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(self._window_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._title = window_title
        pygame.display.set_caption(self._title)
        self._game_is_over = False
        if not pygame.font:
            warnings.warn("Fonts disabled.", RuntimeWarning)
        if not pygame.mixer:
            warnings.warn("Sound disabled.", RuntimeWarning)
        self._scene_graph = None

        self._theme = theme.Theme(theme_name)

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
                name="Invader Clone",
                enemy_rows=4,
                enemy_cols=8,
                difficulty_step=0.05,
                theme_name="default",
                powup=True,
                enable_multiplayer=True,
                width=1820,
                height=1024,
                stars=True,
                bg=False,
                alttitle = None,
                sub1 = "全部のネコ宇宙人を倒す！ 動く：'←'／'→' 撃つ：'SPACE'",
                sub2 = "Kill all cat aliens! Move: '←'/'→' Shoot: 'SPACE'",
                pak = "Press ANY KEY!",
                victorytext = "VICTORY!",
                continuetext = "Continue (Y/N)?",
                gameovertext = "GAME OVER!",
                bg_speed = 6,
                titlebg_color = rgbcolors.black,
                gamebg_color = rgbcolors.black,
                leaderboardbg_color = rgbcolors.black,
                gameoverbg_color = rgbcolors.black,
                title_color = rgbcolors.ghostwhite,
                subtitle1_text_color = None,
                subtitle2_text_color = None,
                pak_text_color = None,
                player_speed = 15.,
                enemy_speed = 5.,
                obstacle_speed = 7.,
                powerup_speed = 20.,
                powerup_chance = 13,
                obstacle_chance = 0.004,
                ):
        """Init the Pygame demo."""
        super().__init__(window_title=name, window_width=width, window_height=height, theme_name=theme_name)

        self._main_dir = os.path.dirname(os.path.realpath(__file__))
        self._data_dir = os.path.join(self._main_dir, "data")

        self._title_color = title_color
        self._subtitle1_color = subtitle1_text_color
        self._subtitle2_color = subtitle2_text_color
        self._pak_color = pak_text_color

        self._titlebg_color = titlebg_color
        self._gamebg_color = gamebg_color
        self._leaderboardbg_color = leaderboardbg_color
        self._gameoverbg_color = gameoverbg_color

        self._difficulty_step = difficulty_step
        self._stars = stars
        self._bg = bg
        self._bg_speed = bg_speed
        self._skin = theme_name

        #Title Screen Settings:
        self._alttitle = alttitle
        self._sub1 = sub1
        self._sub2 = sub2
        self._pak = pak

        #Leaderboard Settings:
        self._victorytext = victorytext
        self._continuetext = continuetext

        #Game Over Settings
        self._gameovertext = gameovertext

        self._enemy_rows = enemy_rows
        self._enemy_cols = enemy_cols

        self._player_speed = player_speed
        self._enemy_speed = enemy_speed
        self._obstacle_speed = obstacle_speed
        self._powerup_speed = powerup_speed
        self._powup_chance = powerup_chance
        self._obstacle_chance = obstacle_chance

        #print("Starting the game...")

        self.build_scene_graph()

    def build_scene_graph(self):
        """Build scene graph for the game demo."""

        the_screen = self._screen
        self._scene_graph = [
            PolygonTitleScene(
                the_screen,
                self._title,
                title_color=self._title_color,
                soundtrack=self._theme.get("title_music", theme.FALLBACK_SND),
                skin=self._skin,
                alttitle = self._alttitle,
                sub1 = self._sub1,
                sub2 = self._sub2,
                pak = self._pak,
                background_color = self._titlebg_color,
                subtitle1_color = self._subtitle1_color,
                subtitle2_color = self._subtitle2_color,
                pak_color = self._pak_color,
                ),
            Level0(
                the_screen,
                soundtrack=self._theme.get("game_music", theme.FALLBACK_SND),
                num_rows=self._enemy_rows,
                num_cols=self._enemy_cols,
                stars=self._stars,
                bg=self._bg,
                bg_speed=self._bg_speed,
                skin=self._skin,
                bg_color = self._gamebg_color,
                player_speed = self._player_speed,
                enemy_speed = self._enemy_speed,
                obstacle_speed = self._obstacle_speed,
                powerup_speed = self._powerup_speed,
                powerup_chance = self._powup_chance,
                obstacle_chance = self._obstacle_chance,
                ),
            LeaderboardScene(
                the_screen,
                0,
                0,
                soundtrack=self._theme.get("leaderboard_music", theme.FALLBACK_SND),
                victorytext=self._victorytext,
                continuetext=self._continuetext,
                background_color = self._leaderboardbg_color
                ),
            GameOverScene(
                the_screen,
                0,
                soundtrack=self._theme.get("gameover_music", theme.FALLBACK_SND),
                skin=self._skin,
                gameovertext=self._gameovertext,
                continuetext=self._continuetext,
                background_color = self._gameoverbg_color
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
                pygame.display.update()
            command = current_scene.end_scene()

            match command:
                case ['q']:
                    self._game_is_over = True
                case ['p']:
                    current_idx = 1
                case ['l', scr]:
                    self._scene_graph[3] = GameOverScene(
                        self._screen,
                        scr,
                        soundtrack=self._theme.get("gameover_music", theme.FALLBACK_SND),
                        skin=self._skin,
                        background_color = self._gameoverbg_color
                    )
                    difficulty = 1.0
                    current_idx = 3
                case ['w', scr]:
                    current_idx = 3
                    self._scene_graph[3] = LeaderboardScene(
                        self._screen,
                        scr[0],
                        scr[1],
                        scr[2],
                        soundtrack=self._theme.get("leaderboard_music", theme.FALLBACK_SND),
                        skin=self._skin,
                        victorytext=self._victorytext,
                        continuetext=self._continuetext,
                        background_color = self._leaderboardbg_color
                        )
                    difficulty = 1.0
                case ['ly', scr]:
                    current_idx = 1
                    diff = diff + self._difficulty_step
                    self._scene_graph[1] = Level0(
                        self._screen,
                        self._theme.get("game_music", theme.FALLBACK_SND),
                        scr[0],
                        scr[1],
                        scr[2],
                        num_rows=self._enemy_rows,
                        num_cols=self._enemy_cols,
                        difficulty=diff,
                        stars=self._stars,
                        bg=self._bg,
                        bg_speed=self._bg_speed,
                        skin=self._skin,
                        bg_color = self._gamebg_color,
                        player_speed = self._player_speed,
                        enemy_speed = self._enemy_speed,
                        obstacle_speed = self._obstacle_speed,
                        powerup_speed = self._powerup_speed,
                        powerup_chance = self._powup_chance,
                        obstacle_chance = self._obstacle_chance,
                        )
                case ['gn']:
                    current_idx = 0
                    self._scene_graph[0] = PolygonTitleScene(
                        self._screen,
                        self._title,
                        title_color=rgbcolors.ghostwhite,
                        soundtrack=self._theme.get("title_music", theme.FALLBACK_SND),
                        skin=self._skin,
                        alttitle = self._alttitle,
                        sub1 = self._sub1,
                        sub2 = self._sub2,
                        pak = self._pak,
                        background_color = self._titlebg_color,
                        subtitle1_color = self._subtitle1_color,
                        subtitle2_color = self._subtitle2_color,
                        pak_color = self._pak_color,
                    )
                    self._scene_graph[1] = Level0(
                        self._screen,
                        soundtrack=self._theme.get("game_music", theme.FALLBACK_SND),
                        num_rows=self._enemy_rows,
                        num_cols=self._enemy_cols,
                        difficulty=diff,
                        stars=self._stars,
                        bg=self._bg,
                        bg_speed=self._bg_speed,
                        skin=self._skin,
                        bg_color = self._gamebg_color,
                        player_speed = self._player_speed,
                        enemy_speed = self._enemy_speed,
                        obstacle_speed = self._obstacle_speed,
                        powerup_speed = self._powerup_speed,
                        powerup_chance = self._powup_chance,
                        obstacle_chance = self._obstacle_chance,
                        )
                    difficulty = 1.0
                case ['gy']:
                    current_idx = 1
                    self._scene_graph[1] = Level0(
                        self._screen,
                        soundtrack=self._theme.get("game_music", theme.FALLBACK_SND),
                        num_rows=self._enemy_rows,
                        num_cols=self._enemy_cols,
                        difficulty=diff,
                        stars=self._stars,
                        bg=self._bg,
                        bg_speed=self._bg_speed,
                        skin=self._skin,
                        bg_color = self._gamebg_color,
                        player_speed = self._player_speed,
                        enemy_speed = self._enemy_speed,
                        obstacle_speed = self._obstacle_speed,
                        powerup_speed = self._powerup_speed,
                        powerup_chance = self._powup_chance,
                        obstacle_chance = self._obstacle_chance,
                        )
                    difficulty = 1.0
        pygame.quit()
        return 0
