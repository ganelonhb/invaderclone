"""implements the first level in the game"""

import pygame

import threading

from random import randint, choice, randrange, uniform

from .scene import Scene
from . import rgbcolors
from . import theme
from . import player
from .explosion import Explosion
from .enemy import EnemyShip
from . import bullets
from . import burst_shot_powerup
from .obstacle import Obstacle
from .constants import PLAYER_SIZE_MODIFIER, ENEMY_SIZE_MODIFIER


class Level0(Scene):
    """Scene which implements a level in the game"""

    def __init__(self,
                screen,
                game_settings,
                soundtrack=None,
                ):
        """Initialize the carnage."""
        super().__init__(screen, game_settings, game_settings['game_music'])

        self._sprite_dict = None
        self._enemy_list = None
        self._obstacle_list = None
        self._player_speed = None
        self._player_bullet_speed = None
        self._enemy_speed = None
        self._obstacle_speed = None
        self._powerup_speed = None
        self._powup_chance = None
        self._obstacle_chance = None
        self._oneup_score = None
        self._powerup_score = None
        self._stars = None
        self._difficulty_mod = None
        self._score = None
        self._lives = None
        self._score_p2 = None
        self._lives_p2 = None
        self._num_rows = None
        self._num_cols = None
        self._score_font = None
        self._score_surface = None
        self._lives_surface = None
        self._lives_surface_p2 = None
        self._life_picture = None
        self._life_picture_p2 = None

        self.update_settings()

        self._width, self._height = self._screen.get_size()

        self._player = player.Player(
            pygame.math.Vector2(self._width // 2, self._height - (10 + screen.get_height() // PLAYER_SIZE_MODIFIER)),
            self._screen,
            self._sprite_dict["hero"],
            self._player_speed
        )

        self._player2 = None
        self._make_player2()

        self._explosion_sound = pygame.mixer.Sound(self._theme.get("explode", theme.FALLBACK_SND))
        self._exploding_kitty = pygame.mixer.Sound(self._theme.get("explode+kitty", theme.FALLBACK_SND))
        self._bullets = []
        self._powerups = []
        self._enemies = []
        self._explosions = []
        self._obstacles = []
        self._speedupswitch = 4
        self._inc_pos_idx = False

        enemy_size = self._height // ENEMY_SIZE_MODIFIER
        gutter_width = enemy_size // 8
        down = enemy_size + gutter_width

        self._horizontal_width = (enemy_size * self._num_cols) + (gutter_width * (self._num_cols)) + (gutter_width * 4)

        self._go = self._width - self._horizontal_width
        self._positions = [(0, down), (-self._go, 0),
                           (0, down), (self._go, 0)]
        self._pos_idx = 0

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

    def reset_scene(self):
        super().reset_scene()

        self.__init__(self._screen, self._game_settings)

    def update_settings(self, new_settings = None):
        super().update_settings()

        gs = self._game_settings if new_settings is None else new_settings
        cd = rgbcolors.color_dictionary
        # Assets
        self._sprite_dict = {
            "hero" : pygame.transform.scale(pygame.image.load(self._theme.get("hero", theme.FALLBACK_IMG)).convert_alpha(), (self._screen.get_height() // PLAYER_SIZE_MODIFIER,self._screen.get_height() // PLAYER_SIZE_MODIFIER)),
            "second_hero": pygame.transform.scale(pygame.image.load(self._theme.get("second_hero", theme.FALLBACK_IMG)).convert_alpha(), (self._screen.get_height() // PLAYER_SIZE_MODIFIER,self._screen.get_height() // PLAYER_SIZE_MODIFIER)),
            "playerbullet": pygame.image.load(self._theme.get("playerbullet", theme.FALLBACK_IMG)).convert_alpha(),
            "enemybullet": pygame.image.load(self._theme.get("enemybullet", theme.FALLBACK_IMG)).convert_alpha(),
            "explosion" : pygame.image.load(self._theme.get("explosion", theme.FALLBACK_IMG)).convert_alpha(),
            "burst" : pygame.image.load(self._theme.get("burst", theme.FALLBACK_IMG)).convert_alpha(),
            "bg" : pygame.transform.scale(pygame.image.load(self._theme.get("bg", theme.FALLBACK_IMG)).convert_alpha(), (self._screen.get_width(), self._screen.get_height())),
            }

        self._enemy_list = []
        for e in self._theme.get_enemies():
            self._enemy_list.append(
                pygame.transform.scale(pygame.image.load(e).convert_alpha(),(self._screen.get_height() // ENEMY_SIZE_MODIFIER, self._screen.get_height() // ENEMY_SIZE_MODIFIER))
                )

        self._obstacle_list = []
        for o in self._theme.get_obstacles():
            self._obstacle_list.append(
                pygame.image.load(o).convert_alpha()
                )

        # Speeds
        self._player_speed = gs["player_speed"]
        self._player_bullet_speed = gs["player_bullet_speed"]
        self._enemy_speed = gs["enemy_speed"]
        self._obstacle_speed = gs["obstacle_speed"]
        self._powerup_speed = gs["powerup_speed"]

        # Chances
        self._powup_chance = gs["powerup_chance"]
        self._obstacle_chance = gs["obstacle_chance"]

        # BG Options
        self._stars = not gs["disable_stars"]
        self._bg = gs["enable_background"]
        self._bg_img = None if not self._bg else self._sprite_dict["bg"]
        self._bg_speed = gs["bg_speed"]

        # Difficulty
        self._difficulty_mod = gs["current_difficulty_modifier"]
        self._num_rows = gs["rows"]
        self._num_cols = gs["columns"]

        # Scores
        self._oneup_score = gs["oneup_score"]
        self._powerup_score = gs["powerup_score"]
        self._death_penalty = -gs["death_penalty"]

        # Scores/Lives
        self._score = gs["current_score_p1"]
        self._lives = gs["current_lives_p1"]
        self._score_p2 = gs["current_score_p2"]
        self._lives_p2 = gs["current_lives_p2"]

        # Fonts
        self._score_font = pygame.font.Font(self._theme.get("pixelfont", theme.FALLBACK_FNT), 16)
        self._score_surface = pygame.font.Font.render(
            self._score_font, f"Score: {self._score}", True, cd[gs["ingame_font_color"]]
        )
        self._lives_surface = pygame.font.Font.render(
            self._score_font, f"Lives: x{self._lives}", True, cd[gs["ingame_font_color"]]
        )
        self._lives_surface_p2 = pygame.font.Font.render(
            self._score_font, f"Lives: x{self._lives_p2}", True, cd[gs["ingame_font_color"]]
        )
        self._life_picture = pygame.image.load(
            self._theme.get("hero", theme.FALLBACK_IMG)).convert_alpha()
        self._life_picture_p2 = pygame.image.load(
            self._theme.get("second_hero", theme.FALLBACK_IMG)).convert_alpha()


    def _make_player2(self):
        """determine if we should make player 2, and make him"""

        if not self._game_settings["disable_multiplayer"] and self._joysticks is not None and len(self._joysticks) > 1:
            gutter = self._player.width + (self._player.width // 2)
            player_2_x = self._player.position.x + gutter
            player_2_y = self._player.position.y
            self._player2 = player.Player(
                pygame.math.Vector2(player_2_x, player_2_y),
                self._screen,
                self._sprite_dict["second_hero"],
                player_speed = self._player_speed
            )
        else:
            self._player2 = None

    def update_lives(self, value):
        """update the lives of the player"""
        gs = self._game_settings
        cd = rgbcolors.color_dictionary

        templives = self._lives + value
        self._lives = templives if templives >= 0 else 0
        gs["current_lives_p1"] = self._lives

        self._lives_surface = pygame.font.Font.render(
            self._score_font,
            f"Lives: x{self._lives}",
            True,
            cd[gs["ingame_font_color"]]
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
                min(self._obstacle_speed * self._difficulty_mod, 35),
                self._obstacle_list[obstacle_choice]
                )
            )

    def spawn_powerup(self):
        """spawn a powerup with the specified max time"""

        powerups = [
            (burst_shot_powerup.BurstShotPowerup, 3, "burst")
            ]

        powup_choice = choice(powerups)

        (width, height) = self._screen.get_size()

        xpos = randint(32, width - 48)
        ypos = 0

        newpos = pygame.math.Vector2(xpos, ypos)
        bullet_target = newpos - pygame.math.Vector2(0, -height - 16)

        self._powerups.append(
            powup_choice[0](newpos, bullet_target, self._powerup_speed, self._sprite_dict[powup_choice[2]], powup_choice[1])
            )

    def update_score(self, value):
        """update the player score"""

        gs = self._game_settings
        cd = rgbcolors.color_dictionary

        oldscore = self._score
        tempscore = self._score + value
        self._score = tempscore if tempscore >= 0 else 0
        gs["current_score_p1"] = self._score

        life_oldscore = oldscore % self._oneup_score
        life_newscore = tempscore % self._oneup_score

        nearest_multiple = self._oneup_score * round(tempscore / self._oneup_score)

        if (value > 0
        and self._score > 0
        and life_newscore < life_oldscore
        and nearest_multiple not in gs["oneups"]):
            self.update_lives(1)
            gs["oneups"].append(nearest_multiple)

        powup_oldscore = oldscore % self._powerup_score
        powup_newscore = tempscore % self._powerup_score

        if (
            value > 0
            and self._score > 0
            and powup_newscore < powup_oldscore
            and randint(1, 101) < self._powup_chance
            ):
            self.spawn_powerup()


        self._score_surface = pygame.font.Font.render(
            self._score_font,
            f"Score: {self._score}",
            True,
            cd[gs["ingame_font_color"]]
        )

    def _make_enemies(self):
        numem = self._theme.num_enemies()

        enemy_size = self._screen.get_height() // ENEMY_SIZE_MODIFIER

        gutter_width = enemy_size // 8
        width, _ = self._screen.get_size()
        x_step = gutter_width + enemy_size
        y_step = gutter_width + enemy_size
        enemies_per_row = self._num_cols + int(self._difficulty_mod) - 1
        num_rows = self._num_rows + int(self._difficulty_mod) - 1
        #print(f"There will be {num_rows} rows and {enemies_per_row} columns")

        enemy_kind = 0

        for i in range(num_rows):
            for j in range(enemies_per_row):
               self._enemies.append(EnemyShip(
                    pygame.math.Vector2(
                        x_step - enemy_size + (j * x_step), y_step + enemy_size + (i * y_step)
                    ),
                    self._screen,
                    self._enemy_list[enemy_kind],
                    self._enemy_speed * self._difficulty_mod
                ))
            if (enemy_kind + 1) < numem:
                enemy_kind += 1


        for enemy in self._enemies:
            target_x = enemy.position.x + self._go
            target_y = enemy.position.y
            enemy.target = pygame.math.Vector2(target_x, target_y)

    def kill_player1(self):
        self._explosions.append(Explosion(self._player, self._sprite_dict["explosion"], self._player.width))
        self._explosion_sound.play()
        self._player.position = pygame.math.Vector2(self._width // 2, self._height - (10 + self._screen.get_height() // PLAYER_SIZE_MODIFIER))
        self._player.invincible_clock()
        self.update_score(int(self._death_penalty * self._difficulty_mod))
        self.update_lives(-1)

    def kill_player2(self):
        if self._player2 is not None:
            gutter = self._player.width + (self._player.width // 2)
            player_2_x = self._player.position.x + gutter
            player_2_y = self._player.position.y
            self._explosions.append(Explosion(self._player2, self._sprite_dict["explosion"], self._player2.width))
            self._explosion_sound.play()
            self._player2.position = pygame.math.Vector2(player_2_x, player_2_y)
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

        spawn_obstacle_uniform = uniform(0, 101)
        if spawn_obstacle_uniform < min(13.33, self._obstacle_chance + (self._difficulty_mod - 1.)):
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

        for explosion in self._explosions:
            explosion.update()
            if explosion.should_die:
                if explosion in self._explosions:
                    self._explosions.remove(explosion)


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
                        self._explosions.append(Explosion(self._enemies[index], self._sprite_dict["explosion"], self._enemies[index].width))
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
                        self._explosions.append(Explosion(self._player, self._sprite_dict["explosion"], self._player.width))
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
                    case burst_shot_powerup.BurstShotPowerup:
                        self._player.set_powerup("burst", powup.maxtime)

                if powup in self._powerups:
                    self._powerups.remove(powup)
            if self._player2 and powup.rect.colliderect(self._player2.rect):
                match (type(powup)):
                    case burst_shot_powerup.BurstShotPowerup:
                        self._player2.set_powerup("burst", powup.maxtime)

                if powup in self._powerups:
                    self._powerups.remove(powup)

    def player_move(self, player, joystick, event):
        try:
            if player is not None and not player.is_dead:
                if (
                    (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE)
                    or
                    (event.type == pygame.JOYBUTTONDOWN
                    and (event.button == 0
                    or event.button == 7
                    or event.button == 6)
                    and event.instance_id == self._joysticks[joystick].get_instance_id()
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
                                bullets.PlayerBulletOneThird(newpos, bullet_target, self._player_bullet_speed - 0, bullet_asset)
                            )
                            self._bullets.append(
                                bullets.PlayerBulletOneThird(newpos, bullet_target, self._player_bullet_speed - 2, bullet_asset)
                            )
                            self._bullets.append(
                                bullets.PlayerBulletOneThird(newpos, bullet_target, self._player_bullet_speed - 4, bullet_asset)
                            )

                        case _:
                            (_, height) = self._screen.get_size()

                            bullet_asset = self._sprite_dict["playerbullet"]

                            newpos = pygame.math.Vector2(
                                player.position.x + + (player.width // 2) - (bullet_asset.get_width() // 2), player.position.y
                            )
                            bullet_target = newpos - pygame.math.Vector2(0, height)
                            velocity = self._player_bullet_speed
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
        except IndexError as e:
            print("Exception encountered. Trying not to crash the thread.")

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

    # pylint: disable=inconsistent-return-statements
    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

        if self._quit:
            return ["QUIT_GAME"]
        if not self._lives:
            return ["CHANGE_SCENE", "GameOverScene"]
        if not self._enemies:
            return ["CHANGE_SCENE", "LeaderboardScene"]

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

        self._player.draw(self._screen)
        if self._player2:
            self._player2.draw(self._screen)
        for explosion in self._explosions:
            if not explosion.should_die:
                explosion.draw(self._screen)
        for enemy in self._enemies:
            if not enemy.is_exploding:
                enemy.draw(self._screen)
        for bullet in self._bullets:
            bullet.draw(self._screen)
        for powup in self._powerups:
            powup.draw(self._screen)
        for obstacle in self._obstacles:
            obstacle.draw(self._screen)

        lives_y = self._score_surface.get_height() + 8
        lives_x = 4
        lives_x2 = self._life_picture.get_width() + 8
        lives_y2 = (self._lives_surface.get_height() // 2) + lives_y

        self._screen.blit(self._life_picture, (lives_x, lives_y))
        self._screen.blit(self._lives_surface, (lives_x2, lives_y2))

        self._screen.blit(self._score_surface, (4, 4))
