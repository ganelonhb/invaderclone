"""Scene objects for making games with PyGame."""

from random import randint, choice, randrange
from sys import platform
from os import path, makedirs
from datetime import datetime
import time
import pygame
import threading

from . import rgbcolors
from . import assets
from . import player
from .animation import Explosion
from .enemy import EnemyShip
from . import bullets
from .asteroid import Asteroid
from . import leaderboard
from . import powerup
from .obstacle import Obstacle

UNIX_SYSTEMS = ["aix", "darwin", "freebsd", "linux", "openbsd"]
WINDOWS_SYSTEMS = ["win32", "win64", "cygwin", "msys", "nt"]

save_path = path.join(path.expanduser('~'), ".config", "invaderclone") if platform in UNIX_SYSTEMS else path.join(path.expanduser('~'), "Documents", "invaderclone")
file_name = path.join(save_path, "scores.pkle")

_PLAYER_SIZE_MODIFIER = 12
_ENEMY_SIZE_MODIFIER = 24

# pylint: disable=too-many-instance-attributes
class Scene:
    """Base class for making PyGame Scenes."""

    def __init__(self, screen, background_color, soundtrack=None, skin="default"):
        """Scene initializer"""
        self._theme = assets.Theme(skin)

        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(background_color)
        self._frame_rate = 60
        self._is_valid = True
        self._soundtrack = soundtrack
        self._render_updates = None
        self._next_scene = None
        self._quit = False
        self._timestart = time.time()


        self._joysticks = None

        self._make_joysticks()

        if not path.exists(save_path):
            makedirs(save_path)
        if not path.exists(file_name):
            leaderboard.Leaderboard().save(save_path)

        self._leaderboard = leaderboard.create_leaderboard_from_pickle(
            file_name)

    def _make_joysticks(self):
        """make a list of joysticks"""
        if pygame.joystick.get_count() > 0:
            self._joysticks = [
                pygame.joystick.Joystick(x)
                for x in range(pygame.joystick.get_count())
                ]

    def clock(self):
        """Reset the scene clock."""

        self._timestart = time.time()

    def draw(self):
        """Draw the scene."""
        self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        """Process a game event by the scene."""
        if event.type == pygame.QUIT:
            self._quit = True
            self._is_valid = False
        if (
            event.type == pygame.JOYDEVICEADDED
            or
            event.type == pygame.JOYDEVICEREMOVED):
            self._make_joysticks()
        if (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            or
            event.type == pygame.JOYBUTTONDOWN and event.button == 8):
            self._is_valid = False
            self._quit = True

    def is_valid(self):
        """Is the scene valid? A valid scene can be used to play a scene."""
        return self._is_valid

    def render_updates(self):
        """Render all sprite updates."""
        pass

    def update_scene(self):
        """Update the scene state."""
        pass

    def start_scene(self):
        """Start the scene."""
        if self._soundtrack:
            try:
                pygame.mixer.music.load(self._soundtrack)
                pygame.mixer.music.set_volume(0.2)
            except pygame.error as pygame_error:
                print("Cannot open the mixer?")
                print("\n".join(pygame_error.args))
                raise SystemExit("broken!!") from pygame_error
            pygame.mixer.music.play(-1)

    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

        if self._quit:
            return ["q"]

        return ["p"]

    def frame_rate(self):
        """Return the frame rate the scene desires."""
        return self._frame_rate

    @property
    def next_scene(self):
        """return the next scene, as set by each individual scene"""

        return self._next_scene


class PressAnyKeyToExitScene(Scene):
    """Empty scene where it will invalidate when a key is pressed."""

    def process_event(self, event):
        """Process game events."""
        super().process_event(event)

        if event.type == pygame.KEYDOWN or event.type == pygame.JOYBUTTONDOWN:
            self._is_valid = False


