"""An obstacle that descends from the top of the screen (like powerup)"""

import pygame

from .bullets import Bullet

class Obstacle(Bullet):
    """Obstacle that descends from the screen"""

    def __init__(self, position, target_position, speed, img):
        """initialize an instance of the obstacle"""

        super().__init__(position, target_position, speed)

        self._img = img

    @property
    def height(self):
        return self._img.get_height()

    @property
    def width(self):
        return self._img.get_width()

    @property
    def rect(self):
        """bounding rect"""

        left = self._position.x
        top = self._position.y
        width = self._img.get_width()
        height = self._img.get_height()
        return pygame.Rect(left, top, width, height)

    def draw(self, screen):
        """draw the powerup to the screen"""

        screen.blit(self._img, self._position)
