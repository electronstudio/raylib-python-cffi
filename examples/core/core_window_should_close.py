"""

raylib [core] example - Window Should Close

"""

# Import
# ------------------------------------------------------------------------------------
from pyray import *
from raylib.colors import (
    RAYWHITE,
    LIGHTGRAY,
    WHITE,
    BLACK
)
from raylib import (
    KEY_NULL,
    KEY_ESCAPE,
    KEY_Y,
    KEY_N
)
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # --------------------------------------------------------------------------------------
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [core] example - window should close")

    set_exit_key(KEY_NULL)  # Disable KEY_ESCAPE to close window, X-button still works

    exitWindowRequested = False  # Flag to request window to exit
    exitWindow = False  # Flag to set window to exit

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not exitWindow:
        # Update
        # ----------------------------------------------------------------------------------
        #  Detect if X-button or KEY_ESCAPE have been pressed to close window
        if window_should_close() or is_key_pressed(KEY_ESCAPE):
            exitWindowRequested = True

        if exitWindowRequested:
            # A request for close window has been issued, we can save data before closing
            # or just show a message asking for confirmation
            if is_key_pressed(KEY_Y):
                exitWindow = True
            elif is_key_pressed(KEY_N):
                exitWindowRequested = False
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        if exitWindowRequested:
            draw_rectangle(0, 100, screenWidth, 200, BLACK)
            draw_text("Are you sure you want to exit program? [Y/N]", 40, 180, 30, WHITE)

        else:
            draw_text("Try to close the window to get confirmation message!", 120, 200, 20, LIGHTGRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# execute the main function
if __name__ == '__main__':
    main()
