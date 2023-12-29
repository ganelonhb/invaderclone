"""implement an enemy ship"""

import pygame

# import rgbcolors


# pylint: disable=too-many-instance-attributes
class EnemyShip:
    """An enemy space ship"""

    def __init__(self, position, screen, sprite, speed=5):
        """initialize an enemy ship"""

        self._screen = screen
        self._position = position
        self._width, self._height = screen.get_size()
        self._character_width = sprite.get_width()
        width = (self._character_width, self._character_width)
        self._is_exploding = False
        self._sprite = sprite
        self._velocity = pygame.math.Vector2(0, 0)
        self._target_pos = None
        self._original_pos = position
        self._stop = False
        self._speed = speed

    def update(self):
        """update an enemy ship"""

        t_x = self._target_pos.x
        t_y = self._target_pos.y
        if not self._stop and self._position.distance_to((t_x, t_y)):
            self._position.move_towards_ip(self._target_pos, self._speed)

    @property
    def speed(self):
        """get the speed of the ship"""

        return self._speed

    def inc_speed(self, val=2):
        """increment the speed by a value"""

        self._speed = self._speed + val

    def stop(self):
        """stop the enemy"""

        self._stop = True

    @property
    def at_pos(self):
        """determine if the enemy is at its target"""

        t_x = self._target_pos.x
        t_y = self._target_pos.y
        return not self._position.distance_to((t_x, t_y))

    @property
    def width(self):
        """get the width of the enemy"""

        return self._character_width

    @property
    def rect(self):
        """get the rect of the enemy ship"""

        left = self._position.x  # - (self._width // 4)
        top = self._position.y  # - (self._width // 4)
        width = self._character_width
        return pygame.Rect(left, top, width, width)

    @property
    def below_rect(self):
        """rect that detects things below"""

        left = self._position.x
        top = self._position.y + self._character_width
        width = self._character_width
        height, _ = self._screen.get_size()
        return pygame.Rect(left, top, width, height)

    @property
    def position(self):
        """get the position of the enemy"""

        return self._position

    @position.setter
    def position(self, val):
        """set the position of the enemy"""

        self._position = val

    @property
    def original_position(self):
        """get the original position of the enemy"""

        return self._original_position

    @original_position.setter
    def original_position(self, val):
        """set the original position"""

        self._original_position = val

    @property
    def target(self):
        """get the target position"""

        return self._target_pos

    @target.setter
    def target(self, val):
        """set the target"""

        self._target_pos = val

    @property
    def height(self):
        """get the height of the ship"""

        return self._character_width

    @property
    def is_exploding(self):
        """determine if the ship is exploding"""

        return self._is_exploding

    @is_exploding.setter
    def is_exploding(self, val):
        """set whether or not the ship is exploding"""

        self._is_exploding = val

    def draw(self, screen):
        """draw the ship"""

        screen.blit(self._sprite, self.position)
        # pygame.draw.rect(screen, rgbcolors.red, self.below_rect)
