from pyray import *
import math
#Initialization

screenWidth = 800
screenHeight = 450

virtualScreenWidth = 160
virtualScreenHeight = 90

virtualRatio = screenWidth/ virtualScreenWidth

init_window(screenWidth, screenHeight, "raylib [core] example - smooth pixel-perfect camera")

worldSpaceCamera = Camera2D([0])  # Game world camera
worldSpaceCamera.zoom = 1.0

screenSpaceCamera = Camera2D([0]) # Smoothing camera
screenSpaceCamera.zoom = 1.0

target = load_render_texture(virtualScreenWidth, virtualScreenHeight); # This is where we'll draw all our objects.

rec01 = Rectangle(70.0, 35.0, 20.0, 20.0)
rec02 = Rectangle(90.0, 55.0, 30.0, 10.0)
rec03 = Rectangle(80.0, 65.0, 15.0, 25.0)

# The target's height is flipped (in the source Rectangle), due to OpenGL reasons
sourceRec = Rectangle(0.0, 0.0, target.texture.width, -target.texture.height)
destRec = Rectangle(-virtualRatio, -virtualRatio, screenWidth + (virtualRatio*2), screenHeight + (virtualRatio*2))

origin = Vector2(0.0, 0.0)

rotation = 0.0

cameraX = 0.0
cameraY = 0.0

set_target_fps(60)

# Main game loop
while not window_should_close(): # Detect window close button or ESC key

    # Update

    rotation += 60.0 *get_frame_time();   # Rotate the rectangles, 60 degrees per second

    # Make the camera move to demonstrate the effect
    cameraX = (math.sin(get_time())*50.0) - 10.0
    cameraY = math.cos(get_time())*30.0

    # Set the camera's target to the values computed above
    screenSpaceCamera.target = Vector2(cameraX, cameraY)

    # Round worldSpace coordinates, keep decimals into screenSpace coordinates
    worldSpaceCamera.target.x = screenSpaceCamera.target.x
    screenSpaceCamera.target.x -= worldSpaceCamera.target.x
    screenSpaceCamera.target.x *= virtualRatio

    worldSpaceCamera.target.y = screenSpaceCamera.target.y
    screenSpaceCamera.target.y -= worldSpaceCamera.target.y
    screenSpaceCamera.target.y *= virtualRatio

    begin_texture_mode(target)
    clear_background(RAYWHITE)

    begin_mode_2d(worldSpaceCamera)
    draw_rectangle_pro(rec01, origin, rotation, BLACK)
    draw_rectangle_pro(rec02, origin, -rotation, RED)
    draw_rectangle_pro(rec03, origin, rotation + 45.0, BLUE)
    end_mode_2d()
    end_texture_mode()

    begin_drawing()
    clear_background(RED)

    begin_mode_2d(screenSpaceCamera)
    draw_texture_pro(target.texture, sourceRec, destRec, origin, 0.0, WHITE)
    end_mode_2d()

    draw_text(text_format("Screen resolution: %ix%i", screenWidth, screenHeight), 10, 10, 20, DARKBLUE)
    draw_text(text_format("World resolution: %ix%i", virtualScreenWidth, virtualScreenHeight), 10, 40, 20, DARKGREEN)
    draw_fps(get_screen_width() - 95, 10)
    end_drawing()


# De-Initialization

unload_render_texture(target)   # Unload render texture

close_window()                # Close window and OpenGL context