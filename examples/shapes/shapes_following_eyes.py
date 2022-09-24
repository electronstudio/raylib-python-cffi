"""

raylib [shapes] example - Following Eyes

"""

# Import
# ------------------------------------------------------------------------------------
from pyray import *
from raylib.colors import (
    RAYWHITE,
    BROWN,
    BLACK,
    LIGHTGRAY,
    DARKGREEN,
)
from math import (
    atan2,
    cos,
    sin
)
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ----------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [shapes] example - following eyes")

    scleraLeftPosition = Vector2(SCREEN_WIDTH / 2.0 - 100.0, SCREEN_HEIGHT / 2.0)
    scleraRightPosition = Vector2(SCREEN_WIDTH / 2.0 + 100.0, SCREEN_HEIGHT / 2.0)
    sclera_radius = 80.0

    irisLeftPosition = Vector2(SCREEN_WIDTH / 2.0 - 100.0, SCREEN_HEIGHT / 2.0)
    irisRightPosition = Vector2(SCREEN_WIDTH / 2.0 - 100.0, SCREEN_HEIGHT / 2.0)
    iris_radius = 24.0

    angle = 0.0
    dx, dy, dxx, dyy = 0.0, 0.0, 0.0, 0.0

    set_target_fps(60)
    # ----------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        irisLeftPosition = get_mouse_position()
        irisRightPosition = get_mouse_position()

        # Check not inside the left eye sclera
        if not check_collision_point_circle(irisLeftPosition, scleraLeftPosition, sclera_radius - 20):
            dx = irisLeftPosition.x - scleraLeftPosition.x
            dy = irisLeftPosition.y - scleraLeftPosition.y

            angle = atan2(dy, dx)

            dxx = (sclera_radius - iris_radius) * cos(angle)
            dyy = (sclera_radius - iris_radius) * sin(angle)

            irisLeftPosition.x = scleraLeftPosition.x + dxx
            irisLeftPosition.y = scleraLeftPosition.y + dyy

        # Check not inside the right eye sclera
        if not check_collision_point_circle(irisRightPosition, scleraRightPosition, sclera_radius - 20):
            dx = irisRightPosition.x - scleraRightPosition.x
            dy = irisRightPosition.y - scleraRightPosition.y

            angle = atan2(dy, dx)

            dxx = (sclera_radius - iris_radius) * cos(angle)
            dyy = (sclera_radius - iris_radius) * sin(angle)

            irisRightPosition.x = scleraRightPosition.x + dxx
            irisRightPosition.y = scleraRightPosition.y + dyy
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_circle_v(scleraLeftPosition, sclera_radius, LIGHTGRAY)
        draw_circle_v(irisLeftPosition, iris_radius, BROWN)
        draw_circle_v(irisLeftPosition, 10, BLACK)

        draw_circle_v(scleraRightPosition, sclera_radius, LIGHTGRAY)
        draw_circle_v(irisRightPosition, iris_radius, DARKGREEN)
        draw_circle_v(irisRightPosition, 10, BLACK)

        draw_fps(10, 10)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
