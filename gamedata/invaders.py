#!/usr/bin/env python3

"""Play the game"""

import sys
import os
import argparse

from copy import deepcopy
# pylint: disable=import-error
from invaderclone.game import InvaderClone
from invaderclone.rgbcolors import color_dictionary as cd
from invaderclone.theme import Theme, get_theme_dir


def main():
    raw_args = deepcopy(sys.argv)

    colors = [key for key in cd.keys() if key is not None]

    parser = argparse.ArgumentParser(
        prog="Invader Clone",
        description="A configurable clone of Space Invaders "
                    "written as part of a school project in Pygame.",
        epilog="For comments, questions, concerns, inquiries, or any other "
               "synonyms of those words, contact me at worcesterz@outlook.com."
        )

    parser.add_argument("-l", "--list_colors", action='store_true', help='show a the list of colors that arguments accepting COLOR NAME will take and exit')

    window_settings = parser.add_argument_group(title="window settings", description="modify window settings")
    window_settings.add_argument("--width", default=1000, type=int, help="window width (default 1000)")
    window_settings.add_argument("--height", default=800, type=int, help="window height (default 800)")
    window_settings.add_argument("-n", "--name", default="Invader Clone", help="change the name of the game")

    game_settings = parser.add_argument_group(title="game settings", description="modify core game functionality")
    game_settings.add_argument("--frame_rate", default=60, type=int, help="game frame rate")
    game_settings.add_argument("--disable_gamepads", action="store_true", help="disable the use of gamepads (if for some reason it doesn't work)")
    game_settings.add_argument("--disable_multiplayer", action="store_true", help="disable multiplayer functionality")

    sound_settings = parser.add_argument_group(title='sound settings', description='music and sound effect settings')
    sound_settings = parser.add_argument("--title_music", default="title_music", help='what asset to use for title music')
    sound_settings = parser.add_argument("--game_music", default="game_music", help="what asset to use for game music")
    sound_settings = parser.add_argument("--gameover_music", default="gameover_music", help="what asset to use for gameover music")
    sound_settings = parser.add_argument("--leaderboard_music", default="leaderboard_music", help="what asset to use for leaderboard music")

    difficulty_settings = parser.add_argument_group(title="difficulty settings", description="modify various difficulty settings")
    difficulty_settings.add_argument("-d", "--difficulty_step", default=25.0, type=float, help="increase the difficulty by this percent every round (default 25.0)")
    difficulty_settings.add_argument("-r", "--rows", default=4, type=int, help="how many rows of enemies there are (default 5)")
    difficulty_settings.add_argument("-c", "--columns", default=12, type=int, help="how many columns of enemies there are (default 9)")
    difficulty_settings.add_argument("--starting_lives", default=3, type=int, help="the number of lives to start with for each player")
    difficulty_settings.add_argument("--player_speed", type=float, default=15., help="change the speed of the player")
    difficulty_settings.add_argument("--player_bullet_speed", type=float, default=20., help="change the speed of the player's bullet")
    difficulty_settings.add_argument("--enemy_speed", type=float, default=5., help="change the base speed of enemies")
    difficulty_settings.add_argument("--obstacle_speed", type=float, default=7., help="change the base speed of obstacles")
    difficulty_settings.add_argument("--powerup_speed", type=float, default=5., help="change the speed of powerups")
    difficulty_settings.add_argument("--powerup_chance", type=int, default=13, help="percent chance a powerup spawns at the powerup score")
    difficulty_settings.add_argument("--obstacle_chance", type=float, default=0.04, help="percent chance an obstacle spawns any given frame")
    difficulty_settings.add_argument("--oneup_score", type=int, default=20000, help="every N points, the player is awarded a one up")
    difficulty_settings.add_argument("--powerup_score", type=int, default=2000, help="every N points, the player has a chance to be awarded a powerup (see --powerup_chance)")
    difficulty_settings.add_argument("--death_penalty", type=int, default=100, help="how many points are taken from the player for dying.")

    theme_settings = parser.add_argument_group(title="theme settings", description="modify generic theme settings")
    theme_settings.add_argument("-t", "--theme", default="default", help="change the theme of the game.")
    theme_settings.add_argument("-s", "--disable_stars", action='store_true', help='disable parallax stars effect')
    theme_settings.add_argument("-b", "--enable_background", action='store_true', help='enable a parallax bg effect')
    theme_settings.add_argument("--bg_speed", type=int, default=6, help='background scroll speed')
    theme_settings.add_argument("--title_bg_color", default="black", choices=colors, metavar="COLOR NAME", help="title background color"),
    theme_settings.add_argument("--game_bg_color", default="black", choices=colors, metavar="COLOR NAME", help="game background color"),
    theme_settings.add_argument("--leaderboard_bg_color", default="black", choices=colors, metavar="COLOR NAME", help="leaderboard background color")
    theme_settings.add_argument("--gameover_bg_color", default="black", choices=colors, metavar="COLOR NAME", help="gameover background color")

    global_text_settings = parser.add_argument_group(title="global text settings", description="set reoccuring global string colors")
    global_text_settings.add_argument("--press_any_key", default="Press ANY KEY!", help="press any key text")
    global_text_settings.add_argument("--press_any_key_text_color", default=None, choices=colors, metavar="COLOR NAME", help="press any key text color")
    global_text_settings.add_argument("--continueyn", default="Continue (Y/N)?", help="continue game text")
    global_text_settings.add_argument("--continueyn_text_color", default="ghostwhite", choices=colors, metavar="COLOR NAME", help="continue game text color")

    mainmenu_text_settings = parser.add_argument_group(title="main menu text settings", description="modify text and text colors of the main menu")
    mainmenu_text_settings.add_argument("--alt_title", default=None, help="give your game an alternative title on the titlescreen")
    mainmenu_text_settings.add_argument("--subtitle1", default="全部のネコ宇宙人を倒す！ 動く：'←'／'→' 撃つ：'SPACE'", help="subtitle 1 text")
    mainmenu_text_settings.add_argument("--subtitle2", default="Kill all cat aliens! Move: '←'/'→' Shoot: 'SPACE'", help="subtitle 2 text")
    mainmenu_text_settings.add_argument("--title_text_color", default="ghostwhite", choices=colors, metavar="COLOR NAME", help="title text color")
    mainmenu_text_settings.add_argument("--subtitle1_text_color", default=None, choices=colors, metavar="COLOR NAME", help="subtitle 1 text color")
    mainmenu_text_settings.add_argument("--subtitle2_text_color", default=None, choices=colors, metavar="COLOR NAME", help="subtitle 2 text color")


    ingame_text_settings = parser.add_argument_group(title="in-game text settings", description="modify in-game text and colors")
    ingame_text_settings.add_argument("--ingame_font_color", default="ghostwhite", choices=colors, metavar="COLOR NAME", help="score and lives font color")

    leaderboard_text_settings = parser.add_argument_group(title="leaderboard text settings", description="modify leaderboard text settings")
    leaderboard_text_settings.add_argument("--victory_text_color", default="ghostwhite", choices=colors, metavar="COLOR NAME", help="victory screen text color")
    leaderboard_text_settings.add_argument("--victory", default="VICTORY!", help="victory screen text")

    gameover_text_settings = parser.add_argument_group(title="gameover text settings", description="game over screen text")
    gameover_text_settings.add_argument("--game_over", default="GAME OVER!", help="game over text")
    gameover_text_settings.add_argument("--game_over_text_color", default="ghostwhite", choices=colors, metavar="COLOR NAME", help="game over text color")

    advanced_settings = parser.add_argument_group(title="advanced settings", description="add custom entries to the settings dictionary, and more")
    advanced_settings.add_argument("--set_custom_keys", nargs="+", default=[], help="add dictionary entries to the game settings entries as k:v pairs. seperate with spaces")
    advanced_settings.add_argument("--add_custom_assets", nargs="+", default=[], help="add custom assets to the game as k:v pairs. seperate with spaces")

    args = parser.parse_args()

    # check if correct sound assets are being applied to sound settings:

    temp_theme = Theme(args.theme)
    title_song = temp_theme.get(args.title_music, None)
    game_song = temp_theme.get(args.game_music, None)
    gameover_song = temp_theme.get(args.gameover_music, None)
    leaderboard_song = temp_theme.get(args.leaderboard_music, None)

    title_not_good = not (title_song is not None and title_song.endswith('.ogg'))
    game_not_good = not (game_song is not None and game_song.endswith('.ogg'))
    gameover_not_good = not (gameover_song is not None and gameover_song.endswith('.ogg'))
    leaderboard_not_good = not (leaderboard_song is not None and leaderboard_song.endswith('.ogg'))

    if (
        title_not_good
        or game_not_good
        or gameover_not_good
        or leaderboard_not_good
        ):
        print("Error: One or more of the supplied music assets cannot be used.")
        sys.exit(-1)

    # ------------------------------------------------------------------

    if args.list_colors:
        for color in colors:
            print(f'{color} : ' + ('#%02x%02x%02x' % cd[color]))
        sys.exit(0)

    _main_dir = os.path.split(os.path.abspath(__file__))[0]
    _data_dir = os.path.join(_main_dir, "invaders", "data")

    UNIX_SYSTEMS = ["aix", "darwin", "freebsd", "linux", "openbsd"]

    _docsdir = ".config" if sys.platform in UNIX_SYSTEMS else "Documents"

    _settingsdir = os.path.join(os.path.expanduser("~"), _docsdir, "invaderclone")

    if not os.path.exists(os.path.join(_settingsdir, "themes")):
        os.makedirs(os.path.join(_settingsdir, "themes"))

    theme_dir = os.path.join(
        _data_dir,
        "themes",
        args.theme
        ) if not os.path.isdir(
            os.path.join(
                _settingsdir,
                "themes",
                args.theme
                )
            ) else os.path.join(
                _settingsdir,
                "themes",
                args.theme
                )

    theme_args = os.path.join(theme_dir, "theme.args")
    default_args = os.path.join(os.getcwd(), "default.args")

    if os.path.isfile(theme_args) or (args.theme == "default" and os.path.isfile(default_args)):
        var_args = vars(args)
        var_args_keys = var_args.keys()

        args_file = theme_args if not args.theme =="default" else default_args

        with open(args_file, "r") as theme_args:
            lines = theme_args.readlines()

            for num, line in enumerate(lines):
                line_tuple = line.split('=', 1)

                if line_tuple[0].strip() in ["set_custom_keys", "add_custom_assets"]:
                    line_tuple[1] = line_tuple[1].strip().split(' ')
                    for line in line_tuple[1]:
                        line = line.strip()


                if len(line_tuple) != 2:
                    print(f"[Line {num + 1}] Error parsing theme.args. "
                          f"Invalid format: {line.rstrip()} "
                          f"(too many or too few assignment operators).")
                    sys.exit(-1)

                if line_tuple[0].strip() not in var_args_keys:
                    print(f"[Line {num + 1}] Error parsing theme.args. "
                          f"Invalid argument: {line_tuple[0].strip()}.")
                    sys.exit(-1)

                if f'--{line_tuple[0].strip()}' not in raw_args:
                    try:
                        typecast = type(var_args[line_tuple[0].strip()]) if var_args[line_tuple[0].strip()] is not None else str
                        lt_strplo = None if typecast is not bool else line_tuple[1].strip().lower()

                        skip = typecast is list

                        if (
                            typecast is bool
                            and lt_strplo in ['0', 'false', None]
                        ):
                            val = False
                        elif (
                            typecast is list
                        ):
                            for kv in line_tuple[1]:
                                k, v = kv.split(':', 1)
                                var_args[k] = v.strip()

                            val = typecast(line_tuple[1])
                        else:
                            if typecast is None:
                                val = str(line_tuple[1].strip())
                            else:
                                val = typecast(line_tuple[1].strip())

                        if not skip:
                            var_args[line_tuple[0].strip()] = val
                    except ValueError:
                        print(
                            (f"[Line {num + 1}] Error parsing theme.args."
                             f"Could not cast {line_tuple[1]} to type "
                             f"{type(var_args[line_tuple[0].strip()])}.")
                            )
                        sys.exit(-1)

    game_settings = deepcopy(dict(vars(args)))

    # Modify Game Settings
    game_settings["default_bg"] = cd["black"]
    game_settings["default_soundtrack"] = None
    game_settings["current_difficulty_modifier"] = 1.0
    game_settings["current_score_p1"] = 0
    game_settings["current_score_p2"] = 0
    game_settings["current_lives_p1"] = game_settings["starting_lives"]
    game_settings["current_lives_p2"] = game_settings["starting_lives"]
    game_settings["oneups"] = []

    for setting in args.set_custom_keys:
        if setting not in game_settings.keys():
            if ':' not in setting:
                game_settings["setting"] = None
            else:
                k, v = setting.split(':', 1)
                v = v.replace('\{theme_dir\}', get_theme_dir(args.theme))

                game_settings[k] = v
        else:
            print(f"Ignoring key with name: {setting}, already exists!")

    sys.exit(InvaderClone(game_settings).run())


if __name__ == "__main__":
    main()

