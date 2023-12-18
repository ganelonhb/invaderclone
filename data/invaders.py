#!/usr/bin/env python3

"""
Imports the the game demo and executes the main function.
"""

import sys
import os
import argparse
# pylint: disable=import-error
from videogame import game

def main():
    parser = argparse.ArgumentParser(
        prog="Invader Clone",
        description="A configurable clone of Space Invaders written as part of a school project in Pygame.",
        epilog="For comments, questions, concerns, inquiries, or any other synonyms of those words, contact me at worcesterz@outlook.com."
        )

    parser.add_argument("-r", "--rows", default=4, type=int, help="how many rows of enemies there are (default 5)")
    parser.add_argument("-c", "--columns", default=12, type=int, help="how many columns of enemies there are (default 9)")
    parser.add_argument("--width", default=1920, type=int, help="window width (default 1920)")
    parser.add_argument("--height", default=1024, type=int, help="window height (default 1024)")
    parser.add_argument("-d", "--difficulty_step", default=5.0, type=float, help="increase the difficulty by this percent every round (default 5.0)")
    parser.add_argument("-n", "--name", default="Invader Clone", help="change the name of the game.")
    parser.add_argument("-t", "--theme", default="default", help="change the theme of the game.")
    parser.add_argument("-s", "--disable_stars", action='store_false', help='disable parallax stars effect')
    parser.add_argument("-b", "--enable_background", action='store_true', help='enable a parallax bg effect')
    parser.add_argument("--bg_speed", type=int, default=6, help='background scroll speed')
    parser.add_argument("--alt_title", default=None, help="give your game an alternative title on the titlescreen")
    parser.add_argument("--subtitle1", default="全部のネコ宇宙人を倒す！ 動く：'←'／'→' 撃つ：'SPACE'", help="subtitle 1 text")
    parser.add_argument("--subtitle2", default="Kill all cat aliens! Move: '←'/'→' Shoot: 'SPACE'", help="subtitle 2 text")
    parser.add_argument("--press_any_key", default="Press ANY KEY!", help="press any key text")
    parser.add_argument("--victory", default="VICTORY!", help="victory text")
    parser.add_argument("--continueyn", default="Continue (Y/N)?", help="continue game text")
    parser.add_argument("--game_over", default="GAME OVER!", help="game over text")


    args = parser.parse_args()

    sys.exit(
        game.InvaderClone(
            name=args.name,
            width=args.width,
            height=args.height,
            enemy_rows=args.rows,
            enemy_cols=args.columns,
            difficulty_step=args.difficulty_step / 100,
            theme=args.theme,
            stars=args.disable_stars,
            bg=args.enable_background,
            alttitle=args.alt_title,
            sub1=args.subtitle1,
            sub2=args.subtitle2,
            pak=args.press_any_key,
            victorytext=args.victory,
            continuetext=args.continueyn,
            gameovertext=args.game_over,
            bg_speed=args.bg_speed
            ).run()
        )

if __name__ == "__main__":
    main()

