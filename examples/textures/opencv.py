import cv2 as cv
from pyray import *

opencv_image = cv.imread("resources/raylib_logo.jpg")
if opencv_image is None:
    exit("Could not read the image.")

screenWidth = 800
screenHeight = 450
init_window(screenWidth, screenHeight, "example - image loading")

pointer_to_image_data = ffi.from_buffer(opencv_image.data)
raylib_image = Image(pointer_to_image_data, 256, 256, 1, PIXELFORMAT_UNCOMPRESSED_R8G8B8)
texture = load_texture_from_image(raylib_image)
unload_image(raylib_image)

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)
    draw_texture(texture, int(screenWidth/2 - texture.width/2), int(screenHeight/2 - texture.height/2), WHITE)
    end_drawing()

unload_texture(texture)
close_window()


