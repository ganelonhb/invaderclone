"""implements a powerup"""

import pygame

from .bullets import Bullet

class BurstShotPowerup(Bullet):
    """Shoot a burst of bullets"""

    def __init__(self, position, target_position, speed, img, maxtime=3):
        """initialize an instance of the burst shot powerup"""

        super().__init__(position, target_position, speed)

        self._maxtime = maxtime
        self._img = pygame.image.load(
            img
            )

    @property
    def rect(self):
        """bounding rect"""

        left = self._position.x
        top = self._position.y
        width = self._img.get_width()
        height = self._img.get_height()
        return pygame.Rect(left, top, width, height)

    @property
    def maxtime(self):
        """get the max time of a power up"""

        return self._maxtime


    def draw(self, screen):
        """draw the powerup to the screen"""

        screen.blit(self._img, self._position)
