# Invader Clone

[![PyPI](https://img.shields.io/badge/PyPI-v0.9.0-blue.svg)](https://pypi.org/project/invaderclone/) [![GitHub](https://img.shields.io/badge/GitHub-v0.9.0-purple.svg)](https://github.com/ganelonhb/invaderclone)

## Project Description

Invader Clone is a ridiculously configurable clone of Space Invaders written in Python. Just about every game setting is swappable using the many available command-line arguments.

If you really wish, you can even create your own custom level using the API.

Documentation that will help you do all of this is on its way. While you wait, here's the condensed version of the project's usage!

## Install

There are two planned options for the installation of Invader Clone. You can install the game either by using pip, or by downloading a launcher for your OS in the Releases section on GitHub.

### Pip

To install using pip, use the following command:

`pip install invaderclone`

If your system package manager manages your python packages, you can instead use the following command (PLEASE READ THE WARNING BELOW\*\*\*):

`pip install invaderclone --break-system-packages`

\*\*\*It's probably okay if you do this, but you should probably install python pygame using your system package manager BEFORE installing Invader Clone using this method.

### Launcher

You can either build the launcher from source, or you can download the latest version from GitHub Releases.

There is a version available for Windows and Linux. A Mac version may or may not come in the future. I haven't quite figured out how I'd do that.

You can also find the Game's page on Itch.io. If you like the project, please make a donation through the Itch.io storefront! I won't buy a cup of coffee with it, I promise! I will probably put it towards gas in California.

## Usage

If you've installed the game through Pip, you can type `invaderclone` into the terminal to run it.

If you downloaded a launcher, double click on the executable file launch it. You will need an internet connection the first time you run this, because the launcher will try to set up a virtual environment in you game directory, and it will install pygame as well.

Running the game without any arguments will simply run the game. To see the vast bounty of switches and options you can use to modify your copy of the game, you can type `invaderclone --help` into the command line.

## Themeing

To learn how to theme your game in-depth, read the CREATING_THEMES.md file that can be found in this repository.

In summary, you can place your theme in the config directory chosen for your OS (~/.config/invaderclone on Linux, C:\\users\\YOU\\Documents\\invaderclone)

## Custom Levels

Documentation will be written on creating custom levels, but it can be done! A custom level can be placed in your config directory (see above). Name your custom level levelN.py, where N is a postive integer that is not 0 (00 probably works).

In it, you must define a class that inherits from invaderclone.Scene, or it must inherit from a class that inherits from invaderclone.Scene that I will talk about in the Documentation to come. The class MUST BE NAMED LevelN, where N is the same number you named the script. There are no limits, if you know pygame, you can do anything you want.

If you need help creating your Scene, study the workings of the game in this repo.
