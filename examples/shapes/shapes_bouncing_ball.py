import pyray

# Initialization
screenWidth = 800
screenHeight = 450
pyray.init_window(screenWidth, screenHeight, "pyray [shapes] example - bouncing ball")

ballPosition = pyray.Vector2(pyray.get_screen_width() / 2.0, pyray.get_screen_height() / 2.0)
ballSpeed = pyray.Vector2(5.0, 4.0)
ballRadius = 20

pause = False
framesCounter = 0

pyray.set_target_fps(60)

# Main game loop
while not pyray.window_should_close():
    # Update
    if pyray.is_key_pressed(pyray.KeyboardKey.KEY_SPACE):
        pause = not pause

    if not pause:
        ballPosition.x += ballSpeed.x
        ballPosition.y += ballSpeed.y

        # Check walls collision for bouncing
        if (ballPosition.x >= (pyray.get_screen_width() - ballRadius)) or (ballPosition.x <= ballRadius):
            ballSpeed.x *= -1.0
        if (ballPosition.y >= (pyray.get_screen_height() - ballRadius)) or (ballPosition.y <= ballRadius):
            ballSpeed.y *= -1.0
    else:
        framesCounter += 1

    # Draw
    pyray.begin_drawing()

    pyray.clear_background(pyray.RAYWHITE)

    pyray.draw_circle_v(ballPosition, ballRadius, pyray.MAROON)
    pyray.draw_text("PRESS SPACE to PAUSE BALL MOVEMENT", 10, pyray.get_screen_height() - 25, 20, pyray.LIGHTGRAY)

    # On pause, we draw a blinking message
    if pause and (framesCounter // 30) % 2:
        pyray.draw_text("PAUSED", 350, 200, 30, pyray.GRAY)

    pyray.draw_fps(10, 10)

    pyray.end_drawing()

# De-Initialization
pyray.close_window()
