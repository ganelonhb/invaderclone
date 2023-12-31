"""A player character."""

import time
import pygame


class Player:
    """A player."""

    def __init__(self, position, screen, character, player_speed=15):
        """initialize a player character"""

        self._width, self._height = screen.get_size()
        self._position = position
        self._size = character.get_width()
        self._velocity = pygame.math.Vector2(0, 0)
        self.is_dead = False
        self._invincible = 0
        self._sprite = character
        self._speed = player_speed

        self._powerup = None
        self._powerup_timer = 0
        self._powerup_max = 0

    def update(self):
        """update the posiition of the player"""

        vel = self._position.x + self._velocity.x
        if 0 < vel < self._width - self._size:
            self._position = self._position + self._velocity

        _ = self.powered_up

    @property
    def width(self):
        """get the width of the player"""

        return self._size

    @property
    def powerup(self):
        """get the current powerup"""

        return self._powerup

    @property
    def powered_up(self):
        """determine if the powerup timer is over"""

        if self._powerup is None:
            return False

        if self._powerup_max < 0:
            return True

        if self._powerup_timer + self._powerup_max < time.time():
            self._powerup = None
            self._powerup_time = 0
            self._powerup_max = 0
            return False

        return True

    def set_powerup(self, name, max_time=15):
        """set the powerup"""

        self._powerup = name
        self._powerup_timer = time.time()
        self._powerup_max = max_time


    @property
    def position(self):
        """Get Position"""

        return self._position

    @property
    def invincible(self):
        """Determine if the player is invincible"""

        if not self._invincible:
            return False

        if self._invincible + 1 < time.time():
            self._invincible = 0
            return False

        return True

    def invincible_clock(self):
        """make the player invincible"""

        self._invincible = time.time()

    @position.setter
    def position(self, value):
        """set the posiition of the ship"""

        self.stop()
        self._position = value

    @property
    def rect(self):
        """get the rect"""

        left = self._position.x
        top = self._position.y
        width = self._size
        return pygame.Rect(left, top, width, width)

    def stop(self):
        """Stop the player"""
        self._velocity = pygame.math.Vector2(0, 0)

    def move_left(self, axis_mult=1):
        """Move the player character left"""
        speed = -int(self._speed * abs(axis_mult) + 0.5)
        if speed > -1:
            speed = -1
        self._velocity = pygame.math.Vector2(speed, 0)

    def move_right(self, axis_mult=1):
        """Move the player character right"""
        speed = int(self._speed * abs(axis_mult) + 0.5)
        if speed < 1:
            speed = 1
        self._velocity = pygame.math.Vector2(speed, 0)

    def _move(self, vel):
        """move the player"""
        self._position = self._position + vel

    def draw(self, screen):
        """Draw the circle to a given screen"""
        if not self.is_dead:
            screen.blit(self._sprite, self._position)
