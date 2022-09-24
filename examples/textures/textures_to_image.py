"""

raylib [texture] example - To Image

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
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [textures] example - texture to image")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)

    image = load_image("resources/raylib_logo.png")  # Load image data into CPU memory (RAM)
    texture = load_texture_from_image(image)         # Image converted to texture, GPU memory (RAM -> VRAM)
    unload_image(image)                              # Unload image data from CPU memory (RAM)

    image = load_image_from_texture(texture)         # Load image from GPU texture (VRAM -> RAM)
    unload_texture(texture)                          # Unload texture from GPU memory (VRAM)

    texture = load_texture_from_image(image)         # Recreate texture from retrieved image data (RAM -> VRAM)
    unload_image(image)                              # Unload retrieved image data from CPU memory (RAM)
    # ---------------------------------------------------------------------------------------

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

        draw_texture(texture, int(SCREEN_WIDTH/2 - texture.width/2), int(SCREEN_HEIGHT/2 - texture.height/2), WHITE)

        draw_text("this IS a texture loaded from an image!", 300, 370, 10, GRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
