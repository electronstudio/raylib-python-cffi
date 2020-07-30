"""

raylib [core] example - Mouse input

"""
from raylib.pyray import PyRay
from raylib.colors import (
    RAYWHITE,
    DARKGRAY,
    MAROON,
    DARKBLUE,
    LIME,
)


pyray = PyRay()


# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                  'raylib [core] example - mouse input')

ball_position = pyray.Vector2(-100, -100)
ball_color = DARKBLUE

pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second


# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    ball_position = pyray.get_mouse_position()

    if pyray.is_mouse_button_pressed(pyray.MOUSE_LEFT_BUTTON):
        ball_color = MAROON
    elif pyray.is_mouse_button_pressed(pyray.MOUSE_MIDDLE_BUTTON):
        ball_color = LIME
    elif pyray.is_mouse_button_pressed(pyray.MOUSE_RIGHT_BUTTON):
        ball_color = DARKBLUE

    # Draw
    pyray.begin_drawing()

    pyray.clear_background(RAYWHITE)
    pyray.draw_circle_v(ball_position, 40, ball_color)
    pyray.draw_text(
        'move ball with mouse and click mouse button to change color',
        10, 10, 20, DARKGRAY
    )

    pyray.end_drawing()


# De-Initialization
pyray.close_window()  # Close window and OpenGL context
