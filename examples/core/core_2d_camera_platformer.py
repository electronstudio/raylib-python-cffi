"""

raylib [core] example - 2d camera platformer

"""
from math import sqrt

from raylib.pyray import PyRay
from raylib.colors import (
    DARKGRAY,
    RED,
    BLACK,
    GRAY,
    LIGHTGRAY,
)


pyray = PyRay()

# Initialization
global g_evening_out, g_even_out_target
g_evening_out = False

G = 400
PLAYER_JUMP_SPD = 350.0
PLAYER_HOR_SPD = 200.0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                  'raylib [core] example - 2d camera')


# Raylib Math
def vector2_subtract(v1, v2):
    return pyray.Vector2(v1.x - v2.x, v1.y - v2.y)


def vector2_add(v1, v2):
    return pyray.Vector2(v1.x + v2.x, v1.y + v2.y)


def vector2_length(v):
    return sqrt((v.x * v.x) + (v.y * v.y))


def vector2_scale(v, scale):
    return pyray.Vector2(v.x * scale, v.y * scale)


class Player:

    def __init__(self, position, speed, can_jump):
        self.position = position
        self.speed = speed
        self.can_jump = can_jump


class EnvItem:

    def __init__(self, rect, blocking, color):
        self.rect = rect
        self.blocking = blocking
        self.color = color


def update_player(player, env_items, delta):
    if pyray.is_key_down(pyray.KEY_LEFT):
        player.position.x -= PLAYER_HOR_SPD * delta
    if pyray.is_key_down(pyray.KEY_RIGHT):
        player.position.x += PLAYER_HOR_SPD * delta
    if pyray.is_key_down(pyray.KEY_SPACE) and player.can_jump:
        player.speed = -PLAYER_JUMP_SPD
        player.can_jump = False

    hit_obstacle = False
    for ei in env_items:
        p = player.position
        if (
            ei.blocking and
            ei.rect.x <= p.x and
            ei.rect.x + ei.rect.width >= p.x and
            ei.rect.y >= p.y and
            ei.rect.y < p.y + player.speed * delta
        ):
            hit_obstacle = True
            player.speed = 0.0
            p.y = ei.rect.y

    if not hit_obstacle:
        player.position.y += player.speed * delta
        player.speed += G * delta
        player.can_jump = False
    else:
        player.can_jump = True


def update_camera_center(
    camera, player, env_items, delta, width, height
):
    camera.offset = pyray.Vector2(width / 2, height / 2)
    camera.target = player.position


def update_camera_center_inside_map(
    camera, player, env_items, delta, width, height
):
    camera.target = player.position
    camera.offset = pyray.Vector2(width / 2, height / 2)

    minX = 1000
    minY = 1000
    maxX = -1000
    maxY = -1000

    for ei in env_items:
        minX = min(ei.rect.x, minX)
        maxX = max(ei.rect.x + ei.rect.width, maxX)

        minY = min(ei.rect.y, minY)
        maxY = max(ei.rect.y + ei.rect.height, maxY)

    wmax = pyray.get_world_to_screen_2d(pyray.Vector2(maxX, maxY), camera)
    wmin = pyray.get_world_to_screen_2d(pyray.Vector2(minX, minY), camera)

    if wmax.x < width:
        camera.offset.x = width - (wmax.x - width / 2)
    if wmax.y < height:
        camera.offset.y = height - (wmax.y - height / 2)
    if wmin.x > 0:
        camera.offset.x = width / 2 - wmin.x
    if wmin.y > 0:
        camera.offset.y = height / 2 - wmin.y


def update_camera_center_smooth_follow(
    camera, player, env_items, delta, width, height
):
    min_speed = 30
    min_effect_length = 10
    fraction_speed = 0.8

    camera.offset = pyray.Vector2(width / 2, height / 2)
    diff = vector2_subtract(player.position, camera.target)
    length = vector2_length(diff)

    if length > min_effect_length:
        speed = max(fraction_speed * length, min_speed)
        camera.target = vector2_add(
            camera.target, vector2_scale(diff, speed * delta / length)
        )


def update_camera_even_out_on_landing(
    camera, player, env_items, delta, width, height
):
    global g_evening_out, g_even_out_target

    even_out_speed = 700

    camera.offset = pyray.Vector2(width / 2, height / 2)
    camera.target.x = player.position.x

    if g_evening_out:
        if g_even_out_target > camera.target.y:
            camera.target.y += even_out_speed * delta

            if camera.target.y > g_even_out_target:
                camera.target.y = g_even_out_target
                g_evening_out = False
        else:
            camera.target.y -= even_out_speed * delta
            if camera.target.y < g_even_out_target:
                camera.target.y = g_even_out_target
                g_evening_out = False
    else:
        if (
            player.can_jump and
            (player.speed == 0) and
            (player.position.y != camera.target.y)
        ):
            g_evening_out = True
            g_even_out_target = player.position.y


