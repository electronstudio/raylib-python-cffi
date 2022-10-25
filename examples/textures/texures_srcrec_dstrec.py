"""

raylib [textures] example - Texture source and destination rectangles

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
    # ------------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [textures] examples - texture source and destination rectangles")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)

    scarfy = load_texture("resources/scarfy.png")  # Texture loading

    frame_width = scarfy.width / 6
    frame_height = scarfy.height

    # Source rectangle (part of the texture to use for drawing)
    source_rec = Rectangle(0, 0, frame_width, frame_height)

    # Destination rectangle (screen rectangle where drawing part of texture)
    dest_rec = Rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, frame_width*2, frame_height*2)

    # Origin of the texture (rotation/scale point), it's relative to destination rectangle size
    origin = Vector2(frame_width, frame_height)

    rotation = 0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        rotation += 1
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        # NOTE: Using DrawTexturePro() we can easily rotate and scale the part of the texture we draw
        # sourceRec defines the part of the texture we use for drawing
        # destRec defines the rectangle where our texture part will fit (scaling it to fit)
        # origin defines the point of the texture used as reference for rotation and scaling
        # rotation defines the texture rotation (using origin as rotation point)

        draw_texture_pro(scarfy, source_rec, dest_rec, origin, rotation, WHITE)

        draw_line(int(dest_rec.x), 0, int(dest_rec.x), SCREEN_HEIGHT, GRAY)
        draw_line(0, int(dest_rec.y), SCREEN_WIDTH, int(dest_rec.y), GRAY)

        draw_text("(c) Scarfy sprite by Eiden Marsal", SCREEN_WIDTH - 200, SCREEN_HEIGHT - 20, 10, GRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
