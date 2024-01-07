"""Implements a Game Over Scene"""

import pygame

import time

from .press_any_key_to_exit_scene import PressAnyKeyToExitScene
from . import rgbcolors
from . import theme

class GameOverScene(PressAnyKeyToExitScene):
    """a game over scene"""

    def __init__(
        self,
        screen,
        game_settings,
        soundtrack=None,
    ):
        """initialize a game over scene"""

        super().__init__(screen, game_settings, game_settings['gameover_music'])

        self._y = False

        self._score = None
        self._score_p2 = None
        self._game_over = None
        self._confirm_screen = None
        self._score_message = None
        self._title_img = None

        self.update_settings()

    def update_settings(self, new_settings=None):
        gs = self._game_settings if new_settings is None else new_settings
        cd = rgbcolors.color_dictionary

        screen_height = self._screen.get_height()
        title_font_size = screen_height // 11
        confirm_font_size = screen_height // 57

        string_font = pygame.font.Font(self._theme.get("pixelfont", theme.FALLBACK_FNT), title_font_size)

        self._score = gs["current_score_p1"]
        self._score_p2 = gs["current_score_p2"]

        self._game_over = pygame.font.Font.render(
            string_font, gs["game_over"], True, cd[gs["game_over_text_color"]]
        )

        confirm_font = pygame.font.Font(self._theme.get("pixelfont", theme.FALLBACK_FNT), confirm_font_size)

        self._confirm_screen = pygame.font.Font.render(
            confirm_font, gs["continueyn"], True, cd[gs["continueyn_text_color"]]
        )

        grammar = "points" if gs["current_score_p1"] != 1 else "point"

        score = gs["current_score_p1"]

        self._score_message = pygame.font.Font.render(
            confirm_font,
            f"You scored {score} {grammar}.",
            True,
            cd[gs["game_over_text_color"]]
        )

        img = pygame.image.load(self._theme.get("gameover_icon", theme.FALLBACK_IMG)).convert_alpha()

        height = screen_height // 8

        self._title_img = pygame.transform.scale(img, (height, height))


    def process_event(self, event):
        """Process game events."""

        if time.time() >= self._timestart + 3:
            if (
                event.type == pygame.KEYDOWN and event.key == pygame.K_y
                or
                event.type == pygame.JOYBUTTONDOWN and event.button == 0):
                self._y = True

            super().process_event(event)

    def set_score(self, val):
        """set the score"""

        self._score = val

    def draw(self):
        """Draw the scene."""
        super().draw()

        s_w, s_h = self._screen.get_size()

        b_x, b_y = self._title_img.get_size()

        self._screen.blit(
            self._title_img, ((s_w // 2) - (b_x // 2), (s_h // 2) + (b_y // 2))
        )

        t_x, t_y = self._game_over.get_size()

        self._screen.blit(
            self._game_over, ((s_w // 2) - t_x // 2, (s_h // 2) - t_y // 2)
        )

        if time.time() >= self._timestart + 3:
            p_x = self._confirm_screen.get_width()
            p_y = self._confirm_screen.get_height()

            self._screen.blit(
                self._confirm_screen,
                ((s_w // 2) - p_x // 2, s_h - (50 + p_y)))

        s_x, s_y = self._score_message.get_size()

        self._screen.blit(
            self._score_message,
            ((s_w // 2) - s_x // 2,
             (s_h // 2) - (s_y // 2) - (50 + (t_y // 2)))
        )

    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

        yes = self._y
        self._y = False

        if self._quit:
            return ["QUIT_GAME"]
        if yes:
            return ['RST_CHANGE_SCENE', "Level0"]

        return ['RST_CHANGE_SCENE', "PolygonTitleScene"]
