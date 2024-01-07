# How To Create a Theme

Creating a theme for Invader Clone should not be too difficult. The game simply reads the theme folders for files with particular naming conventions. For example, the player's sprite is handled by a file in the images folder of your theme, 'hero.png.' All images must be png images.

To create a theme, you need to create a directory that contains a small number of files. You then place the folder into one of the two theme directories that the program searches (really, you should only be using one of them).

Place your theme in C:\\Users\\\<your username\>\\Documents\\invaderclone\\themes (Windows) or /home/\<your username\>/.config/invaderclone/themes on (Linux).

Run the game with the command-line option --theme "folder_name" (using the folder name of your theme) to play!

The rest of this document will go further into detail about each step along the way. If you are familiar with computers you can probably skip reading these steps, but if you are a novice or simply want to learn more about improving your theme (changing text colors, background colors, etc.), then you should read more!

## Step 1 - Finding the Themes Directory

You can find the themes folder in one of two places on your computer.

Among the game files, you will find a themes folder where the default theme is stored. You should really not be using this folder, but if you place your theme in there it will be found by the program and it will work! This directory is meant to be used in the future if I decide to ship the game with more themes.

The directory you should be using can be found in your Documents folder if you are on Windows, under \\invaderclone\\themes.

If this folder doesn't exist, you can create it, or run the game at least once. Invader Clone will automatically create it.

On Linux, you can find your themes folder in your home directory under /.config/invaderclone/themes/. Again, you can either create the folder yourself or run the game at least once to create it.

If you cannot find the folders, and you've already run the game, try checking the folder permissions of your Documents or home directory. Something is probably wrong with them.

## Step 2 - Structuring Your Theme

Once you've found the themes folder, create a new folder in that directory. Name it whatever you want. This will be the name that you use to select your theme. By convention, I like to use names that contain no whitespace, lowercase letters, and only standard QWERTY keys. You can do what you want, I won't stop you. I just have particular reasons that I do this that I will leave up to exploration for you.

Your theme folder should have this structure:

\<your theme name\><br />
├── bgm<br />
│   ├─ game_over.ogg<br />
│   ├─ game.ogg<br />
│   ├─ leaderboard.ogg<br />
│   └─ title.ogg<br />
├── bgs<br />
│   ├─ explode.ogg<br />
│   └─ explode+kitty.ogg<br />
├── fonts<br />
│   ├─ other.ttf<br />
│   └─ title.ttf<br />
└── images<br />
    ├─ bg.png (optional)<br />
    ├─ badbullet.png<br />
    ├─ burst.png<br />
    ├─ enemy*.png<br />
    ├─ explosion.png<br />
    ├─ gameover.png<br />
    ├─ goodbullet.png<br />
    ├─ hero.png<br />
    ├─ obstacle*.png<br />
    ├─ second_hero.png<br />
    └─ title.png<br />

Right now, all you have to do is create the folders "bgm", "bgs", "fonts", and "images."

## Step 3 - BGM & BGS

There are four audio files that are accepted by the game in the 'bgm' folder. They are 'game_over.ogg,' 'game.ogg,' 'leaderboard.ogg,' and 'title.ogg.' If you leave any of these files out, an annoying buzz sound will play. If you want, you can supress the buzz using a setting that will be explained later. Each of these songs are played during different game states. It shouldn't be too hard to figure it out based on the filename.

In the 'bgs' folder, the filenames are 'explode.ogg' (used when anything explodes) and 'explode+kitty.ogg' (sometimes played when an enemy explodes instead of the default explosion).

## Step 4 - Fonts

Only two fonts are used by the game. You must use the .ttf format for your font to be recognized. You can convert your fonts to this format online. Here's a helpful alternative option if you know what you're looking at:

fontforge -lang=ff -c 'Open($1); Generate($2); Close();' input.otf other.ttf

If you do not supply a font, a gibberish font will be used instead. Again, you can use a theme setting to ignore an unset font and use a readable one instead from the default fonts.

## Step 5 - Images

You don't have to be an artist to create your own theme! Slap a picture of your cat into this folder and call it a day!

The images in this folder fall into a few categories of nuance, so I will go through each of them here:

### Image Type 1: Square Images

The following images must be square (that is, their width is equal to their height in pixels):
- enemy*.png (see type 3 as well)
- explosion.png
- gameover.png
- hero.png
- second_hero.png
- title.png

### Image Type 2: Unbound Images

The following images are rendered at their actual size, and are not resized by the game to match the resolution. You can make them any size or aspect ratio you want, but you might break the game or make it look funky!
- badbullet.png
- burst.png
- goodbullet.png
- obstacle*.png

### Image Type 3: Regex Images

The following images have special properties that allow you to have multiple types of enemies or obstacles in your game.

Any file that has the format
- enemy*.png
or
- obstacle*.png
where the asterisk (*) is zero or more characters will be added to a list of enemies/obstacles used by the game. The list is ordered by alphabet, so use that to your advantage.

Obstacles are selected at random, and descend from the top of the screen at random intervals.

Enemies, however, follow a particular pattern. Each row of enemies will contain enemies of the same type. The first row is the first enemy in the folder by alphabet. Each row is a new kind of enemy until the number of new kinds run out. The last kind will just be repeated until no more rows need to be rendered.

For example, in the default theme. The round cat spaceship at the back of the row is enemy1.png. The sharp cat in the second row is enemy2.png. The two rows of catfish (yep, that's what those are) are both enemy3.png. Further rows after those last two will continue to be catfish.

### Image Type 4: Optional Images

All background images are optional, however they must have their respective names to be discovered by the theme engine.

If you want your game to use a background image on a particular screen, you will need to read Steps 6 and/or 7. Not to worry, for they are next!


## Step 6 - Command Line Options

Some settings cannot be swapped out by simply adding a file to a directory. Or, not as far as you're concerned, yet! To change in-game settings, you can pass options to the executable from the command line. What? If you don't know what a command line is and don't care, just skip to Step 7! No, really, it's fine! If you know how to use the command line, however, please read.

This game uses the command line to handle in-game settings. Nearly every setting is configureable. You can really fine-tune your game by changing settings.

Included in the Docs dir (alongside this very file) is a file called help.txt. It includes the output of the game's ```--help``` command. You can read about every setting there.

This game is intended to be configured to your preference. Use the various command line options to change settings on the fly if you are running your game from the command line.

## Step 7 - The default.args And theme.args Files

You may grow tired of using the command line to set your options every time. That's okay, I won't get sad that all of that work I did went to waste!

If you want to make your settings more permanent, you can make a file in the same directory as the executable file titled ```default.args```. You can set command line options in this file, and it will be read at the start of of execution. This way, you can save settings you like!

The command line options will now override options that you set in the ```default.args``` file (if present), rather than overriding the hard-coded default settings.

The structure of the ```default.args``` file is as follows:

```
cli_option1=value2
cli_option2=value2
...
cli_optionN=valueN
```

You must seperate each option by using a new line. You can have as many assignment operators ('=' sign) as you want in one line, as only the first '=' sign is counted as an assignment.

If you're making a theme, you can do the same thing using a file called ```theme.args```. This can be really helpful if you want to change font colors, use a scrolling background, or do other things! If you are not using the default theme, ```default.args``` is not used.
