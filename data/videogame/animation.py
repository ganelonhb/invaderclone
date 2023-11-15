"""An explosion animation"""

import pygame

from . import assets


# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
class Explosion(pygame.sprite.Sprite):
    """An explosion"""

    def __init__(self, actor, sprite, size=32):
        """Initialize an Explosion"""
        pygame.sprite.Sprite.__init__(self, self.containers)
        self._sprite = sprite
        self._defaultlife = 6
        self._animcycle = 3
        self._images = []
        try:
            surface = pygame.image.load(self._sprite).convert_alpha()
        except pygame.error as error:
            raise SystemExit(
                    f"Could not load image at {self._sprite}") from error
        img = surface
        img = pygame.transform.scale(img, (size, size)).convert_alpha()
        if not self._images:
            self._images = [img,
                            pygame.transform.flip(img, 1, 1).convert_alpha()]

        anim_x, anim_y = actor.rect.center

        self.image = self._images[0].convert_alpha()
        self.rect = self.image.get_rect(center=(anim_x, anim_y))
        self.life = self._defaultlife
        self._actor = actor

    def update(self):
        """Update the explosion animation"""
        self.life = self.life - 1
        self.image = self._images[self.life // self._animcycle % 2].convert_alpha()
        if self.life <= 0:
            self.kill()
            self._actor.is_exploding = False
