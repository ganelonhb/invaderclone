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
        title,
        title_color=rgbcolors.ghostwhite,
        title_size=72,
        background_color=rgbcolors.black,
        soundtrack=None,
        skin="default",
        alttitle = None,
        sub1 = "全部のネコ宇宙人を倒す！ 動く：'←'／'→' 撃つ：'SPACE'",
        sub2 = "Kill all cat aliens! Move: '←'/'→' Shoot: 'SPACE'",
        pak = "Press ANY KEY!",
        subtitle1_color=None,
        subtitle2_color=None,
        pak_color=None,
    ):
        """Initialize the scene."""

        super().__init__(screen, background_color, soundtrack, skin=skin)
        SUBTITLE1_COLOR = subtitle1_color
        SUBTITLE2_COLOR = subtitle2_color
        PAK_COLOR = pak_color

        if subtitle1_color is None:
            SUBTITLE1_COLOR = title_color
        if subtitle2_color is None:
            SUBTITLE2_COLOR = subtitle1_color if subtitle1_color is not None else title_color
        if pak_color is None:
            PAK_COLOR = title_color

        screen_height = screen.get_height()

        title_modded_size = screen_height // 11
        subtitle_size = screen_height // 50
        string_size = screen_height // 44
        subpixel_size = screen_height // 47

        title_font = pygame.font.Font(self._theme.get("titlefont", theme.FALLBACK_FNT), title_modded_size)

        subtitle_font = pygame.font.Font(self._theme.get("titlefont", theme.FALLBACK_FNT), subtitle_size)

        string_font = pygame.font.Font(self._theme.get("pixelfont", theme.FALLBACK_FNT), string_size)
        subpixel_font = pygame.font.Font(self._theme.get("pixelfont", theme.FALLBACK_FNT), subpixel_size)


        TITLE = title if alttitle is None else alttitle
        self._title = pygame.font.Font.render(
            title_font,
            TITLE,
            True,
            title_color)

        self._subtitle = pygame.font.Font.render(
            subtitle_font,
            sub1,
            True,
            SUBTITLE1_COLOR,
        )

        self._subtitle_en = pygame.font.Font.render(
            subpixel_font,
            sub2,
            True,
            SUBTITLE2_COLOR,
        )

        self._press_any_key = pygame.font.Font.render(
            string_font, pak, True, PAK_COLOR
        )

        _, height = screen.get_size()
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

