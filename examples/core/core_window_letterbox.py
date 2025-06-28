"""

raylib [core] example - window scale letterbox (and virtual mouse)
    tested with: Python 3.13.3, raylib 5.5.0.2

"""

import pyray
from pyray import Color, Rectangle, Vector2

from pyray import (
    RAYWHITE,
    GREEN,
    YELLOW,
    BLACK,
)

# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

# Enable config flags for resizable window and vertical synchro
pyray.set_config_flags(
    pyray.ConfigFlags.FLAG_WINDOW_RESIZABLE | pyray.ConfigFlags.FLAG_VSYNC_HINT
)

pyray.init_window(
    SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [core] example - window scale letterbox"
)

pyray.set_window_min_size(320, 240)


gameScreenWidth = 640
gameScreenHeight = 480

# Render texture initialization, used to hold the rendering result so we can easily resize it
target = pyray.load_render_texture(gameScreenWidth, gameScreenHeight)
pyray.set_texture_filter(target.texture, pyray.TextureFilter.TEXTURE_FILTER_BILINEAR)

colors = []
for _ in range(10):
    colors.append(
        Color(
            pyray.get_random_value(100, 250),
            pyray.get_random_value(50, 150),
            pyray.get_random_value(10, 100),
            255,
        )
    )

pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second


# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    # TODO: Update your variables here

    #  Compute required framebuffer scaling
    scale = min(
        float(pyray.get_screen_width() / gameScreenWidth),
        float(pyray.get_screen_height() / gameScreenHeight),
    )

    if pyray.is_key_pressed(pyray.KeyboardKey.KEY_SPACE):
        # Recalculate random colors for the bars
        for color in colors:
            color = Color(
                pyray.get_random_value(100, 250),
                pyray.get_random_value(50, 150),
                pyray.get_random_value(10, 100),
                255,
            )

    # Update virtual mouse (clamped mouse value behind game screen)
    mouse = pyray.get_mouse_position()
    virtualMouse = Vector2()
    virtualMouse.x = (
        mouse.x - (pyray.get_screen_width() - (gameScreenWidth * scale)) * 0.5
    ) / scale
    virtualMouse.y = (
        mouse.x - (pyray.get_screen_height() - (gameScreenHeight * scale)) * 0.5
    ) / scale

    virtualMouse = pyray.vector2_clamp(
        virtualMouse,
        Vector2(0, 0),
        Vector2(float(gameScreenWidth), float(gameScreenHeight)),
    )

    pyray.begin_texture_mode(target)
    pyray.clear_background(RAYWHITE)

    for i, color in enumerate(colors):
        pyray.draw_rectangle(
            0,
            int((gameScreenHeight / 10) * i),
            gameScreenWidth,
            int(gameScreenHeight / 10),
            color,
        )

        pyray.draw_text(
            f"Default Mouse: [{int(mouse.x)}, {int(mouse.y)}]", 350, 25, 20, GREEN
        )
        pyray.draw_text(
            f"Default Mouse: [{int(virtualMouse.x)}, {int(virtualMouse.y)}]",
            350,
            55,
            20,
            YELLOW,
        )
    pyray.end_texture_mode()

    pyray.begin_drawing()
    pyray.clear_background(BLACK)
    pyray.draw_texture_pro(
        target.texture,
        Rectangle(
            0.0,
            0.0,
            float(target.texture.width),
            float(-target.texture.height),
        ),
        Rectangle(
            (pyray.get_screen_width() - float(gameScreenWidth) * scale) * 0.5,
            (pyray.get_screen_height() - float(gameScreenHeight) * scale) * 0.5,
            float(gameScreenWidth) * scale,
            float(gameScreenHeight) * scale,
        ),
        Vector2(0.0, 0.0),
        0.0,
        RAYWHITE,
    )

    pyray.end_drawing()

# De-Initialization
pyray.unload_render_texture(target)
pyray.close_window()  # Close window and OpenGL context
