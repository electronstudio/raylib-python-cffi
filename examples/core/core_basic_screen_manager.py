from pyray import *
from enum import Enum, auto

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450


class GameScreen(Enum):
    LOGO = auto()
    TITLE = auto()
    GAMEPLAY = auto()
    ENDING = auto()


def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [core] example - basic screen manager")

    frame_count = 0
    set_target_fps(60)
    current_screen = GameScreen.LOGO

    while not window_should_close():

        # State machine
        if current_screen == GameScreen.LOGO:
            frame_count += 1
            if frame_count > 120:
                current_screen = GameScreen.TITLE
        elif current_screen == GameScreen.TITLE:
            if is_key_pressed(KeyboardKey.KEY_ENTER) or is_gesture_detected(Gesture.GESTURE_TAP):
                current_screen = GameScreen.GAMEPLAY
        elif current_screen == GameScreen.GAMEPLAY:
            if is_key_pressed(KeyboardKey.KEY_ENTER) or is_gesture_detected(Gesture.GESTURE_TAP):
                current_screen = GameScreen.ENDING
        elif current_screen == GameScreen.ENDING:
            if is_key_pressed(KeyboardKey.KEY_ENTER) or is_gesture_detected(Gesture.GESTURE_TAP):
                current_screen = GameScreen.TITLE

        begin_drawing()
        clear_background(RAYWHITE)
        if current_screen == GameScreen.LOGO:
            draw_text("LOGO SCREEN", 20, 20, 40, LIGHTGRAY)
            draw_text("WAIT for 2 SECONDS...", 290, 220, 20, GRAY)
        elif current_screen == GameScreen.TITLE:
            draw_rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, GREEN)
            draw_text("TITLE SCREEN", 20, 20, 40, DARKGREEN)
            draw_text("PRESS ENTER or TAP to JUMP to GAMEPLAY SCREEN", 120, 220, 20, DARKGREEN)
        elif current_screen == GameScreen.GAMEPLAY:
            draw_rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, PURPLE)
            draw_text("GAMEPLAY SCREEN", 20, 20, 40, MAROON)
            draw_text("PRESS ENTER or TAP to JUMP to ENDING SCREEN", 120, 220, 20, MAROON)
        elif current_screen == GameScreen.ENDING:
            draw_rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, BLUE)
            draw_text("ENDING SCREEN", 20, 20, 40, DARKBLUE)
            draw_text("PRESS ENTER or TAP to JUMP to TITLE SCREEN", 120, 220, 20, DARKBLUE)
        end_drawing()
    close_window()


if __name__ == '__main__':
    main()