class PolygonTitleScene(PressAnyKeyToExitScene):
    """Scene with a title string and a polygon."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        screen,
        title,
        title_color=rgbcolors.ghostwhite,
        title_size=72,
        background_color=rgbcolors.black,
        soundtrack=None,
        skin="default",
        alttitle = None,
        sub1 = "全部のネコ宇宙人を倒す！ 動く：'←'／'→' 撃つ：'SPACE'",
        sub2 = "Kill all cat aliens! Move: '←'/'→' Shoot: 'SPACE'",
        pak = "Press ANY KEY!",
        subtitle1_color=None,
        subtitle2_color=None,
        pak_color=None,
    ):
        """Initialize the scene."""

        super().__init__(screen, background_color, soundtrack, skin=skin)
        SUBTITLE1_COLOR = subtitle1_color
        SUBTITLE2_COLOR = subtitle2_color
        PAK_COLOR = pak_color

        if subtitle1_color is None:
            SUBTITLE1_COLOR = title_color
        if subtitle2_color is None:
            SUBTITLE2_COLOR = subtitle1_color if subtitle1_color is not None else title_color
        if pak_color is None:
            PAK_COLOR = title_color

        screen_height = screen.get_height()

        title_modded_size = screen_height // 11
        subtitle_size = screen_height // 50
        string_size = screen_height // 44
        subpixel_size = screen_height // 47

        title_font = pygame.font.Font(self._theme.get("titlefont", assets.FALLBACK_FNT), title_modded_size)

        subtitle_font = pygame.font.Font(self._theme.get("titlefont", assets.FALLBACK_FNT), subtitle_size)

        string_font = pygame.font.Font(self._theme.get("pixelfont", assets.FALLBACK_FNT), string_size)
        subpixel_font = pygame.font.Font(self._theme.get("pixelfont", assets.FALLBACK_FNT), subpixel_size)


        TITLE = title if alttitle is None else alttitle
        self._title = pygame.font.Font.render(
            title_font,
            TITLE,
            True,
            title_color)

        self._subtitle = pygame.font.Font.render(
            subtitle_font,
            sub1,
            True,
            SUBTITLE1_COLOR,
        )

        self._subtitle_en = pygame.font.Font.render(
            subpixel_font,
            sub2,
            True,
            SUBTITLE2_COLOR,
        )

        self._press_any_key = pygame.font.Font.render(
            string_font, pak, True, PAK_COLOR
        )

        _, height = screen.get_size()
        img_size = height // 8

        img = pygame.image.load(self._theme.get("title_icon", assets.FALLBACK_IMG)).convert_alpha()

        self._title_img = pygame.transform.scale(img, (img_size, img_size))

    def draw(self):
        """Draw the scene."""
        super().draw()

        s_w, s_h = self._screen.get_size()

        b_x, b_y = self._title_img.get_size()

        self._screen.blit(
            self._title_img, ((s_w // 2) - (b_x // 2), (s_h // 2) + (b_y // 2))
        )

        t_x, t_y = self._title.get_size()

        self._screen.blit(
            self._title,
            ((s_w // 2) - t_x // 2,
             (s_h // 2) - t_y // 2))

        sjp_x, sjp_y = self._subtitle.get_size()
        sen_x, sen_y = self._subtitle_en.get_size()

        jp_offset = t_y + b_y + (t_y // 2)
        en_offset = jp_offset + sen_y + (sjp_y // 2)

        self._screen.blit(
            self._subtitle,
            ((s_w // 2) - (sjp_x // 2), (s_h // 2) - (sjp_y // 2) + jp_offset),
        )

        self._screen.blit(
            self._subtitle_en,
            ((s_w // 2) - (sen_x // 2), (s_h // 2) - (sen_y // 2) + en_offset),
        )

        p_x = self._press_any_key.get_width()

        self._screen.blit(
            self._press_any_key,
            ((s_w // 2) - p_x // 2, s_h - 50))


class LeaderboardScene(PressAnyKeyToExitScene):
    """a leaderboard"""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        screen,
        score,
        lives,
        oneups = None,
        background_color=rgbcolors.black,
        soundtrack=None,
        skin="default",
        victorytext = "VICTORY!",
        continuetext = "Continue (Y/N)?"
    ):
        """initialize a leaderboard"""
        super().__init__(screen, background_color, soundtrack,skin=skin)

        screen_height = screen.get_height()

        title_font_size = screen_height // 11
        lb_font_size = confirm_font_size = screen_height // 57

        string_font = pygame.font.Font(self._theme.get("pixelfont", assets.FALLBACK_FNT), title_font_size)
        self._score = score
        self._lives = lives
        self._y = False
        self._oneups = [] if oneups is None else oneups

        self._you_win = pygame.font.Font.render(
            string_font, victorytext, True, rgbcolors.ghostwhite
        )

        # pylint: disable=redefined-outer-name
        leaderboard = [f"{count + 1}. {word[0]} - {word[1]}"
                       for count, word in enumerate(self._leaderboard.scores)]

        lb_font = pygame.font.Font(self._theme.get("pixelfont", assets.FALLBACK_FNT), lb_font_size)

        self._lb_font = [pygame.font.Font.render(
            lb_font,
            phrase,
            True,
            rgbcolors.ghostwhite
            ) for phrase in leaderboard]

        confirm_font = pygame.font.Font(self._theme.get("pixelfont", assets.FALLBACK_FNT), confirm_font_size)

        self._confirm_screen = pygame.font.Font.render(
            confirm_font, continuetext, True, rgbcolors.ghostwhite
        )

    def process_event(self, event):
        """Process game events."""

        if time.time() >= self._timestart + 3:
            if (
                event.type == pygame.KEYDOWN and event.key == pygame.K_y
                or
                event.type == pygame.JOYBUTTONDOWN and event.button == 0):
                self._y = True

            super().process_event(event)

    def set_score(self, value):
        """set the score"""

        self._score = value

    def draw(self):
        """Draw the scene."""
        super().draw()

        s_w, s_h = self._screen.get_size()

        t_x, t_y = self._you_win.get_size()

        self._screen.blit(self._you_win, ((s_w // 2) - t_x // 2, 50))

        if self._lb_font:
            l_x, _ = min(
                self._lb_font,
                key=lambda e: e.get_width()).get_size()

            posx = (s_w // 2) - l_x // 2
            posy = 50 + t_y + (t_y // 4)
            position = (posx, posy)
            for num, line in enumerate(self._lb_font):
                self._screen.blit(
                    line,
                    (position[0],
                     position[1] + (num * 14) + (num * 4)))

        if time.time() >= self._timestart + 3:
            p_x = self._confirm_screen.get_width()
            p_y = self._confirm_screen.get_height()

            self._screen.blit(
                self._confirm_screen,
                ((s_w // 2) - p_x // 2, s_h - (50 + p_y)))

    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

        lblen = len(self._leaderboard.scores)
        if lblen < 10 or self._score > self._leaderboard.lowest[0]:
            self._leaderboard.add_score((self._score, datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")))
            self._leaderboard.save(save_path)

        yes = self._y
        self._y = False

        if self._quit:
            return ["q"]
        if yes:
            return ["ly", [self._score, self._lives, self._oneups]]

        return ["gn"]


class GameOverScene(PressAnyKeyToExitScene):
    """a game over scene"""

    def __init__(
        self,
        screen,
        score,
        background_color=rgbcolors.black,
        soundtrack=None,
        skin="default",
        gameovertext = "GAME OVER!",
        continuetext = "Continue (Y/N)?"
    ):
        """initialize a game over scene"""

        super().__init__(screen, background_color, soundtrack, skin=skin)

        screen_height = screen.get_height()
        title_font_size = screen_height // 11
        confirm_font_size = screen_height // 57

        string_font = pygame.font.Font(self._theme.get("pixelfont", assets.FALLBACK_FNT), title_font_size)

        self._y = False

        self._score = score

        height = screen.get_height() // 8

        self._game_over = pygame.font.Font.render(
            string_font, gameovertext, True, rgbcolors.ghostwhite
        )

        confirm_font = pygame.font.Font(self._theme.get("pixelfont", assets.FALLBACK_FNT), confirm_font_size)

        self._confirm_screen = pygame.font.Font.render(
            confirm_font, continuetext, True, rgbcolors.ghostwhite
        )

        grammar = "points" if score != 1 else "point"

        self._score_message = pygame.font.Font.render(
            confirm_font,
            f"You scored {score} {grammar}.",
            True,
            rgbcolors.ghostwhite
        )

        img = pygame.image.load(self._theme.get("gameover_icon", assets.FALLBACK_IMG)).convert_alpha()

        self._title_img = pygame.transform.scale(img, (height, height))

    def process_event(self, event):
        """Process game events."""

        if time.time() >= self._timestart + 3:
            if (
                event.type == pygame.KEYDOWN and event.key == pygame.K_y
                or
                event.type == pygame.JOYBUTTONDOWN and event.button == 0):
                self._y = True

            super().process_event(event)

    def set_score(self, val):
        """set the score"""

        self._score = val

    def draw(self):
        """Draw the scene."""
        super().draw()

        s_w, s_h = self._screen.get_size()

        b_x, b_y = self._title_img.get_size()

        self._screen.blit(
            self._title_img, ((s_w // 2) - (b_x // 2), (s_h // 2) + (b_y // 2))
        )

        t_x, t_y = self._game_over.get_size()

        self._screen.blit(
            self._game_over, ((s_w // 2) - t_x // 2, (s_h // 2) - t_y // 2)
        )

        if time.time() >= self._timestart + 3:
            p_x = self._confirm_screen.get_width()
            p_y = self._confirm_screen.get_height()

            self._screen.blit(
                self._confirm_screen,
                ((s_w // 2) - p_x // 2, s_h - (50 + p_y)))

        s_x, s_y = self._score_message.get_size()

        self._screen.blit(
            self._score_message,
            ((s_w // 2) - s_x // 2,
             (s_h // 2) - (s_y // 2) - (50 + (t_y // 2)))
        )

    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

        yes = self._y
        self._y = False

        if self._quit:
            return ["q"]
        if yes:
            return ["gy"]

        return ["gn"]


class ViolentShooterKillerScene(Scene):
    """Scene with murder and violence"""

    def __init__(self,
                 screen,
                 soundtrack=None,
                 score=0,
                 lives=3,
                 oneups=None,
                 num_rows=9,
                 num_cols=20,
                 difficulty=1.0,
                 skin="default",
                 stars=True,
                 bg=False,
                 bg_speed=6,
                 bg_color=rgbcolors.black
                 ):
        """Initialize the carnage."""
        super().__init__(screen, bg_color, soundtrack, skin=skin)

        self._sprite_dict = {
            "hero" : pygame.transform.scale(pygame.image.load(self._theme.get("hero", assets.FALLBACK_IMG)).convert_alpha(), (screen.get_height() // _PLAYER_SIZE_MODIFIER,screen.get_height() // _PLAYER_SIZE_MODIFIER)),
            "second_hero": pygame.transform.scale(pygame.image.load(self._theme.get("second_hero", assets.FALLBACK_IMG)).convert_alpha(), (screen.get_height() // _PLAYER_SIZE_MODIFIER,screen.get_height() // _PLAYER_SIZE_MODIFIER)),
            "playerbullet": pygame.image.load(self._theme.get("playerbullet", assets.FALLBACK_IMG)).convert_alpha(),
            "enemybullet": pygame.image.load(self._theme.get("enemybullet", assets.FALLBACK_IMG)).convert_alpha(),
            }
        self._enemy_list = []
        for e in self._theme.get_enemies():
            self._enemy_list.append(
                pygame.transform.scale(pygame.image.load(e).convert_alpha(),(screen.get_height() // _ENEMY_SIZE_MODIFIER, screen.get_height() // _ENEMY_SIZE_MODIFIER))
                )

        self._obstacle_list = []
        for o in self._theme.get_obstacles():
            self._obstacle_list.append(
                pygame.image.load(o).convert_alpha()
                )

        self._width, self._height = self._screen.get_size()
        self._player = player.Player(
            pygame.math.Vector2(self._width // 2, self._height - (10 + screen.get_height() // _PLAYER_SIZE_MODIFIER)),
            self._screen,
            self._sprite_dict["hero"]
        )

        self._stars = stars
        self._bg = bg
        self._bg_img = None if not self._bg else pygame.transform.scale(pygame.image.load(self._theme.get("bg", assets.FALLBACK_IMG)).convert_alpha(), (screen.get_width(), screen.get_height()))
        self._bg_speed = bg_speed

        self._difficulty_mod = difficulty


        self._player2 = None
        self._make_player2()

        self._oneups = [] if oneups is None else oneups

        self._num_rows = num_rows
        self._num_cols = num_cols

        self._render_updates = pygame.sprite.RenderUpdates()
        Explosion.containers = self._render_updates
        self._explosion_sound = pygame.mixer.Sound(self._theme.get("explode", assets.FALLBACK_SND))
        self._exploding_kitty = pygame.mixer.Sound(self._theme.get("explode+kitty", assets.FALLBACK_SND))
        self._bullets = []
        self._powerups = []
        self._enemies = []
        self._obstacles = []
        self._speedupswitch = 4
        self._inc_pos_idx = False

        enemy_size = self._height // _ENEMY_SIZE_MODIFIER
        gutter_width = enemy_size // 8
        down = enemy_size + gutter_width

        self._horizontal_width = (enemy_size * self._num_cols) + (gutter_width * (self._num_cols)) + (gutter_width * 4)

        self._go = self._width - self._horizontal_width
        self._positions = [(0, down), (-self._go, 0),
                           (0, down), (self._go, 0)]
        self._pos_idx = 0
        self._score = score
        self._lives = lives
        #
        # ast1_x = randint(64, self._width // 2 - 64)
        # ast2_x = randint(self._width // 2, self._width - 64)
        # # ast1_y = randint(400, 550)
        # ast2_y = randint(400, 550)
        # ast1_p = pygame.math.Vector2((ast1_x, ast1_y))
        # ast2_p = pygame.math.Vector2((ast2_x, ast2_y))

        # self._asteroid1 = Asteroid(ast1_p, self._theme.get("ast1", assets.FALLBACK_IMG))
        # self._asteroid2 = Asteroid(ast2_p, self._theme.get("ast2", assets.FALLBACK_IMG))
        self._score_font = pygame.font.Font(self._theme.get("pixelfont", assets.FALLBACK_FNT), 16)
        self._score_surface = pygame.font.Font.render(
            self._score_font, f"Score: {score}", True, rgbcolors.ghostwhite
        )
        self._lives_surface = pygame.font.Font.render(
            self._score_font, f"Lives: x{lives}", True, rgbcolors.ghostwhite
        )
        self._life_picture = pygame.image.load(
            self._theme.get("hero", assets.FALLBACK_IMG)).convert_alpha()

        self._scroll_bg = 0
        if self._stars:
            self._scroll = 0

            random_coords = [
                (i, j)
                for i in range(1, self._screen.get_width())
                for j in range(1, self._screen.get_height())
                if i % 2 and randint(0, 1000) < 30 and
                j % 2 and randint(0, 1000) < 30
                ]

            star_colors = [
                rgbcolors.ghostwhite,
                rgbcolors.snow,
                rgbcolors.floralwhite,
                rgbcolors.ghostwhite,
                rgbcolors.snow,
                rgbcolors.floralwhite,
                rgbcolors.ghostwhite,
                rgbcolors.snow,
                rgbcolors.floralwhite,
                rgbcolors.lemonchiffon,
                rgbcolors.mintcream,
                rgbcolors.aliceblue,
                rgbcolors.lavenderblush,
                rgbcolors.indianred,
                rgbcolors.lightsalmon
                ]

            self._random_space = pygame.Surface((
                self._screen.get_width() - 1,
                self._screen.get_height() - 1))

            for coord in random_coords:
                self._random_space.set_at(
                    coord,
                    choice(star_colors))

        self._make_enemies()

    def _make_player2(self):
        """determine if we should make player 2, and make him"""

        if self._joysticks is not None and len(self._joysticks) > 1:
            gutter = self._player.width + (self.player.width // 2)
            player_2_x = self._player.position.x + gutter
            player_2_y = self._player.position.y
            self._player2 = player.Player(
                pygame.math.Vector2(player_2_x, player_2_y),
                self._screen,
                self._sprite_dict["second_hero"]
            )

    def update_lives(self, value):
        """update the lives of the player"""

        templives = self._lives + value
        self._lives = templives if templives >= 0 else 0

        self._lives_surface = pygame.font.Font.render(
            self._score_font,
            f"Lives: x{self._lives}",
            True,
            rgbcolors.ghostwhite
        )

        if not self._lives:
            self._is_valid = False

    def spawn_obstacle(self):
        """spawn an obstacle that descends from the top of the screen"""

        obstacle_choice = randrange(0, self._theme.num_obstacles())
        img = pygame.image.load(self._theme.get_obstacle(obstacle_choice))

        (width, height) = self._screen.get_size()

        xpos = randint(0, width - img.get_width())
        ypos = 0 - img.get_height()

        position = pygame.math.Vector2(xpos, ypos)
        obstacle_target = position - pygame.math.Vector2(0, -(height + img.get_height()))
        self._obstacles.append(
            Obstacle(
                position,
                obstacle_target,
                min(10 * self._difficulty_mod, 25),
                self._obstacle_list[obstacle_choice]
                )
            )

    def spawn_powerup(self):
        """spawn a powerup with the specified max time"""

        powerups = [
            (powerup.BurstShotPowerup, 15, "burst")
            ]

        powup_choice = choice(powerups)

        (width, height) = self._screen.get_size()

        xpos = randint(32, width - 48)
        ypos = 0

        newpos = pygame.math.Vector2(xpos, ypos)
        bullet_target = newpos - pygame.math.Vector2(0, -height - 16)

        self._powerups.append(
            powup_choice[0](newpos, bullet_target, 2, self._theme.get(powup_choice[2], assets.FALLBACK_IMG), powup_choice[1])
            )

    def update_score(self, value):
        """update the player score"""
        lock = threading.Lock()
        lock.acquire()

        oldscore = self._score
        tempscore = self._score + value
        self._score = tempscore if tempscore >= 0 else 0

        life_oldscore = oldscore % 20000
        life_newscore = tempscore % 20000

        nearest_multiple = 20000 * round(tempscore / 20000)

        if (value > 0
        and self._score > 0
        and life_newscore < life_oldscore
        and nearest_multiple not in self._oneups):
            self.update_lives(1)
            self._oneups.append(nearest_multiple)

        powup_oldscore = oldscore % 2000
        powup_newscore = tempscore % 2000
        if (
            value > 0
            and self._score > 0
            and powup_newscore < powup_oldscore
            and randint(1, 101) < 13
            ):
            self.spawn_powerup()


        self._score_surface = pygame.font.Font.render(
            self._score_font,
            f"Score: {self._score}",
            True,
            rgbcolors.ghostwhite
        )

    def _make_enemies(self):
        numem = self._theme.num_enemies()

        enemy_size = self._screen.get_height() // _ENEMY_SIZE_MODIFIER

        gutter_width = enemy_size // 8
        width, _ = self._screen.get_size()
        x_step = gutter_width + enemy_size
        y_step = gutter_width + enemy_size
        enemies_per_row = self._num_cols + int(self._difficulty_mod) - 1
        num_rows = self._num_rows + int(self._difficulty_mod) - 1
        print(f"There will be {num_rows} rows and {enemies_per_row} columns")

        enemy_kind = 0

        for i in range(num_rows):
            for j in range(enemies_per_row):
               self._enemies.append(EnemyShip(
                    pygame.math.Vector2(
                        x_step - enemy_size + (j * x_step), y_step + enemy_size + (i * y_step)
                    ),
                    self._screen,
                    self._enemy_list[enemy_kind],
                    5 * self._difficulty_mod
                ))
            if (enemy_kind + 1) < numem:
                enemy_kind += 1


        for enemy in self._enemies:
            target_x = enemy.position.x + self._go
            target_y = enemy.position.y
            enemy.target = pygame.math.Vector2(target_x, target_y)

    def kill_player1(self):
        Explosion(self._player, self._theme.get("explosion", assets.FALLBACK_IMG), self._player.width)
        self._explosion_sound.play()
        self._player.position = pygame.math.Vector2(self._width // 2, self._height - (10 + self._screen.get_height() // _PLAYER_SIZE_MODIFIER))
        self._player.invincible_clock()
        self.update_score(int(-100 * self._difficulty_mod))
        self.update_lives(-1)

    def kill_player2(self):
        Explosion(self._player, self._theme.get("explosion", assets.FALLBACK_IMG), self._player.width)
        self._explosion_sound.play()
        self._player2.position = pygame.math.Vector2(self._width // 2, self._height - (10 + self._screen.get_height() // _PLAYER_SIZE_MODIFIER))
        self._player2.invincible_clock()
        # self.update_score(int(-100 * self._difficulty_mod))
        # self.update_lives(-1)


    # pylint: disable=too-many-statements too-many-branches
    def update_scene(self):
        if not self._lives:
            return
        if not self._enemies:
            self._is_valid = False
            return

        self._inc_pos_idx = False

        super().update_scene()

        if randint(0, 10001) < min(40 * self._difficulty_mod, 6667):
            print("spawning")
            self.spawn_obstacle()

        self._player.update()
        if self._player2:
            self._player2.update()

        for obstacle in self._obstacles:
            obstacle.update()
            if obstacle.should_die() and obstacle in self._powerups:
                self.obstacles.remove(obstacle)
            if (
                obstacle.rect.colliderect(self._player.rect)
                and not self._player.invincible
                ):
                self.kill_player1()
            if self._player2 and obstacle.rect.colliderect(self._player2.rect):
                self.kill_player2()

        for bullet in self._bullets:
            bullet.update()
            if bullet in self._bullets:
                if (
                    bullet.rect.colliderect(self._player.rect)
                    and not self._player.invincible
                    and isinstance(bullet, bullets.EnemyBullet)
                ):
                    self.kill_player1()
                if (
                    self._player2
                    and bullet.rect.colliderect(self._player2.rect)
                    and not self._player2.invincible
                    and isinstance(bullet, bullets.EnemyBullet)
                ):
                   self.kill_player2()
                if bullet.rect.collideobjects([obstacle for obstacle in self._obstacles]):
                    if bullet in self._bullets:
                        self._bullets.remove(bullet)
                    if isinstance(bullet, bullets.PlayerBullet):
                        self.update_score(int(-25 * self._difficulty_mod))
                    if isinstance(bullet, bullets.PlayerBulletOneThird):
                        self.update_score(int(-5 * self._difficulty_mod))
                if bullet.should_die():
                    if bullet in self._bullets:
                        self._bullets.remove(bullet)
                    if isinstance(bullet, bullets.PlayerBullet):
                        self.update_score(int(-50 * self._difficulty_mod))
                    if isinstance(bullet, bullets.PlayerBulletOneThird):
                        self.update_score(int(-15 * self._difficulty_mod))
                else:
                    index = bullet.rect.collidelist(
                        [c.rect for c in self._enemies])
                    if index > -1 and not isinstance(bullet, bullets.EnemyBullet):
                        Explosion(self._enemies[index], self._theme.get("explosion", assets.FALLBACK_IMG), self._enemies[index].width)
                        self._enemies[index].is_exploding = True
                        self._enemies.remove(self._enemies[index])

                        if randint(0, 100) >= 8:
                            self._explosion_sound.play()
                        else:
                            self._exploding_kitty.play()

                        if bullet in self._bullets:
                            self._bullets.remove(bullet)
                        self.update_score(int(200 * self._difficulty_mod))
                        if not self._enemies:
                            self._is_valid = False
                            return

        for enemy in self._enemies:
            if enemy in self._enemies:
                enemy.update()
                if enemy.at_pos:
                    t_x = enemy.position.x + self._positions[self._pos_idx][0]
                    t_y = enemy.position.y + self._positions[self._pos_idx][1]
                    enemy.original_position = enemy.target
                    enemy.target = pygame.math.Vector2(t_x, t_y)
                    if not self._inc_pos_idx:
                        self._inc_pos_idx = True
                if enemy.rect.colliderect(self._player.rect):
                    if not self._player.is_dead:
                        self._player.is_dead = True
                        self.update_lives(-999)
                        Explosion(self._player, self._theme.get("explosion", assets.FALLBACK_IMG), enemy.width)
                        self._explosion_sound.play()
                        for enemy in self._enemies:
                            enemy.stop()

                enmy = self._enemies
                if enemy.below_rect.collidelist([c.rect for c in enmy]) < 0:
                    collidelist = [self._player.rect] if self._player2 is None else [self._player.rect, self._player2.rect]
                    fire_at_player = (1) if enemy.below_rect.collidelist(collidelist) < 0 else (10 * self._difficulty_mod)

                    if randint(0, 10001) < min(20 * self._difficulty_mod + fire_at_player, 6667):
                        (_, height) = self._screen.get_size()

                        newpos = pygame.math.Vector2(
                            enemy.position.x + (enemy.width // 2), enemy.position.y
                        )
                        bullet_target = newpos - pygame.math.Vector2(0, -height)
                        velocity = 15
                        self._bullets.append(
                            bullets.EnemyBullet(newpos, bullet_target, velocity, self._sprite_dict["enemybullet"])
                        )
        if self._inc_pos_idx:
            if not self._speedupswitch:
                for enemy in self._enemies:
                    enemy.inc_speed(0.5 * self._difficulty_mod)

            self._speedupswitch = (self._speedupswitch + 1) % 8
            self._pos_idx = (self._pos_idx + 1) % 4

        for powup in self._powerups:
            powup.update()
            if powup.should_die() and powup in self._powerups:
                self._powerups.remove(powup)
            if powup.rect.colliderect(self._player.rect):
                match (type(powup)):
                    case powerup.BurstShotPowerup:
                        self._player.set_powerup("burst", powup.maxtime)

                if powup in self._powerups:
                    self._powerups.remove(powup)
            if self._player2 and powup.rect.colliderect(self._player2.rect):
                match (type(powup)):
                    case powerup.BurstShotPowerup:
                        self._player2.set_powerup("burst", powup.maxtime)

                if powup in self._powerups:
                    self._powerups.remove(powup)

    def player_move(self, player, joystick, event):
        if player is not None and not player.is_dead:
            if (
                (event.type == pygame.KEYDOWN
                 and event.key == pygame.K_SPACE)
                or
                (event.type == pygame.JOYBUTTONDOWN
                 and (event.button == 0
                 or event.button == 7
                 or event.button == 6)
                 and event.instance_id == joystick
                 )

            ):

                match (player.powerup):
                    case "burst":
                        (_, height) = self._screen.get_size()

                        bullet_asset = self._sprite_dict["playerbullet"]

                        newpos = pygame.math.Vector2(
                            player.position.x + (player.width // 2) - (bullet_asset.get_width() // 2), player.position.y
                        )
                        bullet_target = newpos - pygame.math.Vector2(0, height)
                        self._bullets.append(
                            bullets.PlayerBulletOneThird(newpos, bullet_target, 20, bullet_asset)
                        )
                        self._bullets.append(
                            bullets.PlayerBulletOneThird(newpos, bullet_target, 18, bullet_asset)
                        )
                        self._bullets.append(
                            bullets.PlayerBulletOneThird(newpos, bullet_target, 16, bullet_asset)
                        )

                    case _:
                        (_, height) = self._screen.get_size()

                        bullet_asset = self._sprite_dict["playerbullet"]

                        newpos = pygame.math.Vector2(
                            player.position.x + + (player.width // 2) - (bullet_asset.get_width() // 2), player.position.y
                        )
                        bullet_target = newpos - pygame.math.Vector2(0, height)
                        velocity = 20
                        self._bullets.append(
                            bullets.PlayerBullet(newpos, bullet_target, velocity, bullet_asset)
                        )

            if self._joysticks:
                axis = self._joysticks[joystick].get_axis(0)

                if -0.1 < axis < 0.1:
                    axis = 0


                if axis > 0.1:
                    player.move_right(axis)
                if axis < -0.1:
                    player.move_left(axis)
                if axis == 0:
                    player.stop()

    def process_event(self, event):
        super().process_event(event)

        if not self._player.is_dead:

            if (
                event.type == pygame.JOYDEVICEADDED
                or
                event.type == pygame.JOYDEVICEREMOVED):
                self._make_player2()

            t1 = threading.Thread(target=self.player_move, args=(self._player, 0, event))
            t2 = threading.Thread(target=self.player_move, args=(self._player2, 1, event))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self._player.move_left()
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self._player.stop()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self._player.move_right()
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self._player.stop()

            t1.start()
            t2.start()
            t1.join()
            t2.join()

    def render_updates(self):
        super().render_updates()
        self._render_updates.clear(self._screen, self._background)
        self._render_updates.update()
        _ = self._render_updates.draw(self._screen)

    # pylint: disable=inconsistent-return-statements
    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

        if self._quit:
            return ["q"]
        if not self._lives:
            return ["l", self._score]
        if not self._enemies:
            return ["w", [self._score, self._lives, self._oneups]]

    def draw(self):
        super().draw()

        if self._bg:
            bg_height = self._bg_img.get_height()
            screen_height = self._screen.get_height()
            if self._scroll_bg >= screen_height:
                self._scroll_bg = 0

            frame1_y = self._scroll_bg
            frame2_y = self._scroll_bg - bg_height
            self._screen.blit(self._bg_img, (0, frame1_y))
            self._screen.blit(self._bg_img, (0, frame2_y))

            self._scroll_bg += self._bg_speed


        if self._stars and not self._bg:
            space_height = self._random_space.get_height()
            screen_height = self._screen.get_height()
            if self._scroll >= screen_height:
                self._scroll = 0

            frame1_y = self._scroll
            frame2_y = self._scroll - space_height
            self._screen.blit(self._random_space, (1, frame1_y))
            self._screen.blit(self._random_space, (1, frame2_y))

            self._scroll = self._scroll + self._bg_speed

        for enemy in self._enemies:
            if not enemy.is_exploding:
                enemy.draw(self._screen)
        for bullet in self._bullets:
            bullet.draw(self._screen)
        for powup in self._powerups:
            powup.draw(self._screen)
        for obstacle in self._obstacles:
            obstacle.draw(self._screen)

        self._player.draw(self._screen)
        if self._player2:
            self._player2.draw(self._screen)
        # self._asteroid1.draw(self._screen)
        # self._asteroid2.draw(self._screen)

        lives_y = self._score_surface.get_height() + 8
        lives_x = 4
        lives_x2 = self._life_picture.get_width() + 8
        lives_y2 = (self._lives_surface.get_height() // 2) + lives_y

        self._screen.blit(self._life_picture, (lives_x, lives_y))
        self._screen.blit(self._lives_surface, (lives_x2, lives_y2))

        self._screen.blit(self._score_surface, (4, 4))
