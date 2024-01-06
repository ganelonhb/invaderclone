"""Implements bullets"""

import math
import pygame

from . import rgbcolors


class Bullet:
    """Implement a generic bullet"""

    def __init__(self, position, target_position, speed, bulletimg=None):
        """Initialize a bullet"""

        self._position = pygame.math.Vector2(position)
        self._target_position = pygame.math.Vector2(target_position)
        self._speed = speed
        if bulletimg is not None:
            self._img = bulletimg
            self._width = self._img.get_width()
            self._height = self._img.get_height()
        else:
            self._img = None
            self._width = 4
            self._height = 8

    def should_die(self):
        """determine if a bullet should die"""

        squared_distance = (
            self._position - self._target_position
            ).length_squared()
        return math.isclose(squared_distance, 0.0, rel_tol=1e-01)

    def draw(self, screen):
        """draw an enemy bullet"""

        if self._img is not None:
            screen.blit(self._img, self._position)
        else:
            pygame.draw.rect(screen, rgbcolors.ghostwhite, self.rect)

    @property
    def rect(self):
        """bounding rect"""

        left = self._position.x
        top = self._position.y
        width = self._width
        height = self._height
        return pygame.Rect(left, top, width, height)

    def update(self):
        """update the position of a bullet"""

        self._position.move_towards_ip(self._target_position, self._speed)


class PlayerBullet(Bullet):
    """Implements a player's bullet"""

    def __init__self(self, position, target_position, speed, bulletimg=None):
        super.__init__(self, position, target_position, speed, bulletimg)


class PlayerBulletOneThird(Bullet):
    """implements a player bullet that costs 1/3rd the price when lost"""

    def __init__self(self, position, target_position, speed, bulletimg=None):
        super.__init__(self, position, target_position, speed, bulletimg)


class EnemyBullet(Bullet):
    """implement an enemy bullet"""

    def __init__self(self, position, target_position, speed, bulletimg=None):
        super.__init__(self, position, target_position, speed, bulletimg)


