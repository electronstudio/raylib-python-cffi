"""
raylib [core] example - 2D Camera Mouse Zoom
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
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [core] example - 2d camera mouse zoom")

    camera = Camera2D()
    camera.zoom = 1.0

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ----------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT):
            delta = get_mouse_delta()
            delta = vector2_scale(delta, -1.0 / camera.zoom)
            camera.target = vector2_add(camera.target, delta)

        # zoom based on mouse wheel
        wheel = get_mouse_wheel_move()
        if wheel != 0:

            mouseWorldPos = get_screen_to_world_2d(get_mouse_position(), camera)

            camera.offset = get_mouse_position()

            camera.target = mouseWorldPos

            zoomIncrement = 0.125

            camera.zoom += wheel * zoomIncrement
            if camera.zoom < zoomIncrement: camera.zoom = zoomIncrement

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(BLACK)

        begin_mode_2d(camera)

        rl_push_matrix()
        rl_translatef(0, 25*50, 0)
        rl_rotatef(90, 1, 0, 0)
        draw_grid(100, 50)
        rl_pop_matrix()

        draw_circle(100, 100, 50, YELLOW)

        end_mode_2d()

        draw_text("Mouse right button drag to move, mouse wheel to zoom", 10, 10, 20, WHITE);

        end_drawing()
        # ----------------------------------------------------------------------------------

        # De-Initialization
        # ----------------------------------------------------------------------------------
        close_window()  # Close window and OpenGL context
        # ----------------------------------------------------------------------------------

    # Execute the main function
    if __name__ == '__main__':
        main()
