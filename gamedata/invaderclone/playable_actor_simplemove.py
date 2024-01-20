import pygame

from .event_actor import EventActor

class PlayableActorSimplemove(EventActor):
    """simplemove simply applies speed in a direction without ac/deceleration"""

    def __init__(
        self,
        screen,
        starting_position,
        sprite,
        player_number,
        controls,
        joystick=None,
        speed=0.,
        vel_init=(0., 0.),
        custom_rect = None,
        restrict_movement = None,
        can_go_oob = False,
        ):

        super().__init__(screen, starting_position, sprite)

        self._player_number = player_number
        self._is_player_1 = player_number == 0

        self._joystick = joystick
        self._controls = controls

        self._speed = speed
        self._velocity = pygame.math.Vector2(vel_init)
        self._can_go_oob = can_go_oob

        self._rect_width = self._size[0] if custom_rect is None else custom_rect[0]
        self._rect_height = self._size[1] if custom_rect is None else custom_rect[1]

        restrictions = [] if restrict_movement is None else [item.strip().lower() for item in restrict_movement]
        self._restrict_px = "x" in restrictions or "+x" in restrictions
        self._restrict_nx = "-x" in restrictions

        self._restrict_py = "y" in restrictions or "+y" in restrictions
        self._restrict_ny = "-y" in restrictions


    def update(self):
        if not self._is_dead:
            vel_x = self._position.x + self._velocity.x
            vel_y = self._position.y + self._velocity.y

            if (
                self._can_go_oob
                or (
                    not self._can_go_oob
                    and 0 <= vel_x <= self._screen_size[0] - self._size[0]
                    and 0 <= vel_y <= self._screen_size[1] - self._size[1]
                    )
                ):
                self._position = pygame.math.Vector2(vel_x, vel_y)
            else:
                self.stop()

    def draw(self):
        if not self._is_dead:
            screen.blit(self._sprite, self._position)

    @property
    def rect(self):
        left = self._position.x
        top = self._position.y
        width = self._rect_width
        height = self._rect_height

        return pygame.Rect(left, top, width, height)

    def process_event(self, event):

        if not self._is_dead:
            up_keys = self._controls["up_keys"]
            down_keys = self._controls["down_keys"]
            left_keys = self._controls["left_keys"]
            right_keys = self._controls["right_keys"]

            movement_keys = up_keys + down_keys + left_keys + right_keys
            fire_keys = fire_keys + fire_joys

            try:
                # Keypad movement
                if self._is_player_1:
                    if event.type == pygame.KEYDOWN:
                        if event.key in left_keys and not self._restrict_nx:
                            self.move_left()
                        elif event.key in right_keys and not self._restrict_px:
                            self.move_right()
                        elif event.key in up_keys and not self._restrict_py:
                            self.move_up()
                        elif event.key in down_keys and not self._restrict_ny:
                            self.move_down()
                    elif event.type == pygame.KEYDOWN and event.key in movement_keys:
                        self.stop()

                # Joystick movement
                if self._joystick is not None:
                    axis = self._joystick.get_axis(0)

                    if -0.1 < axis < 0.1:
                        axis = 0

                    if axis > 0.1:
                        self.move_right(axis)
                    elif axis < -0.1:
                        player.move_left(-axis)
                    elif axis = 0:
                        player.stop()
            except IndexError:
                print("Exception encountered when moving player. Trying not to crash the thread.")

    def stop(self):
        self._velocity = pygame.math.Vector2(0.,0.)

    def move_up(self, axis_mult=1.):
        speed = self._speed * axis_mult
        if speed < 0.:
            speed = 0.
        self._velocity = pygame.math.Vector2(0., -speed)

    def move_down(self, axis_mult = 1.):
        speed = self._speed * axis_mult
        if speed < 0.:
            speed = 0.
        self._velocity = pygame.math.Vector2(0., speed)

    def move_left(self, axis_mult = 1.):
        speed = self._speed * axis_mult
        if speed < 0.:
            speed = 0.
        self._velocity = pygame.math.Vector2(-speed, 0.)

    def move_right(self, axis_mult = 1.):
        speed = self._speed * axis_mult
        if speed < 0.:
            speed = 0.
        self._velocity = pygame.math.Vector2(speed, 0.)
