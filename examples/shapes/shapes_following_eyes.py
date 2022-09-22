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
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [shapes] example - following eyes")

    scleraLeftPosition = Vector2(screenWidth / 2.0 - 100.0, screenHeight / 2.0)
    scleraRightPosition = Vector2(screenWidth / 2.0 + 100.0, screenHeight / 2.0)
    scleraRadius = 80.0

    irisLeftPosition = Vector2(screenWidth / 2.0 - 100.0, screenHeight / 2.0)
    irisRightPosition = Vector2(screenWidth / 2.0 - 100.0, screenHeight / 2.0)
    irisRadius = 24.0

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
        if not check_collision_point_circle(irisLeftPosition, scleraLeftPosition, scleraRadius - 20):
            dx = irisLeftPosition.x - scleraLeftPosition.x
            dy = irisLeftPosition.y - scleraLeftPosition.y

            angle = atan2(dy, dx)

            dxx = (scleraRadius - irisRadius)*cos(angle)
            dyy = (scleraRadius - irisRadius)*sin(angle)

            irisLeftPosition.x = scleraLeftPosition.x + dxx
            irisLeftPosition.y = scleraLeftPosition.y + dyy

        # Check not inside the right eye sclera
        if not check_collision_point_circle(irisRightPosition, scleraRightPosition, scleraRadius - 20):
            dx = irisRightPosition.x - scleraRightPosition.x
            dy = irisRightPosition.y - scleraRightPosition.y

            angle = atan2(dy, dx)

            dxx = (scleraRadius - irisRadius)*cos(angle)
            dyy = (scleraRadius - irisRadius)*sin(angle)

            irisRightPosition.x = scleraRightPosition.x + dxx
            irisRightPosition.y = scleraRightPosition.y + dyy
        # ----------------------------------------------------------------------------------

        # draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_circle_v(scleraLeftPosition, scleraRadius, LIGHTGRAY)
        draw_circle_v(irisLeftPosition, irisRadius, BROWN)
        draw_circle_v(irisLeftPosition, 10, BLACK)

        draw_circle_v(scleraRightPosition, scleraRadius, LIGHTGRAY)
        draw_circle_v(irisRightPosition, irisRadius, DARKGREEN)
        draw_circle_v(irisRightPosition, 10, BLACK)

        draw_fps(10, 10)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# execute the main function
if __name__ == '__main__':
    main()
