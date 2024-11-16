"""
raylib [core] example - 2d camera mouse zoom
"""

import pyray

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [core] example - 2d camera mouse zoom")

pyray.set_target_fps(60)

camera = pyray.Camera2D()

camera.zoom = 1.0

pyray.set_target_fps(60)

# main game loop
while not pyray.window_should_close():   
    # update
    if pyray.is_mouse_button_down(pyray.MouseButton.MOUSE_BUTTON_RIGHT):
        delta = pyray.get_mouse_delta()
        delta = pyray.vector2_scale(delta, -1.0 / camera.zoom)
        camera.target = pyray.vector2_add(camera.target, delta)

    # zoom based on mouse wheel
    wheel = pyray.get_mouse_wheel_move()
    if wheel != 0:

        mouseWorldPos = pyray.get_screen_to_world_2d(pyray.get_mouse_position(), camera)
        
        camera.offset = pyray.get_mouse_position()

        camera.target = mouseWorldPos

        ZOOM_INCREMENT = 0.125

        camera.zoom += (wheel*ZOOM_INCREMENT)
        if (camera.zoom < ZOOM_INCREMENT): camera.zoom = ZOOM_INCREMENT


    # draw
    pyray.begin_drawing()
    pyray.clear_background(pyray.BLACK)

    pyray.begin_mode_2d(camera)

    pyray.rl_push_matrix()
    pyray.rl_translatef(0, 25*50, 0)
    pyray.rl_rotatef(90, 1, 0, 0)
    pyray.draw_grid(100, 50)
    pyray.rl_pop_matrix()

    pyray.draw_circle(100, 100, 50, pyray.YELLOW)
            
    pyray.end_mode_2d()

    pyray.draw_text("Mouse right button drag to move, mouse wheel to zoom", 10, 10, 20, pyray.WHITE)
    
    pyray.end_drawing()

# de-Initialization
pyray.close_window()   

