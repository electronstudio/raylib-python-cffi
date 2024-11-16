"""

raylib [texture] example - To image

"""
from pyray import *

# Initialization
screenWidth = 800
screenHeight = 450

init_window(screenWidth, screenHeight, "raylib [textures] example - texture to image")

# NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)

image = load_image("resources/raylib_logo.png")  # Load image data into CPU memory (RAM)
texture = load_texture_from_image(image)     # Image converted to texture, GPU memory (RAM -> VRAM)
unload_image(image)                                    # Unload image data from CPU memory (RAM)

image = load_image_from_texture(texture)               # Load image from GPU texture (VRAM -> RAM)
unload_texture(texture)                                # Unload texture from GPU memory (VRAM)

texture = load_texture_from_image(image)               # Recreate texture from retrieved image data (RAM -> VRAM)
unload_image(image)                                    # Unload retrieved image data from CPU memory (RAM)
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

    texture.width

    draw_texture(texture, int(screenWidth/2 - texture.width/2), int(screenHeight/2 - texture.height/2), WHITE)

    draw_text("this IS a texture loaded from an image!", 300, 370, 10, GRAY)

    end_drawing()
    # ----------------------------------------------------------------------------------

# De-Initialization
# ----------------------------------------------------------------------------------
unload_texture(texture)  # Unload render texture

close_window()  # Close window and OpenGL context
