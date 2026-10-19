# DeadenD

A visual novel made with [Ren'Py](https://www.renpy.org/). Alpha version 0.1, originally developed in 2018 with Ren'Py 6.99.13.

## Running the game

1. Install the Ren'Py SDK from <https://www.renpy.org/latest.html>.
2. Open the Ren'Py launcher, go to **Preferences → Projects Directory** and select the folder that contains this `DeadenD` folder.
3. Select **DeadenD** in the project list and click **Launch Project**.

## Layout

```
game/
  script.rpy        characters, images and audio definitions
  script/           story chapters (prologue, Monday to Thursday, n_deadend)
  screens.rpy       UI screens, including the credits
  gui.rpy, gui/     GUI configuration and graphics
  options.rpy       project options and build settings
  images/           backgrounds (Ambientazione) and sprites (Personaggi)
  audio/bgm/        background music
  audio/sounds/     sound effects (sources in audio/sounds/CREDITS.md)
```

Ren'Py regenerates `cache/`, `*.rpyc`, saves and logs on launch; they are not tracked.

## Credits and licenses

- Sprites by Elzee, CC BY-NC-SA 4.0
- Music by Kevin MacLeod (incompetech.com), CC BY 3.0
- Sound effects from Freesound, CC0
- Backgrounds: royalty free (Café Memoria set: only cropping, color changes, filters and scaling allowed)

The full credits are in the game's Credits screen.
