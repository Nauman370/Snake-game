Snake Game

A snake game written in Python with pygame, made for Hack Club's Terra challenge. It started as a plain green square on a black window and grew into a full game with a difficulty menu, wrap-around mode, bonus fruits, snake skins and board themes.


Download and play

Windows: get SnakeGame.exe from the latest release and double-click it. Nothing needs to be installed.

Windows may show a "Windows protected your PC" warning because the app is not code-signed. Click More info, then Run anyway. All of the source code is in this repository, so you can read exactly what it does or run it yourself (see below).

Features
Difficulty menu
7 presets: Easiest, EZ_PZ, EZ, normal, abnormal, HELP and NUH Uh.
Custom difficulty: pick your own speed and grid size.
Speeds: slow, normal, fast, faster, fastest
Grid sizes: small (18x18), normal (24x24), big (32x32), bigger (36x36), biggest (48x48)
Wrap-around mode: the easier presets let the snake come out of the opposite edge instead of dying at the wall. The harder ones keep the walls deadly. In custom games you choose.
Fruit
Apple: +1 point, always on the board.
Banana and orange: bonus fruits that show up at random, give extra points and make the snake grow extra segments. They disappear after a few seconds if you do not reach them.
Look and feel
6 snake skins: blue, green, purple, red, golden, black.
5 board themes: grass, desert, night, ice, candy.
Animated stripes moving along the snake's body, an arrow on the head that shows which way it is facing, and a tongue that flicks out now and then.
A translucent controls strip at the bottom of the screen (press H to hide it).
Pause screen, fullscreen toggle and a game over screen with restart, menu and quit.
Controls
Key	Action
W A S D or Arrow keys	Move the snake
P	Pause / resume
H	Hide / show the controls strip
F11	Toggle fullscreen
Enter	Restart after game over
M	Back to the menu (while paused or after game over)
Esc	Quit

The menu is mouse-driven: click a preset to start straight away, or choose a speed, a grid size and wrap mode and press Start Custom. The Snake and Board buttons cycle through the skins and themes.

Run from source

You need Python 3 and pygame-ce.

bash
pip install pygame-ce
python Snake.py

(pygame-ce is the community edition of pygame. It is used the same way, with import pygame, and it installs more reliably on new Python versions.)



Download and play

Windows: get SnakeGame.exe from the latest release and double-click it. Nothing needs to be installed.

Windows may show a "Windows protected your PC" warning because the app is not code-signed. Click More info, then Run anyway. All of the source code is in this repository, so you can read exactly what it does or run it yourself (see below).

Features
Difficulty menu
7 presets: Easiest, EZ_PZ, EZ, normal, abnormal, HELP and NUH Uh.
Custom difficulty: pick your own speed and grid size.
Speeds: slow, normal, fast, faster, fastest
Grid sizes: small (18x18), normal (24x24), big (32x32), bigger (36x36), biggest (48x48)
Wrap-around mode: the easier presets let the snake come out of the opposite edge instead of dying at the wall. The harder ones keep the walls deadly. In custom games you choose.
Fruit
Apple: +1 point, always on the board.
Banana and orange: bonus fruits that show up at random, give extra points and make the snake grow extra segments. They disappear after a few seconds if you do not reach them.
Look and feel
6 snake skins: blue, green, purple, red, golden, black.
5 board themes: grass, desert, night, ice, candy.
Animated stripes moving along the snake's body, an arrow on the head that shows which way it is facing, and a tongue that flicks out now and then.
A translucent controls strip at the bottom of the screen (press H to hide it).
Pause screen, fullscreen toggle and a game over screen with restart, menu and quit.
Controls
Key	Action
W A S D or Arrow keys	Move the snake
P	Pause / resume
H	Hide / show the controls strip
F11	Toggle fullscreen
Enter	Restart after game over
M	Back to the menu (while paused or after game over)
Esc	Quit

The menu is mouse-driven: click a preset to start straight away, or choose a speed, a grid size and wrap mode and press Start Custom. The Snake and Board buttons cycle through the skins and themes.

Run from source

You need Python 3 and pygame-ce.

bash
pip install pygame-ce
python Snake.py

(pygame-ce is the community edition of pygame. It is used the same way, with import pygame, and it installs more reliably on new Python versions.)

Build the .exe yourself
bash
pip install pyinstaller
python -m PyInstaller --onefile --windowed --name SnakeGame Snake.py

The finished file is dist/SnakeGame.exe.


AI disclosure

I used AI at a few points for debugging, i made  most of the game myself but at some points i couldnt figure out the problems so ised AI.
on -m PyInstaller --onefile --windowed --name SnakeGame Snake.py

The finished file is dist/SnakeGame.exe.
