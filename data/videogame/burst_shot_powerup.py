"""implements a powerup"""

import pygame

from .bullets import Bullet

class BurstShotPowerup(Bullet):
    """Shoot a burst of bullets"""

    def __init__(self, position, target_position, speed, img, maxtime=3):
        """initialize an instance of the burst shot powerup"""

        super().__init__(position, target_position, speed, img)

        self._maxtime = maxtime

    @property
    def maxtime(self):
        """get the max time of a power up"""

        return self._maxtime
