"""

raylib [core] example - Scissor Test

"""
from pyray import *


# Initialization
# --------------------------------------------------------------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [core] example - scissor test")

scissorArea = Rectangle(0, 0, 300, 300)
scissorMode = True

set_target_fps(60)  # Set our game to run at 60 frames-per-second
# --------------------------------------------------------------------------------------

# Main game loop
while not window_should_close():  # Detect window close button or ESC key
    # Update
    # ----------------------------------------------------------------------------------
    if is_key_pressed(KEY_S):
        scissorMode = not scissorMode

    # Centre the scissor area around the mouse position
    scissorArea.x = get_mouse_x() - scissorArea.width/2
    scissorArea.y = get_mouse_y() - scissorArea.height/2
    # ----------------------------------------------------------------------------------


    # Draw
    # ----------------------------------------------------------------------------------
    begin_drawing()

    clear_background(RAYWHITE)
    if scissorMode:
        begin_scissor_mode(int(scissorArea.x), int(scissorArea.y), int(scissorArea.width), int(scissorArea.height))

    # Draw full screen rectangle and some text
    # NOTE: Only part defined by scissor area will be rendered
    draw_rectangle(0, 0, get_screen_width(), get_screen_height(), RED)
    draw_text("Move the mouse around to reveal this text!", 190, 200, 20, LIGHTGRAY)

    if scissorMode:
        end_scissor_mode()

    draw_rectangle_lines_ex(scissorArea, 1, BLACK)
    draw_text("Press S to toggle scissor test", 10, 10, 20, BLACK)

    end_drawing()

# De-Initialization
close_window()  # Close window and OpenGL context
