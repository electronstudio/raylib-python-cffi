"""

raylib [core] example - Input Gestures Detection

"""
from raylib.pyray import PyRay, makeStructHelper
from raylib.static import ffi
from raylib.colors import (
    RAYWHITE,
    LIGHTGRAY,
    DARKGRAY,
    MAROON,
    DARKBLUE,
    LIME,
    GRAY,
)


pyray = PyRay()

# Initialization
MAX_GESTURE_STRINGS = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                  'raylib [core] example - input gestures')

touch_position = pyray.Vector2(0, 0)
touch_area = pyray.Rectangle(220, 10, SCREEN_WIDTH - 230, SCREEN_HEIGHT - 20)

gesture_strings = []

current_gesture = pyray.GESTURE_NONE
last_gesture = pyray.GESTURE_NONE

GESTURE_LABELS = {
    pyray.GESTURE_TAP: 'GESTURE TAP',
    pyray.GESTURE_DOUBLETAP: 'GESTURE DOUBLETAP',
    pyray.GESTURE_HOLD: 'GESTURE HOLD',
    pyray.GESTURE_DRAG: 'GESTURE DRAG',
    pyray.GESTURE_SWIPE_RIGHT: 'GESTURE SWIPE RIGHT',
    pyray.GESTURE_SWIPE_LEFT: 'GESTURE SWIPE LEFT',
    pyray.GESTURE_SWIPE_UP: 'GESTURE SWIPE UP',
    pyray.GESTURE_SWIPE_DOWN: 'GESTURE SWIPE DOWN',
    pyray.GESTURE_PINCH_IN: 'GESTURE PINCH IN',
    pyray.GESTURE_PINCH_OUT: 'GESTURE PINCH OUT',
}

pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second


# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    last_gesture = current_gesture
    current_gesture = pyray.get_gesture_detected()
    touch_position = pyray.get_touch_position(0)

    if (
        pyray.check_collision_point_rec(touch_position, touch_area)
        and current_gesture != pyray.GESTURE_NONE
    ):
        if current_gesture != last_gesture:
            gesture_strings.append(GESTURE_LABELS[current_gesture])

        # Reset gestures strings
        if len(gesture_strings) >= MAX_GESTURE_STRINGS:
            gesture_strings = []

    # Draw
    pyray.begin_drawing()

    pyray.clear_background(RAYWHITE)

    pyray.draw_rectangle_rec(touch_area, GRAY)
    pyray.draw_rectangle(225, 15, SCREEN_WIDTH - 240, SCREEN_HEIGHT - 30,
                         RAYWHITE)

    pyray.draw_text(
        'GESTURES TEST AREA',
        SCREEN_WIDTH - 270, SCREEN_HEIGHT - 40, 20, pyray.fade(GRAY, 0.5)
    )

    pyray.draw_rectangle(10, 29, 200, SCREEN_HEIGHT - 50, GRAY)
    pyray.draw_text('DETECTED GESTURES', 50, 15, 10, GRAY)

    for i, val in enumerate(gesture_strings):
        if i % 2 == 0:
            pyray.draw_rectangle(
                10, 30 + 20 * i, 200, 20, pyray.fade(LIGHTGRAY, 0.5))
        else:
            pyray.draw_rectangle(
                10, 30 + 20 * i, 200, 20, pyray.fade(LIGHTGRAY, 0.3))

        if i < len(gesture_strings) - 1:
            pyray.draw_text(val, 35, 36 + 20 * i, 10, DARKGRAY)
        else:
            pyray.draw_text(val, 35, 36 + 20 * i, 10, MAROON)


    if current_gesture != pyray.GESTURE_NONE:
        pyray.draw_circle_v(touch_position, 30, MAROON)


    pyray.end_drawing()


# De-Initialization
pyray.close_window()  # Close window and OpenGL context
