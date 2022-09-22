## Python API Coding Style Conventions

Here is a list with some code conventions used by raylib in python:

| Code element        |             Convention              | Example                                      |
|-------------------- |:-----------------------------------:|----------------------------------------------|
| Variables           |              lowerCase              | `screenWidth = 0`, `targetFrameTime = 0.016` |
| Local variables     |              lowerCase              | ` playerPosition = Vector2(0, 0)`            |
| Global variables    |              lowerCase              | `windowReady = False`                        |
| Constants variables |              lowerCase              | `maxValue = 8`                               |
| Constants values    |              ALL_CAPS               | `MAX_BUILDINGS = 5`                          |
| float values        |             always x.x              | `gravity = 10.0`                             |
| Operators           |           value1 * value2           | `product = value * 6`                        |
| Operators           |           value1 / value2           | `division = value / 4`                       |
| Operators           |           value1 + value2           | `sum = value + 10`                           |
| Operators           |           value1 - value2           | `res = value - 5`                            |
| Class               |              TitleCase              | `class TextureFormat`                        |
| Enum Class members  |              ALL_CAPS               | `PIXELFORMAT_UNCOMPRESSED_R8G8B8`            |
| Class members       |              lowerCase              | `texture.width`, `color.r`                   |
| Functions           |    lowerCase & wordSeparationBy_    | `init_window()`, `window_should_close()`     |
| Functions params    |              lowerCase              | `width`, `height`                            |
| Ternary Operator    | result1 if (condition) else result2 | `print("yes" if (value == 0) else "no")`     |

Some other conventions to follow:
 - **ALWAYS** initialize all defined variables.
 - **use TABS / 4 spaces**.
 - Avoid trailing spaces, please, avoid them
 - Avoid using **semicolon** as you can
 - Control flow statements always are followed **by a space**:
```python
if condition : value = 0

while not window_should_close():
    #Do something here!

for i in range(NUM_VALUES): print(i)
```
 - All conditions checks are **always between parenthesis** but not boolean values:
```python
if value > 1 and value1 < 50 and valueActive:
    #Do something here!
```

**If proposing new functions, please try to use a clear naming for function-name and functions-parameters, in case of doubt, open an issue for discussion.**

## Import libraries and Module 
 - import libraries with the form `from library import *`
 - import modules/variables from libraries with the form `from library import (module1, ..., variable1, ...)`
```python
from pyray import *
from raylib.colors import (
    RAYWHITE,
    DARKGRAY,
    ...
)
```

## Files and Directories Naming Conventions
 
  - Directories will be named using `snake_case`: `resources/models`, `resources/fonts`
  
  - Files will be named using `snake_case`: `main_title.png`, `cubicmap.png`, `sound.wav`
  
_NOTE: Avoid any space or special character in the files/dir naming!_
  
## Games/Examples Directories Organization Conventions
  
 - Data files should be organized by context and usage in the game, think about the loading requirements for data and put all the resources that need to be loaded at the same time together.
 - Use descriptive names for the files, it would be perfect if just reading the name of the file, it was possible to know what is that file and where fits in the game.
 - Here is an example, note that some resources require to be loaded all at once while other require to be loaded only at initialization (gui, font).
  
```
resources/audio/fx/long_jump.wav
resources/audio/music/main_theme.ogg
resources/screens/logo/logo.png
resources/screens/title/title.png
resources/screens/gameplay/background.png
resources/characters/player.png
resources/characters/enemy_slime.png
resources/common/font_arial.ttf
resources/common/gui.png
```

## Example Conventions For Python API
 - examples ***should*** have the following structure
```python
"""

raylib [raylib module] example - name of the example

"""

# Import
# ------------------------------------------------------------------------------------
# Do something here!
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    # Do something here!
    # ------------------------------------------------------------------------------------

    # Main game loop
    while ... :  
        # Update
        # ----------------------------------------------------------------------------------
        # Do something here!
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        # Do something here!
        # ----------------------------------------------------------------------------------
    
    # De-Initialization
    # ----------------------------------------------------------------------------------
    # Do something here!
    # ----------------------------------------------------------------------------------

# execute the main function 
if __name__ == '__main__':
    main()
```
 - temple (basic window example):
```python
"""

raylib [core] example - Basic Window

"""

# Import
# ------------------------------------------------------------------------------------
from pyray import *
from raylib.colors import (
    RAYWHITE,
    LIGHTGRAY,
)
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [core] example - basic window")

    # TODO: Load resources / Initialize variables at this point
    
    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # TODO: Update variables / Implement example logic at this point
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)
        draw_text("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------

    # TODO: Unload all loaded resources at this point

    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# execute the main function 
if __name__ == '__main__':
    main()

```
