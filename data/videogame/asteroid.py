"""An asteroid sprite"""

import pygame

from . import assets


class Asteroid:
    """Represents an asteroid"""

    def __init__(self, position, img_asset):
        """Initialize an asteroid"""

        self._position = position
        self._sprite = pygame.image.load(img_asset).convert_alpha()

    @property
    def rect(self):
        """Get an asteroid's rect"""

        a_x = self._position.x
        a_y = self._position.y
        a_w = self._sprite.get_width()
        a_h = self._sprite.get_height()
        return pygame.Rect(a_x, a_y, a_w, a_h)

    def draw(self, screen):
        """Draw an asteroid"""
        screen.blit(self._sprite, self._position)
