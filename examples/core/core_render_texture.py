"""

raylib [core] example - render texture
version 6.0.1.1

"""

import pyray

# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [core] example - render texture")

# Define a render texture to render
text_width = 300
text_height = 300
target = pyray.load_render_texture(text_width, text_height)

ball_pos = pyray.Vector2(text_width / 2.0, text_height / 2.0)
ball_speed = pyray.Vector2(5.0, 4.0)
ball_radius = 20.0

rotation = 0.0

pyray.set_target_fps(60)
# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update

    # Ball movement logic
    ball_pos.x += ball_speed.x
    ball_pos.y += ball_speed.y

    # Check walls collision for bouncing
    if (ball_pos.x >= (text_width - ball_radius)) or (ball_pos.x <= ball_radius):
        ball_speed.x *= -1.0
    if (ball_pos.y >= (text_height - ball_radius)) or (ball_pos.y <= ball_radius):
        ball_speed.y *= -1.0

    # Render texture rotation
    rotation += 0.5

    # Draw

    # Draw our scene to the render texture
    pyray.begin_texture_mode(target)

    pyray.clear_background(pyray.SKYBLUE)
    pyray.draw_rectangle(0, 0, 20, 20, pyray.RED)
    pyray.draw_circle_v(ball_pos, ball_radius, pyray.MAROON)

    pyray.end_texture_mode()

    # Draw render texture to main framebuffer
    pyray.begin_drawing()

    pyray.clear_background(pyray.RAYWHITE)

    # Draw our render texture with rotation applied
    # NOTE 1: We set the origin of the texture to the center of the render texture
    # NOTE 2: We flip vertically the texture setting negative source rectangle height
    pyray.draw_texture_pro(
        target.texture,
        pyray.Rectangle(0, 0, text_width, -text_height),
        pyray.Rectangle(
            SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0, text_width, text_height
        ),
        pyray.Vector2(text_width / 2.0, text_height / 2.0),
        rotation,
        pyray.WHITE,
    )
    pyray.draw_text(
        "DRAWING BOUNCING BALL INSIDE RENDER TEXTURE!",
        10,
        SCREEN_HEIGHT - 40,
        20,
        pyray.BLACK,
    )

    pyray.draw_fps(10, 10)

    pyray.end_drawing()

# De-Initialization
pyray.close_window()  # Close window and OpenGL context
