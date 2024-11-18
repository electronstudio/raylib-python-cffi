from pyray import *

# Initialization
screenWidth = 800
screenHeight = 450

init_window(screenWidth, screenHeight, "raylib [core] example - 3d camera free")

# Define the camera to look into our 3d world
camera = Camera3D()
camera.position = Vector3(10.0, 10.0, 10.0)  # Camera position
camera.target = Vector3(0.0, 0.0, 0.0)       # Camera looking at point
camera.up = Vector3(0.0, 1.0, 0.0)           # Camera up vector (rotation towards target)
camera.fovy = 45.0                           # Camera field-of-view Y
camera.projection = CameraProjection.CAMERA_PERSPECTIVE       # Camera projection type

cubePosition = Vector3(0.0, 0.0, 0.0)

disable_cursor()                  # Limit cursor to relative movement inside the window

set_target_fps(60)                 # Set our game to run at 60 frames-per-second

# Main game loop
while not window_should_close():   # Detect window close button or ESC key
    # Update
    update_camera(camera, CameraMode.CAMERA_FREE)

    if is_key_pressed(KeyboardKey.KEY_Z):
        camera.target = Vector3(0.0, 0.0, 0.0)

    # Draw
    begin_drawing()

    clear_background(RAYWHITE)

    begin_mode_3d(camera)

    draw_cube(cubePosition, 2.0, 2.0, 2.0, RED)
    draw_cube_wires(cubePosition, 2.0, 2.0, 2.0, MAROON)

    draw_grid(10, 1.0)

    end_mode_3d()

    draw_rectangle(10, 10, 320, 93, fade(SKYBLUE, 0.5))
    draw_rectangle_lines(10, 10, 320, 93, BLUE)

    draw_text("Free camera default controls:", 20, 20, 10, BLACK)
    draw_text("- Mouse Wheel to Zoom in-out", 40, 40, 10, DARKGRAY)
    draw_text("- Mouse Wheel Pressed to Pan", 40, 60, 10, DARKGRAY)
    draw_text("- Alt + Mouse Wheel Pressed to Rotate", 40, 80, 10, DARKGRAY)
    draw_text("- Alt + Ctrl + Mouse Wheel Pressed for Smooth Zoom", 40, 100, 10, DARKGRAY)
    draw_text("- Z to zoom to (0, 0, 0)", 40, 120, 10, DARKGRAY)

    end_drawing()

# De-Initialization
close_window()  # Close window and OpenGL context
