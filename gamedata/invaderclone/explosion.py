"""An explosion animation"""

import pygame


# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
class Explosion:
    """An explosion"""

    def __init__(self, actor, sprite, size):
        """Initialize an Explosion"""
        self._defaultlife = 9
        self._animcycle = 3
        img = pygame.transform.scale(sprite, (size, size))
        self._images = []
        if not self._images:
            self._images = [img.convert_alpha(),
                            pygame.transform.flip(img, 1, 1).convert_alpha()]

        anim_x, anim_y = actor.rect.center
        self._position = actor.position

        self.image = self._images[0]
        self.rect = self.image.get_rect(center=(anim_x, anim_y))
        self.life = self._defaultlife
        self._actor = actor

        self.should_die = False

    def update(self):
        """Update the explosion animation"""
        self.life = self.life - 1
        self.image = self._images[self.life // self._animcycle % 2]
        if self.life <= 0:
            self.should_die = True
            self._actor.is_exploding = False

    def draw(self, screen):

        if not self.should_die:
            screen.blit(self.image, self._position)
