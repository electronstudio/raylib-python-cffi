import pyray
from raylib.colors import (
    RAYWHITE,
    DARKGRAY,
    DARKBLUE,
    SKYBLUE,
    MAROON,
    ORANGE,
    RED,
    VIOLET,
    BEIGE,
    BROWN,
    BLACK,
    GREEN,
    GOLD
)


# Initialization
screenWidth = 800
screenHeight = 450
pyray.init_window(screenWidth, screenHeight, "raylib [shapes] example - basic shapes drawing")

rotation = 0.0

pyray.set_target_fps(60)

# Main game loop
while not pyray.window_should_close():
    # Update
    rotation += 0.2

    # Draw
    pyray.begin_drawing()

    pyray.clear_background(RAYWHITE)

    pyray.draw_text("some basic shapes available on raylib", 20, 20, 20, DARKGRAY)

    # Circle shapes and lines
    pyray.draw_circle(screenWidth // 5, 120, 35, DARKBLUE)
    pyray.draw_circle_gradient(screenWidth // 5, 220, 60, GREEN, SKYBLUE)
    pyray.draw_circle_lines(screenWidth // 5, 340, 80, DARKBLUE)

    # Rectangle shapes and lines
    pyray.draw_rectangle(screenWidth // 4 * 2 - 60, 100, 120, 60, RED)
    pyray.draw_rectangle_gradient_h(screenWidth // 4 * 2 - 90, 170, 180, 130, MAROON, GOLD)
    pyray.draw_rectangle_lines(screenWidth // 4 * 2 - 40, 320, 80, 60, ORANGE)

    # Triangle shapes and lines
    pyray.draw_triangle(pyray.Vector2(screenWidth / 4.0 * 3.0, 80.0),
                     pyray.Vector2(screenWidth / 4.0 * 3.0 - 60.0, 150.0),
                     pyray.Vector2(screenWidth / 4.0 * 3.0 + 60.0, 150.0), VIOLET)

    pyray.draw_triangle_lines(pyray.Vector2(screenWidth / 4.0 * 3.0, 160.0),
                           pyray.Vector2(screenWidth / 4.0 * 3.0 - 20.0, 230.0),
                           pyray.Vector2(screenWidth / 4.0 * 3.0 + 20.0, 230.0), DARKBLUE)

    # Polygon shapes and lines
    pyray.draw_poly(pyray.Vector2(screenWidth / 4.0 * 3, 330), 6, 80, rotation, BROWN)
    pyray.draw_poly_lines(pyray.Vector2(screenWidth / 4.0 * 3, 330), 6, 90, rotation, BROWN)
    pyray.draw_poly_lines_ex(pyray.Vector2(screenWidth / 4.0 * 3, 330), 6, 85, rotation, 6, BEIGE)

    # NOTE: We draw all LINES based shapes together to optimize internal drawing,
    # this way, all LINES are rendered in a single draw pass
    pyray.draw_line(18, 42, screenWidth - 18, 42, BLACK)

    pyray.end_drawing()

# De-Initialization
pyray.close_window()
