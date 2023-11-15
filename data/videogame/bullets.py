"""Implements bullets"""

import math
import pygame

from . import rgbcolors


class Bullet:
    """Implement a generic bullet"""

    def __init__(self, position, target_position, speed, width=4, height=6, bulletimg=None):
        """Initialize a bullet"""

        self._position = pygame.math.Vector2(position)
        self._target_position = pygame.math.Vector2(target_position)
        self._speed = speed
        self._width = width
        self._height= height

    def should_die(self):
        """determine if a bullet should die"""

        squared_distance =  (self._position
                            - self._target_position).length_squared()
        return math.isclose(squared_distance, 0.0, rel_tol=1e-01)

    def update(self):
        """update the position of a bullet"""

        self._position.move_towards_ip(self._target_position, self._speed)

    def draw(self, screen):
        """draw a bullet"""

        raise NotImplementedError


class PlayerBullet(Bullet):
    """Implements a player's bullet"""

    @property
    def rect(self):
        """bounding rect"""

        left = self._position.x
        top = self._position.y
        width = self._width
        height = self._height
        return pygame.Rect(left, top, width, height)

    def draw(self, screen):
        """draw a player bullet"""

        pygame.draw.rect(screen, rgbcolors.ghostwhite, self.rect)

class PlayerBulletOneThird(Bullet):
    """implements a player bullet that costs 1/3rd the price when lost"""

    @property
    def rect(self):
        """bounding rect"""

        left = self._position.x
        top = self._position.y
        width = self._width
        height = self._height
        return pygame.Rect(left, top, width, height)

    def draw(self, screen):
        """draw a player bullet"""

        pygame.draw.rect(screen, rgbcolors.ghostwhite, self.rect)


class EnemyBullet(Bullet):
    """implement an enemy bullet"""

    @property
    def rect(self):
        """bounding rect"""

        left = self._position.x
        top = self._position.y
        width = 6
        height = 6
        return pygame.Rect(left, top, width, height)

    def draw(self, screen):
        """draw an enemy bullet"""

        rect1_left = self._position.x + 2
        rect1_top = self._position.y
        rect1_w = 2
        rect1_h = 6

        rect2_left = self._position.x
        rect2_top = self._position.y + 1
        rect2_w = 4
        rect2_h = 6

        rect1 = pygame.Rect(rect1_left, rect1_top, rect1_w, rect1_h)
        rect2 = pygame.Rect(rect2_left, rect2_top, rect2_w, rect2_h)

        pygame.draw.rect(screen, rgbcolors.ghostwhite, rect1)
        pygame.draw.rect(screen, rgbcolors.ghostwhite, rect2)
