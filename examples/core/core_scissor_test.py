"""

raylib [core] example - Scissor Test

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

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [core] example - scissor test")

    scissor_area = Rectangle(0, 0, 300, 300)
    scissor_mode = True

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_key_pressed(KeyboardKey.KEY_S):
            scissor_mode = not scissor_mode

        # Centre the scissor area around the mouse position
        scissor_area.x = get_mouse_x() - scissor_area.width/2
        scissor_area.y = get_mouse_y() - scissor_area.height/2
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        if scissor_mode:
            begin_scissor_mode(int(scissor_area.x), int(scissor_area.y), int(scissor_area.width), int(scissor_area.height))

        # Draw full screen rectangle and some text
        # NOTE: Only part defined by scissor area will be rendered
        draw_rectangle(0, 0, get_screen_width(), get_screen_height(), RED)
        draw_text("Move the mouse around to reveal this text!", 190, 200, 20, LIGHTGRAY)

        if scissor_mode:
            end_scissor_mode()

        draw_rectangle_lines_ex(scissor_area, 1, BLACK)
        draw_text("Press S to toggle scissor test", 10, 10, 20, BLACK)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
