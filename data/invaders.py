#!/usr/bin/env python3

"""
Imports the the game demo and executes the main function.
"""

import sys
import os
import argparse

from copy import deepcopy
# pylint: disable=import-error
from videogame import game
from videogame.rgbcolors import color_dictionary as cd

_main_dir = os.path.split(os.path.abspath(__file__))[0]
_data_dir = os.path.join(_main_dir, "videogame", "data")

UNIX_SYSTEMS = ["aix", "darwin", "freebsd", "linux", "openbsd"]
WINDOWS_SYSTEMS = ["win32", "win64", "cygwin", "msys", "nt"]

_docsdir = ".config" if sys.platform in UNIX_SYSTEMS else "Documents"

_settingsdir = os.path.join(os.path.expanduser("~"), _docsdir, "invaderclone")

if not os.path.exists(os.path.join(_settingsdir, "themes")):
    os.makedirs(os.path.join(_settingsdir, "themes"))

def main():
    raw_args = deepcopy(sys.argv)

    colors = [key for key in cd.keys() if key is not None]

    parser = argparse.ArgumentParser(
        prog="Invader Clone",
        description="A configurable clone of Space Invaders written as part of a school project in Pygame.",
        epilog="For comments, questions, concerns, inquiries, or any other synonyms of those words, contact me at worcesterz@outlook.com."
        )

    parser.add_argument("-l", "--list_colors", action='store_true', help='show a the list of colors that arguments accepting COLOR NAME will take and exit')

    game_settings = parser.add_argument_group(title="game settings", description="modify generic game settings")
    game_settings.add_argument("-r", "--rows", default=4, type=int, help="how many rows of enemies there are (default 5)")
    game_settings.add_argument("-c", "--columns", default=12, type=int, help="how many columns of enemies there are (default 9)")
    game_settings.add_argument("--width", default=1000, type=int, help="window width (default 1920)")
    game_settings.add_argument("--height", default=800, type=int, help="window height (default 1024)")
    game_settings.add_argument("-d", "--difficulty_step", default=25.0, type=float, help="increase the difficulty by this percent every round (default 25.0)")
    game_settings.add_argument("-n", "--name", default="Invader Clone", help="change the name of the game.")

    theme_settings = parser.add_argument_group(title="theme settings", description="modify generic theme settings")
    theme_settings.add_argument("-t", "--theme", default="default", help="change the theme of the game.")
    theme_settings.add_argument("-s", "--disable_stars", action='store_true', help='disable parallax stars effect')
    theme_settings.add_argument("-b", "--enable_background", action='store_true', help='enable a parallax bg effect')
    theme_settings.add_argument("--bg_speed", type=int, default=6, help='background scroll speed')
    theme_settings.add_argument("--title_bg_color", default="black", choices=colors, metavar="COLOR NAME", help="title background color"),
    theme_settings.add_argument("--game_bg_color", default="black", choices=colors, metavar="COLOR NAME", help="game background color"),
    theme_settings.add_argument("--leaderboard_bg_color", default="black", choices=colors, metavar="COLOR NAME", help="leaderboard background color")
    theme_settings.add_argument("--gameover_bg_color", default="black", choices=colors, metavar="COLOR NAME", help="gameover background color")

    mainmenu_text_settings = parser.add_argument_group(title="main menu text settings", description="modify text and text colors of the main menu")
    mainmenu_text_settings.add_argument("--alt_title", default=None, help="give your game an alternative title on the titlescreen")
    mainmenu_text_settings.add_argument("--subtitle1", default="全部のネコ宇宙人を倒す！ 動く：'←'／'→' 撃つ：'SPACE'", help="subtitle 1 text")
    mainmenu_text_settings.add_argument("--subtitle2", default="Kill all cat aliens! Move: '←'/'→' Shoot: 'SPACE'", help="subtitle 2 text")
    mainmenu_text_settings.add_argument("--press_any_key", default="Press ANY KEY!", help="press any key text")
    mainmenu_text_settings.add_argument("--victory", default="VICTORY!", help="victory text")
    mainmenu_text_settings.add_argument("--continueyn", default="Continue (Y/N)?", help="continue game text")
    mainmenu_text_settings.add_argument("--game_over", default="GAME OVER!", help="game over text")
    mainmenu_text_settings.add_argument("--title_text_color", default="ghostwhite", choices=colors, metavar="COLOR NAME", help="title text color")
    mainmenu_text_settings.add_argument("--subtitle1_text_color", default=None, choices=colors, metavar="COLOR NAME", help="subtitle 1 text color")
    mainmenu_text_settings.add_argument("--subtitle2_text_color", default=None, choices=colors, metavar="COLOR NAME", help="subtitle 2 text color")
    mainmenu_text_settings.add_argument("--press_any_key_text_color", default=None, choices=colors, metavar="COLOR NAME", help="press any key text color")

    args = parser.parse_args()

    if args.list_colors:
        for color in colors:
            print(f'{color} : ' + ('#%02x%02x%02x' % cd[color]))
        sys.exit(0)

    theme_dir = os.path.join(_data_dir, "themes", args.theme) if not os.path.isdir(os.path.join(_settingsdir, "themes", args.theme)) else os.path.join(_settingsdir, "themes", args.theme)

    if os.path.isfile(os.path.join(theme_dir, "theme.args")):
        var_args = vars(args)
        var_args_keys = var_args.keys()

        with open(os.path.join(theme_dir, "theme.args"), "r") as theme_args:
            lines = theme_args.readlines()

            for num, line in enumerate(lines):
                line_tuple = line.split('=')

                if len(line_tuple) != 2:
                    print(f"[Line {num + 1}] Error parsing theme.args. Invalid format: {line.rstrip()} (too many or too few assignment operators).")
                    sys.exit(-1)

                if line_tuple[0].strip() not in var_args_keys:
                    print(f"[Line {num + 1}] Error parsing theme.args. Invalid argument: {line_tuple[0].strip()}.")
                    sys.exit(-1)

                if f'--{line_tuple[0].strip()}' not in raw_args:
                    try:
                        typecast = type(var_args[line_tuple[0].strip()])

                        if typecast is bool and line_tuple[1].strip().lower() in ['0', 'false', None]:
                            val = False
                        else:
                            val = typecast(line_tuple[1].strip())

                        var_args[line_tuple[0].strip()] = val
                    except ValueError:
                        print(f"[Line {num + 1}] Error parsing theme.args. Could not cast {line_tuple[1].strip()} to type {type(var_args[line_tuple[0].strip()])}.")
                        sys.exit(-1)

    sys.exit(
        game.InvaderClone(
            name=args.name,
            width=args.width,
            height=args.height,
            enemy_rows=args.rows,
            enemy_cols=args.columns,
            difficulty_step=args.difficulty_step / 100.,
            theme=args.theme,
            stars=not args.disable_stars,
            bg=args.enable_background,
            alttitle=args.alt_title,
            sub1=args.subtitle1,
            sub2=args.subtitle2,
            pak=args.press_any_key,
            victorytext=args.victory,
            continuetext=args.continueyn,
            gameovertext=args.game_over,
            bg_speed=args.bg_speed,
            titlebg_color=cd[args.title_bg_color],
            gamebg_color=cd[args.game_bg_color],
            leaderboardbg_color=cd[args.leaderboard_bg_color],
            gameoverbg_color=cd[args.gameover_bg_color],
            title_color=cd[args.title_text_color],
            subtitle1_text_color=cd[args.subtitle1_text_color],
            subtitle2_text_color=cd[args.subtitle2_text_color],
            pak_text_color=cd[args.press_any_key_text_color],
            ).run()
        )

if __name__ == "__main__":
    main()

