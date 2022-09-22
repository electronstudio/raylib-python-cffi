"""

raylib [shapes] example - Logo Raylib

"""

# Import
# ------------------------------------------------------------------------------------
from pyray import *
from raylib.colors import (
    RAYWHITE,
    BLACK,
    GRAY
)
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ----------------------------------------------------------------------------------
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, 'raylib [shapes] example - raylib logo using shapes')

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ----------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # TODO: Update your variables here
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_rectangle(int(screenWidth/2 - 128), int(screenHeight/2 - 128), 256, 256, BLACK)
        draw_rectangle(int(screenWidth/2 - 112), int(screenHeight/2 - 112), 224, 224, RAYWHITE)
        draw_text("raylib", int(screenWidth/2 - 44), int(screenHeight/2 + 48), 50, BLACK)

        draw_text("this is NOT a texture!", 350, 370, 10, GRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()

