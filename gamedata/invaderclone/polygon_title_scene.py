"""Implements the Title screen"""

import pygame

from .press_any_key_to_exit_scene import PressAnyKeyToExitScene
from . import rgbcolors
from . import theme

class PolygonTitleScene(PressAnyKeyToExitScene):
    """Scene with a title string and a polygon."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        screen,
        game_settings,
        soundtrack=None,
    ):
        """Initialize the scene."""

        super().__init__(screen, game_settings, game_settings['title_music'])

        self._title = None
        self._subtitle = None
        self._subtitle_en = None
        self._press_any_key = None
        img = None
        self._title_img = None
        self.update_settings()

    def reset_scene(self):
        super().reset_scene()

        self.__init__(self._screen, self._game_settings)

    def update_settings(self, new_settings = None):
        super().update_settings()
        gs = self._game_settings if new_settings is None else new_settings
        cd = rgbcolors.color_dictionary

        self._background.fill(cd[gs["title_bg_color"]])

        SUBTITLE1_COLOR = cd[gs["subtitle1_text_color"]]
        SUBTITLE2_COLOR = cd[gs["subtitle2_text_color"]]
        PAK_COLOR = cd[gs["press_any_key_text_color"]]

        if SUBTITLE1_COLOR is None:
            SUBTITLE1_COLOR = cd[gs["title_text_color"]]
        if SUBTITLE2_COLOR is None:
            SUBTITLE2_COLOR = cd[gs["subtitle1_text_color"]] if cd[gs["subtitle1_text_color"]] is not None else cd[gs["title_text_color"]]
        if PAK_COLOR is None:
            PAK_COLOR = cd[gs["title_text_color"]]

        screen_height = self._screen.get_height()

        title_modded_size = screen_height // 11
        subtitle_size = screen_height // 50
        string_size = screen_height // 44
        subpixel_size = screen_height // 47

        title_font = pygame.font.Font(self._theme.get("titlefont", theme.FALLBACK_FNT), title_modded_size)

        subtitle_font = pygame.font.Font(self._theme.get("titlefont", theme.FALLBACK_FNT), subtitle_size)

        string_font = pygame.font.Font(self._theme.get("pixelfont", theme.FALLBACK_FNT), string_size)
        subpixel_font = pygame.font.Font(self._theme.get("pixelfont", theme.FALLBACK_FNT), subpixel_size)


        TITLE = gs["name"] if gs["alt_title"] is None else gs["alt_title"]
        self._title = pygame.font.Font.render(
            title_font,
            TITLE,
            True,
            cd[gs["title_text_color"]])

        self._subtitle = pygame.font.Font.render(
            subtitle_font,
            gs["subtitle1"],
            True,
            SUBTITLE1_COLOR,
        )

        self._subtitle_en = pygame.font.Font.render(
            subpixel_font,
            gs["subtitle2"],
            True,
            SUBTITLE2_COLOR,
        )

        self._press_any_key = pygame.font.Font.render(
            string_font, gs["press_any_key"], True, PAK_COLOR
        )

        _, height = self._screen.get_size()
        img_size = height // 8

        img = pygame.image.load(self._theme.get("title_icon", theme.FALLBACK_IMG)).convert_alpha()

        self._title_img = pygame.transform.scale(img, (img_size, img_size))

    def draw(self):
        """Draw the scene."""
        super().draw()

        s_w, s_h = self._screen.get_size()

        b_x, b_y = self._title_img.get_size()

        self._screen.blit(
            self._title_img, ((s_w // 2) - (b_x // 2), (s_h // 2) + (b_y // 2))
        )

        t_x, t_y = self._title.get_size()

        self._screen.blit(
            self._title,
            ((s_w // 2) - t_x // 2,
             (s_h // 2) - t_y // 2))

        sjp_x, sjp_y = self._subtitle.get_size()
        sen_x, sen_y = self._subtitle_en.get_size()

        jp_offset = t_y + b_y + (t_y // 2)
        en_offset = jp_offset + sen_y + (sjp_y // 2)

        self._screen.blit(
            self._subtitle,
            ((s_w // 2) - (sjp_x // 2), (s_h // 2) - (sjp_y // 2) + jp_offset),
        )

        self._screen.blit(
            self._subtitle_en,
            ((s_w // 2) - (sen_x // 2), (s_h // 2) - (sen_y // 2) + en_offset),
        )

        p_x = self._press_any_key.get_width()

        self._screen.blit(
            self._press_any_key,
            ((s_w // 2) - p_x // 2, s_h - 50))

