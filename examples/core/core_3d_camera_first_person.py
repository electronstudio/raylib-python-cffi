"""
raylib [core] example - 3d camera first person
adapted from   https://github.com/raysan5/raylib/blob/master/examples/core/core_3d_camera_first_person.c
"""

import pyray 

MAX_COLUMNS = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"raylib [core] example - 3d camera first person")

# Define the camera to look into our 3d world (position, target, up vector)
camera = pyray.Camera3D()
camera.position = pyray.Vector3(4.0, 2.0, 4.0)
camera.target = pyray.Vector3(0.0, 1.8, 0.0)
camera.up = pyray.Vector3(0.0, 1.0, 0.0)
camera.fovy = 60.0
camera.projection = pyray.CAMERA_PERSPECTIVE

# Generates some random columns
heights = [None] * MAX_COLUMNS
positions = [None] * MAX_COLUMNS
colors = [None] * MAX_COLUMNS

for i in range(MAX_COLUMNS):
    heights[i] = pyray.get_random_value(1, 12) * 1.0
    positions[i] = pyray.Vector3(pyray.get_random_value(-15, 15) * 1.0, heights[i]/2.0 * 1.0, pyray.get_random_value(-15, 15) * 1.0)
    colors[i] = pyray.Color(pyray.get_random_value(20, 255), pyray.get_random_value(10, 55), 30, 255)


pyray.set_target_fps(60)                

while not pyray.window_should_close():

    pyray.update_camera(camera, pyray.CAMERA_FIRST_PERSON)

    pyray.begin_drawing()

    pyray.clear_background(pyray.RAYWHITE)

    pyray.begin_mode_3d(camera)

    pyray.draw_plane(pyray.Vector3(0.0, 0.0, 0.0), pyray.Vector2(32.0, 32.0), pyray.LIGHTGRAY)
    pyray.draw_cube(pyray.Vector3(-16.0, 2.5, 0.0), 1.0, 5.0, 32.0, pyray.BLUE)
    pyray.draw_cube(pyray.Vector3(16.0, 2.5, 0.0), 1.0, 5.0, 32.0, pyray.LIME) 
    pyray.draw_cube(pyray.Vector3(0.0, 2.5, 16.0), 32.0, 5.0, 1.0, pyray.GOLD)

    for i in range(MAX_COLUMNS):
        pyray.draw_cube(positions[i], 2.0, heights[i], 2.0, colors[i])
        pyray.draw_cube_wires(positions[i], 2.0, heights[i], 2.0, pyray.MAROON)
    

    pyray.end_mode_3d()

    pyray.draw_rectangle( 10, 10, 220, 70, pyray.fade(pyray.SKYBLUE, 0.5))
    pyray.draw_rectangle_lines( 10, 10, 220, 70, pyray.BLUE)

    pyray.draw_text("First person camera default controls:", 20, 20, 10, pyray.BLACK)
    pyray.draw_text("- Move with keys: W, A, S, D", 40, 40, 10, pyray.DARKGRAY)
    pyray.draw_text("- Mouse move to look around", 40, 60, 10, pyray.DARKGRAY)

    pyray.end_drawing()

pyray.close_window()
