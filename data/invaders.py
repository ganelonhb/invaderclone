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
            bg=args.enable_background

            ).run()
        )

if __name__ == "__main__":
    main()

