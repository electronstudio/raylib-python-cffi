"""

raylib [core] example - Keyboard input

"""
import pyray


# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'raylib [core] example - keyboard input')
ball_position = pyray.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second


# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    if pyray.is_key_down(pyray.KEY_RIGHT):
        ball_position.x += 2
    if pyray.is_key_down(pyray.KEY_LEFT):
        ball_position.x -= 2
    if pyray.is_key_down(pyray.KEY_UP):
        ball_position.y -= 2
    if pyray.is_key_down(pyray.KEY_DOWN):
        ball_position.y += 2

    # Draw
    pyray.begin_drawing()

    pyray.clear_background(pyray.RAYWHITE)
    pyray.draw_text('move the ball with arrow keys', 10, 10, 20, pyray.DARKGRAY)
    pyray.draw_circle_v(ball_position, 50, pyray.MAROON)

    pyray.end_drawing()


# De-Initialization
pyray.close_window()  # Close window and OpenGL context
