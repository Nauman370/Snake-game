# Snake Game

A snake game written in Python with pygame, made for Hack Club's **Terra** challenge.
It started as a plain green square on a black window and grew into a full game with a
difficulty menu, wrap-around mode, bonus fruits, snake skins and board themes.

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

pip install pygame-ce
python Snake.py
(pygame-ce is the community edition of pygame. It is used the same way, with import pygame, and it installs more reliably on new Python versions.)

Build the .exe yourself
pip install pyinstaller
python -m PyInstaller --onefile --windowed --name SnakeGame Snake.py
The finished file is dist/SnakeGame.exe.

How it works
The snake is just a list of grid positions, for example [(10, 10), (10, 9), (10, 8)], with the head first. Each move adds a new head and removes the tail. Growing means skipping the removal.
Game states: the main loop checks a state variable (menu, playing, paused, gameover) and only runs the game logic while it is playing.
Input queue: key presses are stored in a small queue and used one per move. Without it, pressing two keys inside one frame could turn the snake back into its own neck.
Settings are data. Presets, speeds, grid sizes, fruits, snake skins and board themes are all dictionaries, so adding a new one is a small change.
Wrap-around uses the remainder operator: x % columns brings a position that has left one edge back in on the other side.
Fixed window, variable cell size. The window is always 576x576 pixels. The grid sizes were chosen so 576 divides evenly by each of them, so the board always fills the window.
Bonus fruit timers count frames, not milliseconds, so they freeze when the game is paused.
