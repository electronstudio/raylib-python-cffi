from pyray import *
import pyray

# Initialization
# ---------------------------------------------------------
screen_width = 800
screen_height = 450

init_window(screen_width, screen_height, b"raylib [core] example - window flags")

ball_position = Vector2(get_screen_width() / 2.0, get_screen_height() / 2.0)
ball_speed = Vector2(5.0, 4.0)
ball_radius = 20.0

frames_counter = 0

# Main game loop
while not window_should_close():  # Detect window close button or ESC key
    # Update
    # -----------------------------------------------------
    if is_key_pressed(pyray.KEY_F):
        toggle_fullscreen()

    if is_key_pressed(pyray.KEY_R):
        if is_window_state(pyray.FLAG_WINDOW_RESIZABLE):
            clear_window_state(pyray.FLAG_WINDOW_RESIZABLE)
        else:
            set_window_state(pyray.FLAG_WINDOW_RESIZABLE)

    if is_key_pressed(pyray.KEY_D):
        if is_window_state(pyray.FLAG_WINDOW_UNDECORATED):
            clear_window_state(pyray.FLAG_WINDOW_UNDECORATED)
        else:
            set_window_state(pyray.FLAG_WINDOW_UNDECORATED)

    if is_key_pressed(pyray.KEY_H):
        if not is_window_state(pyray.FLAG_WINDOW_HIDDEN):
            set_window_state(pyray.FLAG_WINDOW_HIDDEN)
            frames_counter = 0

    if is_window_state(pyray.FLAG_WINDOW_HIDDEN):
        frames_counter += 1
        if frames_counter >= 240:
            clear_window_state(pyray.FLAG_WINDOW_HIDDEN)  # Show window after 3 seconds

    if is_key_pressed(pyray.KEY_N):
        if not is_window_state(pyray.FLAG_WINDOW_MINIMIZED):
            minimize_window()
            frames_counter = 0

    if is_window_state(pyray.FLAG_WINDOW_MINIMIZED):
        frames_counter += 1
        if frames_counter >= 240:
            restore_window()  # Restore window after 3 seconds

    if is_key_pressed(pyray.KEY_M):
        if is_window_state(pyray.FLAG_WINDOW_RESIZABLE):
            if is_window_state(pyray.FLAG_WINDOW_MAXIMIZED):
                restore_window()
            else:
                maximize_window()

    if is_key_pressed(pyray.KEY_U):
        if is_window_state(pyray.FLAG_WINDOW_UNFOCUSED):
            clear_window_state(pyray.FLAG_WINDOW_UNFOCUSED)
        else:
            set_window_state(pyray.FLAG_WINDOW_UNFOCUSED)

    if is_key_pressed(pyray.KEY_T):
        if is_window_state(pyray.FLAG_WINDOW_TOPMOST):
            clear_window_state(pyray.FLAG_WINDOW_TOPMOST)
        else:
            set_window_state(pyray.FLAG_WINDOW_TOPMOST)

    if is_key_pressed(pyray.KEY_A):
        if is_window_state(pyray.FLAG_WINDOW_ALWAYS_RUN):
            clear_window_state(pyray.FLAG_WINDOW_ALWAYS_RUN)
        else:
            set_window_state(pyray.FLAG_WINDOW_ALWAYS_RUN)

    if is_key_pressed(pyray.KEY_V):
        if is_window_state(pyray.FLAG_VSYNC_HINT):
            clear_window_state(pyray.FLAG_VSYNC_HINT)
        else:
            set_window_state(pyray.FLAG_VSYNC_HINT)

    # Bouncing ball logic
    ball_position.x += ball_speed.x
    ball_position.y += ball_speed.y
    if ball_position.x >= (get_screen_width() - ball_radius) or ball_position.x <= ball_radius:
        ball_speed.x *= -1.0
    if ball_position.y >= (get_screen_height() - ball_radius) or ball_position.y <= ball_radius:
        ball_speed.y *= -1.0

    # Draw
    # -----------------------------------------------------
    begin_drawing()

    if is_window_state(pyray.FLAG_WINDOW_TRANSPARENT):
        clear_background(BLANK)
    else:
        clear_background(RAYWHITE)

    draw_circle_v(ball_position, ball_radius, MAROON)
    draw_rectangle_lines_ex(Rectangle(0, 0, get_screen_width(), get_screen_height()), 4, RAYWHITE)

    draw_circle_v(get_mouse_position(), 10, DARKBLUE)

    draw_fps(10, 10)

    draw_text(f"Screen Size: [{get_screen_width()}, {get_screen_height()}]", 10, 40, 10, GREEN)

    # Draw window state info
    draw_text("Following flags can be set after window creation:", 10, 60, 10, GRAY)
    flag_texts = [
        ("FLAG_FULLSCREEN_MODE", pyray.FLAG_FULLSCREEN_MODE),
        ("FLAG_WINDOW_RESIZABLE", pyray.FLAG_WINDOW_RESIZABLE),
        ("FLAG_WINDOW_UNDECORATED", pyray.FLAG_WINDOW_UNDECORATED),
        ("FLAG_WINDOW_HIDDEN", pyray.FLAG_WINDOW_HIDDEN),
        ("FLAG_WINDOW_MINIMIZED", pyray.FLAG_WINDOW_MINIMIZED),
        ("FLAG_WINDOW_MAXIMIZED", pyray.FLAG_WINDOW_MAXIMIZED),
        ("FLAG_WINDOW_UNFOCUSED", pyray.FLAG_WINDOW_UNFOCUSED),
        ("FLAG_WINDOW_TOPMOST", pyray.FLAG_WINDOW_TOPMOST),
        ("FLAG_WINDOW_ALWAYS_RUN", pyray.FLAG_WINDOW_ALWAYS_RUN),
        ("FLAG_VSYNC_HINT", pyray.FLAG_VSYNC_HINT),
    ]
    y_offset = 80
    for text, flag in flag_texts:
        if is_window_state(flag):
            draw_text(f"[{text[5:]}] {text}: on", 10, y_offset, 10, LIME)
        else:
            draw_text(f"[{text[5:]}] {text}: off", 10, y_offset, 10, MAROON)
        y_offset += 20

    draw_text("Following flags can only be set before window creation:", 10, 300, 10, GRAY)
    if is_window_state(pyray.FLAG_WINDOW_HIGHDPI):
        draw_text("FLAG_WINDOW_HIGHDPI: on", 10, 320, 10, LIME)
    else:
        draw_text("FLAG_WINDOW_HIGHDPI: off", 10, 320, 10, MAROON)
    if is_window_state(pyray.FLAG_WINDOW_TRANSPARENT):
        draw_text("FLAG_WINDOW_TRANSPARENT: on", 10, 340, 10, LIME)
    else:
        draw_text("FLAG_WINDOW_TRANSPARENT: off", 10, 340, 10, MAROON)
    if is_window_state(pyray.FLAG_MSAA_4X_HINT):
        draw_text("FLAG_MSAA_4X_HINT: on", 10, 360, 10, LIME)
    else:
        draw_text("FLAG_MSAA_4X_HINT: off", 10, 360, 10, MAROON)

    end_drawing()
    # -----------------------------------------------------

# De-Initialization
# ---------------------------------------------------------
close_window()  # Close window and OpenGL context
# ---------------------------------------------------------

