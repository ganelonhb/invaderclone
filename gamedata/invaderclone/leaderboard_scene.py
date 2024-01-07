"""implements a leaderboard scene"""

import pygame

from .press_any_key_to_exit_scene import PressAnyKeyToExitScene
from . import rgbcolors
from . import theme
from .constants import save_path

from datetime import datetime
import time

class LeaderboardScene(PressAnyKeyToExitScene):
    """a leaderboard"""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        screen,
        game_settings,
        soundtrack=None,
    ):
        """initialize a leaderboard"""
        super().__init__(screen, game_settings, game_settings['leaderboard_music'])

        self._score = None
        self._lives_p1 = None
        self._lives = None
        self._lives_p2 = None
        self._y = False

        self._you_win = None

        self._lb_font = None

        self._confirm_screen = None
        self.update_settings()

    def reset_scene(self):
        super().reset_scene()

        self.__init__(self._screen, self._game_settings)

    def process_event(self, event):
        """Process game events."""

        if time.time() >= self._timestart + 3:
            if (
                event.type == pygame.KEYDOWN and event.key == pygame.K_y
                or
                event.type == pygame.JOYBUTTONDOWN and event.button == 0):
                self._y = True

            super().process_event(event)

    def set_score(self, value):
        """set the score"""

        self._score = value

    def update_settings(self, new_settings = None):
        super().update_settings()
        gs = self._game_settings
        cd = rgbcolors.color_dictionary

        screen_height = self._screen.get_height()

        title_font_size = screen_height // 11
        lb_font_size = confirm_font_size = screen_height // 57

        string_font = pygame.font.Font(self._theme.get("pixelfont", theme.FALLBACK_FNT), title_font_size)
        self._score = gs["current_score_p1"]
        self._score_p2 = gs["current_score_p2"]
        self._lives = gs["current_lives_p1"]
        self._lives_p2 = gs["current_lives_p2"]

        self._you_win = pygame.font.Font.render(
            string_font, gs["victory"], True, cd[gs["victory_text_color"]]
        )

        # pylint: disable=redefined-outer-name
        leaderboard = [f"{count + 1}. {word[0]} - {word[1]}"
                       for count, word in enumerate(self._leaderboard.scores)]

        lb_font = pygame.font.Font(self._theme.get("pixelfont", theme.FALLBACK_FNT), lb_font_size)

        self._lb_font = [pygame.font.Font.render(
            lb_font,
            phrase,
            True,
            rgbcolors.ghostwhite
            ) for phrase in leaderboard]

        confirm_font = pygame.font.Font(self._theme.get("pixelfont", theme.FALLBACK_FNT), confirm_font_size)

        self._confirm_screen = pygame.font.Font.render(
            confirm_font, gs["continueyn"], True, rgbcolors.ghostwhite
        )


    def draw(self):
        """Draw the scene."""
        super().draw()

        s_w, s_h = self._screen.get_size()

        t_x, t_y = self._you_win.get_size()

        self._screen.blit(self._you_win, ((s_w // 2) - t_x // 2, 50))

        if self._lb_font:
            l_x, _ = min(
                self._lb_font,
                key=lambda e: e.get_width()).get_size()

            posx = (s_w // 2) - l_x // 2
            posy = 50 + t_y + (t_y // 4)
            position = (posx, posy)
            for num, line in enumerate(self._lb_font):
                self._screen.blit(
                    line,
                    (position[0],
                     position[1] + (num * 14) + (num * 4)))

        if time.time() >= self._timestart + 3:
            p_x = self._confirm_screen.get_width()
            p_y = self._confirm_screen.get_height()

            self._screen.blit(
                self._confirm_screen,
                ((s_w // 2) - p_x // 2, s_h - (50 + p_y) + (s_w // 100)))

    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

        lblen = len(self._leaderboard.scores)
        if lblen < 10 or self._score > self._leaderboard.lowest[0]:
            self._leaderboard.add_score((self._score, datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")))
            self._leaderboard.save(save_path)

        yes = self._y
        self._y = False

        if self._quit:
            return ["QUIT_GAME"]
        elif yes and self._lives == 0:
            return ["RST_CHANGE_SCENE", "Level0"]
        elif not yes:
            return ["RST_CHANGE_SCENE", "PolygonTitleScene"]
        else:
            return ["CHANGE_LEVEL"]

        return ["RST_CHANGE_SCENE"]
