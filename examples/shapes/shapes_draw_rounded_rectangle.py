"""

raylib [shapes] example - Draw Rounded Rectangle

"""

# Import
# ------------------------------------------------------------------------------------
from pyray import *
from raylib.colors import (
    RAYWHITE,
    LIGHTGRAY,
    DARKGRAY,
    GOLD,
    MAROON,
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

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [shapes] example - draw rectangle rounded")

    roundness = 0.2
    width = 200
    height = 100
    segments = 0
    lineThick = 1

    draw_rect = False
    draw_rounded_rect = True
    draw_rounded_lines = False

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        rec = Rectangle((get_screen_width() - width - 250) / 2, (get_screen_height() - height) / 2, width, height)
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_line(560, 0, 560, get_screen_height(), fade(LIGHTGRAY, 0.6))
        draw_rectangle(560, 0, get_screen_width() - 500, get_screen_height(), fade(LIGHTGRAY, 0.3))

        if draw_rect:
            draw_rectangle_rec(rec, fade(GOLD, 0.6))
        if draw_rounded_rect:
            draw_rectangle_rounded(rec, roundness, segments, fade(MAROON, 0.2))
        if draw_rounded_lines:
            draw_rectangle_rounded_lines(rec, roundness, segments, lineThick, fade(MAROON, 0.4))

        # Draw GUI controls
        # ------------------------------------------------------------------------------
        width = int(gui_slider_bar(Rectangle(640, 40, 105, 20), "Width", 0, width, 0, get_screen_width() - 300))
        height = int(gui_slider_bar(Rectangle(640, 70, 105, 20), "Height", 0, height, 0, get_screen_height() - 50))
        roundness = gui_slider_bar(Rectangle(640, 140, 105, 20), "Roundness", 0, roundness, 0, 1)
        lineThick = int(gui_slider_bar(Rectangle(640, 170, 105, 20), "Thickness", 0, lineThick, 0, 20))
        segments = int(gui_slider_bar(Rectangle(640, 240, 105, 20), "Segments", 0, segments, 0, 60))

        draw_rounded_rect = gui_check_box(Rectangle(640, 320, 20, 20), "DrawRoundedRect", draw_rounded_rect)
        draw_rounded_lines = gui_check_box(Rectangle(640, 350, 20, 20), "DrawRoundedLines", draw_rounded_lines)
        draw_rect = gui_check_box(Rectangle(640, 380, 20, 20), "DrawRect", draw_rect)
        # ------------------------------------------------------------------------------

        draw_text(text_format("MODE: %s" % "MANUAL" if segments >= 4 else "AUTO"), 640, 280, 10, MAROON if segments >= 4 else DARKGRAY)

        draw_fps(10, 10)

        end_drawing()
        # ------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
