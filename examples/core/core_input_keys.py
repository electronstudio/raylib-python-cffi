"""

raylib [core] example - Keyboard input

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
    # ----------------------------------------------------------------------------------
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [core] example - keyboard input")

    ball_position = Vector2(screenWidth / 2, screenHeight / 2)

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ----------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_key_down(KeyboardKey.KEY_RIGHT): ball_position.x += 2
        if is_key_down(KeyboardKey.KEY_LEFT): ball_position.x -= 2
        if is_key_down(KeyboardKey.KEY_UP): ball_position.y -= 2
        if is_key_down(KeyboardKey.KEY_DOWN): ball_position.y += 2
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_text("move the ball with arrow keys", 10, 10, 20, DARKGRAY)

        draw_circle_v(ball_position, 50, MAROON)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# execute the main function
if __name__ == '__main__':
    main()

