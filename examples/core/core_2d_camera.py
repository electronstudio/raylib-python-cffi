"""

raylib [core] example - 2D Camera System

"""
import pyray

from raylib.colors import (
    RAYWHITE,
    DARKGRAY,
    RED,
    GREEN,
    SKYBLUE,
    BLUE,
    BLACK,
)




# Initialization
MAX_BUILDINGS = 100
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                  'raylib [core] example - 2d camera')

player = pyray.Rectangle(400, 280, 40, 40)
buildings = []
build_colors = []
spacing = 0

for i in range(MAX_BUILDINGS):
    width = pyray.get_random_value(50, 200)
    height = pyray.get_random_value(100, 800)
    y = SCREEN_HEIGHT - 130 - height
    x = -6000 + spacing

    buildings.append(pyray.Rectangle(x, y, width, height))

    spacing += width

    build_colors.append(pyray.Color(
        pyray.get_random_value(200, 240),
        pyray.get_random_value(200, 240),
        pyray.get_random_value(200, 250),
        255
    ))

camera = pyray.Camera2D()
camera.target = pyray.Vector2(player.x + 20, player.y + 20)
camera.offset = pyray.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
camera.rotation = 0.0
camera.zoom = 1.0

pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second


# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update

    # Player movement
    if pyray.is_key_down(pyray.KEY_RIGHT):
        player.x += 2
    elif pyray.is_key_down(pyray.KEY_LEFT):
        player.x -= 2

    # Camera target follows player
    camera.target = pyray.Vector2(player.x + 20, player.y + 20)

    # Camera rotation controls
    if pyray.is_key_down(pyray.KEY_A):
        camera.rotation -= 1
    elif pyray.is_key_down(pyray.KEY_S):
        camera.rotation += 1

    # Limit camera rotation to 80 degrees (-40 to 40)
    if camera.rotation > 40:
        camera.rotation = 40
    elif camera.rotation < -40:
        camera.rotation = -40

    # Camera zoom controls
    camera.zoom += pyray.get_mouse_wheel_move() * 0.05

    if camera.zoom > 3.0:
        camera.zoom = 3.0
    elif camera.zoom < 0.1:
        camera.zoom = 0.1

    # Camera reset (zoom and rotation)
    if pyray.is_key_pressed(pyray.KEY_R):
        camera.zoom = 1.0
        camera.rotation = 0.0

    # Draw
    pyray.begin_drawing()
    pyray.clear_background(RAYWHITE)

    pyray.begin_mode_2d(camera)

    pyray.draw_rectangle(-6000, 320, 13000, 8000, DARKGRAY)

    for i in range(MAX_BUILDINGS):
        pyray.draw_rectangle_rec(buildings[i], build_colors[i])

    pyray.draw_rectangle_rec(player, RED)

    x = int(camera.target.x)
    y = int(camera.target.y)
    pyray.draw_line(x, -SCREEN_HEIGHT * 10, x, SCREEN_HEIGHT * 10, GREEN)
    pyray.draw_line(-SCREEN_WIDTH * 10, y, SCREEN_WIDTH * 10, y, GREEN)

    pyray.end_mode_2d()

    pyray.draw_text('SCREEN AREA', 640, 10, 20, RED)

    pyray.draw_rectangle(0, 0, SCREEN_WIDTH, 5, RED)
    pyray.draw_rectangle(0, 5, 5, SCREEN_HEIGHT - 10, RED)
    pyray.draw_rectangle(SCREEN_WIDTH - 5, 5, 5, SCREEN_HEIGHT - 10, RED)
    pyray.draw_rectangle(0, SCREEN_HEIGHT - 5, SCREEN_WIDTH, 5, RED)

    pyray.draw_rectangle(10, 10, 250, 113, pyray.fade(SKYBLUE, 0.5))
    pyray.draw_rectangle_lines(10, 10, 250, 113, BLUE)

    pyray.draw_text('Free 2d camera controls:', 20, 20, 10, BLACK)
    pyray.draw_text('- Right/Left to move Offset', 40, 40, 10, DARKGRAY)
    pyray.draw_text('- Mouse Wheel to Zoom in-out', 40, 60, 10, DARKGRAY)
    pyray.draw_text('- A / S to Rotate', 40, 80, 10, DARKGRAY)
    pyray.draw_text('- R to reset Zoom and Rotation', 40, 100, 10, DARKGRAY)

    pyray.end_drawing()


# De-Initialization
pyray.close_window()  # Close window and OpenGL context
