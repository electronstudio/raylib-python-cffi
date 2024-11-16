"""
raylib [core] example - 3d camera mode
adapted from https://github.com/raysan5/raylib/blob/master/examples/core/core_3d_camera_mode.c
"""

import pyray

# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [core] example - 3d camera mode")

# Define the camera to look into our 3d world
camera = pyray.Camera3D([0])
camera.position = pyray.Vector3(0.0, 10.0, 10.0)   # Camera position
camera.target = pyray.Vector3(0.0, 0.0, 0.0)       # Camera looking at point
camera.up = pyray.Vector3(0.0, 1.0, 0.0)           # Camera up vector (rotation towards target)
camera.fovy = 45.0                                 # Camera field-of-view Y
camera.projection = pyray.CameraProjection.CAMERA_PERSPECTIVE       # Camera mode type

cube_position = pyray.Vector3(0.0, 0.0, 0.0)

pyray.set_target_fps(60)              

# Main game loop
while not pyray.window_should_close():

    # Draw
    pyray.begin_drawing()

    pyray.clear_background(pyray.RAYWHITE)

    pyray.begin_mode_3d(camera)

    pyray.draw_cube(cube_position, 2.0, 2.0, 2.0, pyray.RED)
    pyray.draw_cube_wires(cube_position, 2.0, 2.0, 2.0, pyray.MAROON)

    pyray.draw_grid(10, 1.0)

    pyray.end_mode_3d()

    pyray.draw_text("Welcome to the third dimension!", 10, 40, 20, pyray.DARKGRAY)

    pyray.draw_fps(10, 10)

    pyray.end_drawing()

# De-Initialization
pyray.close_window()

