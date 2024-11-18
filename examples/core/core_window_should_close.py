"""

raylib [core] example - Window Should Close

"""
from pyray import *

# Initialization
# --------------------------------------------------------------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [core] example - window should close")

set_exit_key(KeyboardKey.KEY_NULL)  # Disable KEY_ESCAPE to close window, X-button still works

exitWindowRequested = False  # Flag to request window to exit
exitWindow = False  # Flag to set window to exit

set_target_fps(60)  # Set our game to run at 60 frames-per-second
# --------------------------------------------------------------------------------------

# Main game loop
while not exitWindow:

    # Update
    # ----------------------------------------------------------------------------------
    #  Detect if X-button or KEY_ESCAPE have been pressed to close window
    if window_should_close() or is_key_pressed(KeyboardKey.KEY_ESCAPE):
        exitWindowRequested = True

    if exitWindowRequested:

        # A request for close window has been issued, we can save data before closing
        # or just show a message asking for confirmation

        if is_key_pressed(KeyboardKey.KEY_Y):
            exitWindow = True
        elif is_key_pressed(KeyboardKey.KEY_N):
            exitWindowRequested = False

    # ----------------------------------------------------------------------------------

    # Draw
    # ----------------------------------------------------------------------------------
    begin_drawing()

    clear_background(RAYWHITE)

    if exitWindowRequested:

        draw_rectangle(0, 100, SCREEN_WIDTH, 200, BLACK)
        draw_text("Are you sure you want to exit program? [Y/N]", 40, 180, 30, WHITE)

    else:
        draw_text("Try to close the window to get confirmation message!", 120, 200, 20, LIGHTGRAY)

    end_drawing()
    # ----------------------------------------------------------------------------------

# De-Initialization
close_window()  # Close window and OpenGL context
