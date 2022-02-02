"""

raylib [core] example - Basic window

"""
import pyray
from raylib.colors import (
    RAYWHITE,
    LIGHTGRAY,
)





# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                  'raylib [core] example - basic window')
pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second


# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    # TODO: Update your variables here

    # Draw
    pyray.begin_drawing()

    pyray.clear_background(RAYWHITE)
    pyray.draw_text(
        'Congrats! You created your first window!', 190, 200, 20, LIGHTGRAY)

    pyray.end_drawing()


# De-Initialization
pyray.close_window()  # Close window and OpenGL context
