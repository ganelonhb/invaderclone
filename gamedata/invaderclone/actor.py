
import pygame

class Actor:
    def __init__(
        self,
        screen,
        starting_position,
        sprite,
        ):
        self._screen = screen
        self._position = pygame.math.Vector2(starting_position)
        self._sprite = sprite,
        self._is_dead = False

        self._screen_size = screen.get_size()
        self._size = sprite.get_size()


    def update(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

    @property
    def rect(self):
        raise NotImplementedError

    @property
    def should_die(self):
        return self._is_dead

    @should_die.setter
    def should_die(self, value):
        self._should_die = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def width(self):
        return self._size[0]

    @property
    def height(self):
        return self._size[1]