def update_camera_player_bounds_push(
    camera, player, env_items, delta, width, height
):
    bbox = pyray.Vector2(0.2, 0.2)

    bbox_world_min = pyray.get_world_to_screen_2d(
        pyray.Vector2((1 - bbox.x) * 0.5 * width,
                      (1 - bbox.y) * 0.5 * height),
        camera
    )
    bbox_world_max = pyray.get_world_to_screen_2d(
        pyray.Vector2((1 + bbox.x) * 0.5 * width,
                      (1 + bbox.y) * 0.5 * height),
        camera
    )
    camera.offset = pyray.Vector2((1 - bbox.x) * 0.5 * width,
                                  (1 - bbox.y) * 0.5 * height)

    if player.position.x < bbox_world_min.x:
        camera.target.x = player.position.x
    if player.position.y < bbox_world_min.y:
        camera.target.y = player.position.y
    if player.position.x > bbox_world_max.x:
        camera.target.x = (
            bbox_world_min.x + (player.position.x - bbox_world_max.x)
        )
    if player.position.y > bbox_world_max.y:
        camera.target.y = (
            bbox_world_min.y + (player.position.y - bbox_world_max.y)
        )


# Main intialization
player = Player(pyray.Vector2(400, 280), 0, False)
env_items = (
    EnvItem(pyray.Rectangle(0, 0, 1000, 400), 0, LIGHTGRAY),
    EnvItem(pyray.Rectangle(0, 400, 1000, 200), 1, GRAY),
    EnvItem(pyray.Rectangle(300, 200, 400, 10), 1, GRAY),
    EnvItem(pyray.Rectangle(250, 300, 100, 10), 1, GRAY),
    EnvItem(pyray.Rectangle(650, 300, 100, 10), 1, GRAY),
)

camera = pyray.Camera2D()
camera.target = player.position
camera.offset = pyray.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
camera.rotation = 0.0
camera.zoom = 1.0

pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second

# Store pointers to the multiple update camera functions
camera_updaters = (
    update_camera_center,
    update_camera_center_inside_map,
    update_camera_center_smooth_follow,
    update_camera_even_out_on_landing,
    update_camera_player_bounds_push,
)
camera_option = 0
camera_updaters_length = len(camera_updaters)

camera_descriptions = (
    'Follow player center',
    'Follow player center, but clamp to map edges',
    'Follow player center smoothed',
    ('Follow player center horizontally '
     'update player center vertically after landing'),
    'Player push camera on getting too close to screen edge',
)

# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    delta_time = pyray.get_frame_time()

    update_player(player, env_items, delta_time)

    camera.zoom += pyray.get_mouse_wheel_move() * 0.05

    if camera.zoom > 3.0:
        camera.zoom = 3.0
    elif camera.zoom < 0.25:
        camera.zoom = 0.25

    if pyray.is_key_pressed(pyray.KEY_R):
        camera.zoom = 1.0
        player.position = pyray.Vector2(400, 280)

    if pyray.is_key_pressed(pyray.KEY_C):
        camera_option = (camera_option + 1) % camera_updaters_length

    # Call update camera function by its pointer
    camera_updaters[camera_option](
        camera, player, env_items, delta_time,
        SCREEN_WIDTH, SCREEN_HEIGHT
    )

    # Draw
    pyray.begin_drawing()
    pyray.clear_background(LIGHTGRAY)

    pyray.begin_mode_2d(camera)

    for env_item in env_items:
        pyray.draw_rectangle_rec(env_item.rect, env_item.color)

    player_rect = pyray.Rectangle(
        int(player.position.x) - 20,
        int(player.position.y) - 40,
        40, 40
    )
    pyray.draw_rectangle_rec(player_rect, RED)

    pyray.end_mode_2d()

    pyray.draw_text('Controls:', 20, 20, 10, BLACK)
    pyray.draw_text('- Right/Left to move', 40, 40, 10, DARKGRAY)
    pyray.draw_text('- Space to jump', 40, 60, 10, DARKGRAY)
    pyray.draw_text('- Mouse Wheel to Zoom in-out, R to reset zoom',
                    40, 80, 10, DARKGRAY)
    pyray.draw_text('- C to change camera mode', 40, 100, 10, DARKGRAY)
    pyray.draw_text('Current camera mode:', 20, 120, 10, BLACK)
    pyray.draw_text(camera_descriptions[camera_option], 40, 140, 10, DARKGRAY)

    pyray.end_drawing()

# De-Initialization
pyray.close_window()  # Close window and OpenGL context
