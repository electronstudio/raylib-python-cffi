"""

raylib [core] example - Window Should Close

"""

# Import
# ------------------------------------------------------------------------------------
from pyray import *
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # --------------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [core] example - window should close")

    set_exit_key(KeyboardKey.KEY_NULL)  # Disable KEY_ESCAPE to close window, X-button still works

    exit_window_requested = False  # Flag to request window to exit
    exit_window = False  # Flag to set window to exit

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not exit_window:
        # Update
        # ----------------------------------------------------------------------------------
        #  Detect if X-button or KEY_ESCAPE have been pressed to close window
        if window_should_close() or is_key_pressed(KeyboardKey.KEY_ESCAPE):
            exit_window_requested = True

        if exit_window_requested:
            # A request for close window has been issued, we can save data before closing
            # or just show a message asking for confirmation
            if is_key_pressed(KeyboardKey.KEY_Y):
                exit_window = True
            elif is_key_pressed(KeyboardKey.KEY_N):
                exit_window_requested = False
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        if exit_window_requested:
            draw_rectangle(0, 100, SCREEN_WIDTH, 200, BLACK)
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
