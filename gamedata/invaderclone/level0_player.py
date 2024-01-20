import time

from .playable_actor_simplemove import PlayableActorSimplemove as PlayableActor

class Level0Player(PlayableActor):
    def __init__(
        self,
        screen,
        starting_position,
        sprite,
        player_number,
        controls,
        bullets,
        bullet_speed=15.,
        joystick=None,
        speed=15.,
        ):
        super().__init(
            screen,
            starting_position,
            sprite,
            player_number,
            controls,
            joystick,
            speed,
            (0.,0.),
            None,
            ["-y", "+y"],
            False,
            )

        self._bullets = bullets
        self._bullet_speed = bullet_speed
        self._invincible = 0
        self._invincible_max = 1
        self._powerup = None
        self._powerup_timer = 0
        self._powerup_max = 0

        self._timestart = time.time()
        self._lastshot = 0

    def update(self):
        super().update()

        if not self._is_dead:
            self._auto_shoot()

    @property
    def powerup(self):
        return self._powerup

    @property
    def powered_up(self):
        if self._powerup is None:
            return False
        elif self._powerup_timer + self._powerup_max < time.time():
            self._powerup = None
            self._powerup_timer = 0
            self._powerup_max = 0
            return False

        return True

    def set_powerup(self, name, max_time=15):
        self._powerup = name
        self._powerup_timer = time.time()
        self._powerup_max = max_time

    def process_event(self, event):
        super().process_event(event)

        if not self._is_dead:
            fire_keys = self._controls["fire_keys"]
            fire_joys = self._controls["fire_joys"]

            fire_controls = fire_keys + fire_joys

            if (
                event.key in fire_controls
                and event.instance_id == self._joystick.get_instance_id()
                ):
                self.manual_shoot()

    def _auto_shoot(self):
        if not self._is_dead:
            fire_keys = self._controls["fire_keys"]
            fire_joys = self._controls["fire_joys"]

            fire_controls = fire_keys + fire_joys

            current_time = int((time.time() - self._timestart) * 1000)
            if (
                override,
                or ()
                )

    @property
    def invincible(self):
        if not self._invincible:
            return False
        elif self._invincible + self._invincible_max < time.time():
            self._invincible = 0
            return False

        return True

    def invincible_clock(self):
        self._invincible = time.time()


