"""

raylib [shapes] example - Cubic-bezier lines

"""

# Import
# ------------------------------------------------------------------------------------
from pyray import *
from raylib.colors import (
    RAYWHITE,
    GRAY,
    RED
)
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    set_config_flags(ConfigFlags.FLAG_MSAA_4X_HINT)
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [shapes] example - cubic-bezier lines")

    start = Vector2(0, 0)
    end = Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # -------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT): start = get_mouse_position()
        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT): end = get_mouse_position()
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_text("USE MOUSE LEFT-RIGHT CLICK to DEFINE LINE START and END POINTS", 15, 20, 20, GRAY)

        draw_line_bezier(start, end, 2.0, RED)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function 
if __name__ == '__main__':
    main()
