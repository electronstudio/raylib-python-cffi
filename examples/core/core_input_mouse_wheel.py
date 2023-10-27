"""

raylib [core] example - Mouse Wheel Input

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

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [core] example - input mouse wheel")

    box_position_y = SCREEN_HEIGHT // 2 - 40
    scroll_speed = 4  # Scrolling speed in pixels

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        box_position_y -= int(get_mouse_wheel_move() * scroll_speed)
        # --------------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_rectangle(SCREEN_WIDTH // 2 - 40, box_position_y, 80, 80, MAROON)

        draw_text("User mouse wheel to move the cube up and down!", 10, 10, 20, GRAY)
        draw_text("Box position Y: {:03d}".format(box_position_y), 10, 40, 20, LIGHTGRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()

