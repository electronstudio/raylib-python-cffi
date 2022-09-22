"""

raylib [core] example - Input Gestures Detection

"""

# Import
# ------------------------------------------------------------------------------------
from pyray import *
from raylib.colors import (
    RAYWHITE,
    LIGHTGRAY,
    DARKGRAY,
    MAROON,
    GRAY,
)
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ----------------------------------------------------------------------------------
    MAX_GESTURE_STRINGS = 20
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [core] example - input gestures")

    touch_position = Vector2(0, 0)
    touch_area = Rectangle(220, 10, screenWidth - 230, screenHeight - 20)

    gesture_strings = []

    current_gesture = Gesture.GESTURE_NONE
    last_gesture = Gesture.GESTURE_NONE

    GESTURE_LABELS = {
        Gesture.GESTURE_TAP: 'GESTURE TAP',
        Gesture.GESTURE_DOUBLETAP: 'GESTURE DOUBLETAP',
        Gesture.GESTURE_HOLD: 'GESTURE HOLD',
        Gesture.GESTURE_DRAG: 'GESTURE DRAG',
        Gesture.GESTURE_SWIPE_RIGHT: 'GESTURE SWIPE RIGHT',
        Gesture.GESTURE_SWIPE_LEFT: 'GESTURE SWIPE LEFT',
        Gesture.GESTURE_SWIPE_UP: 'GESTURE SWIPE UP',
        Gesture.GESTURE_SWIPE_DOWN: 'GESTURE SWIPE DOWN',
        Gesture.GESTURE_PINCH_IN: 'GESTURE PINCH IN',
        Gesture.GESTURE_PINCH_OUT: 'GESTURE PINCH OUT',
    }

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ----------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        last_gesture = current_gesture
        current_gesture = get_gesture_detected()
        touch_position = get_touch_position(0)

        if check_collision_point_rec(touch_position, touch_area) and current_gesture != Gesture.GESTURE_NONE :
            if current_gesture != last_gesture:
                gesture_strings.append(GESTURE_LABELS[current_gesture])

            # Reset gestures strings
            if len(gesture_strings) >= MAX_GESTURE_STRINGS:
                gesture_strings = []
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        draw_rectangle_rec(touch_area, GRAY)
        draw_rectangle(225, 15, screenWidth - 240, screenHeight - 30, RAYWHITE)
        draw_text("GESTURES TEST AREA", screenWidth - 270, screenHeight - 40, 20, fade(GRAY, 0.5)
        )

        for i, val in enumerate(gesture_strings):
            if i % 2 == 0:
                draw_rectangle(10, 30 + 20 * i, 200, 20, fade(LIGHTGRAY, 0.5))
            else:
                draw_rectangle(10, 30 + 20 * i, 200, 20, fade(LIGHTGRAY, 0.3))

            if i < len(gesture_strings) - 1:
                draw_text(val, 35, 36 + 20 * i, 10, DARKGRAY)
            else:
                draw_text(val, 35, 36 + 20 * i, 10, MAROON)

        draw_rectangle_lines(10, 29, 200, screenHeight - 50, GRAY)
        draw_text('DETECTED GESTURES', 50, 15, 10, GRAY)

        if current_gesture != Gesture.GESTURE_NONE:
            draw_circle_v(touch_position, 30, MAROON)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# execute the main function
if __name__ == '__main__':
    main()
