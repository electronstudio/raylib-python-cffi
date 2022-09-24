"""

raylib [core] example - 2D Camera Platformer

"""

# Import
# ------------------------------------------------------------------------------------
from pyray import *

# ------------------------------------------------------------------------------------

# Definitions
# ------------------------------------------------------------------------------------
G = 400
PLAYER_JUMP_SPD = 350.0
PLAYER_HOR_SPD = 200.0

class Player:
    def __init__(self, position, speed, canJump):
        self.position = position
        self.speed = speed
        self.canJump = canJump


class EnvItem:
    def __init__(self, rect, blocking, color):
        self.rect = rect
        self.blocking = blocking
        self.color = color

def update_player(player, env_items, delta):
    if is_key_down(KeyboardKey.KEY_LEFT):
        player.position.x -= PLAYER_HOR_SPD * delta
    if is_key_down(KeyboardKey.KEY_RIGHT):
        player.position.x += PLAYER_HOR_SPD * delta
    if is_key_down(KeyboardKey.KEY_SPACE) and player.canJump:
        player.speed = -PLAYER_JUMP_SPD
        player.canJump = False

    hit_obstacle = False
    for ei in env_items:
        p = player.position
        if ei.blocking and ei.rect.x <= p.x <= ei.rect.x + ei.rect.width and p.y <= ei.rect.y < p.y + player.speed * delta:
            hit_obstacle = True
            player.speed = 0.0
            p.y = ei.rect.y

    if not hit_obstacle:
        player.position.y += player.speed * delta
        player.speed += G * delta
        player.canJump = False
    else:
        player.canJump = True

def update_camera_center(camera, player, env_items, delta, width, height):
    camera.offset = Vector2(width / 2, height / 2)
    camera.target = player.position
def update_camera_center_inside_map(camera, player, env_items, delta, width, height):
    camera.target = player.position
    camera.offset = Vector2(width / 2, height / 2)

    minX = 1000
    minY = 1000
    maxX = -1000
    maxY = -1000

    for ei in env_items:
        minX = min(ei.rect.x, minX)
        maxX = max(ei.rect.x + ei.rect.width, maxX)

        minY = min(ei.rect.y, minY)
        maxY = max(ei.rect.y + ei.rect.height, maxY)

    wmax = get_world_to_screen_2d(Vector2(maxX, maxY), camera)
    wmin = get_world_to_screen_2d(Vector2(minX, minY), camera)

    if wmax.x < width:
        camera.offset.x = width - (wmax.x - width / 2)
    if wmax.y < height:
        camera.offset.y = height - (wmax.y - height / 2)
    if wmin.x > 0:
        camera.offset.x = width / 2 - wmin.x
    if wmin.y > 0:
        camera.offset.y = height / 2 - wmin.y

def update_camera_center_smooth_follow(camera, player, env_items, delta, width, height):
    minSpeed = 30
    minEffectLength = 10
    fraction_speed = 0.8

    camera.offset = Vector2(width / 2, height / 2)
    diff = vector2_subtract(player.position, camera.target)
    length = vector2_length(diff)

    if length > minEffectLength:
        speed = max(fraction_speed * length, minSpeed)
        camera.target = vector2_add(camera.target, vector2_scale(diff, speed * delta / length))

def update_camera_even_out_on_landing(camera, player, env_items, delta, width, height):
    evenOutSpeed = 700.0
    eveningOut = False
    evenOutTarget = 0.0

    camera.offset = Vector2(width / 2, height / 2)
    camera.target.x = player.position.x

    if eveningOut:
        if evenOutTarget > camera.target.y:
            camera.target.y += evenOutSpeed * delta

            if camera.target.y > evenOutTarget:
                camera.target.y = evenOutTarget
                eveningOut = False
        else:
            camera.target.y -= evenOutSpeed * delta
            if camera.target.y < evenOutTarget:
                camera.target.y = evenOutTarget
                eveningOut = False
    else:
        if (player.can_jump and player.speed == 0) and (player.position.y != camera.target.y):
            eveningOut = True
            evenOutTarget = player.position.y

def update_camera_player_bounds_push(camera, player, env_items, delta, width, height):
    bbox = Vector2(0.2, 0.2)

    bboxWorldMin = get_world_to_screen_2d(Vector2((1 - bbox.x) * 0.5 * width, (1 - bbox.y) * 0.5 * height), camera)
    bbox_world_max = get_world_to_screen_2d(Vector2((1 + bbox.x) * 0.5 * width,(1 + bbox.y) * 0.5 * height), camera)
    camera.offset = Vector2((1 - bbox.x) * 0.5 * width, (1 - bbox.y) * 0.5 * height)

    if player.position.x < bboxWorldMin.x:
        camera.target.x = player.position.x
    if player.position.y < bboxWorldMin.y:
        camera.target.y = player.position.y
    if player.position.x > bbox_world_max.x:
        camera.target.x = bboxWorldMin.x + (player.position.x - bbox_world_max.x) 
    if player.position.y > bbox_world_max.y:
        camera.target.y = bboxWorldMin.y + (player.position.y - bbox_world_max.y)
# ------------------------------------------------------------------------------------

def main():
    # Initialization
    # ----------------------------------------------------------------------------------
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [core] example - 2d camera")

    player = Player(Vector2(400, 280), 0, False)
    envItems = (
        EnvItem(Rectangle(0, 0, 1000, 400), 0, LIGHTGRAY),
        EnvItem(Rectangle(0, 400, 1000, 200), 1, GRAY),
        EnvItem(Rectangle(300, 200, 400, 10), 1, GRAY),
        EnvItem(Rectangle(250, 300, 100, 10), 1, GRAY),
        EnvItem(Rectangle(650, 300, 100, 10), 1, GRAY),
    )

    camera = Camera2D()
    camera.target = player.position
    camera.offset = Vector2(screenWidth / 2, screenHeight / 2)
    camera.rotation = 0.0
    camera.zoom = 1.0

    # Store pointers to the multiple update camera functions
    cameraUpdaters = (
        update_camera_center,
        update_camera_center_inside_map,
        update_camera_center_smooth_follow,
        update_camera_even_out_on_landing,
        update_camera_player_bounds_push,
    )
    cameraOption = 0
    cameraUpdatersLength = len(cameraUpdaters)

    cameraDescriptions = (
        "Follow player center",
        "Follow player center, but clamp to map edges",
        "Follow player center smoothed",
        ("Follow player center horizontally "
         "update player center vertically after landing"),
        "Player push camera on getting too close to screen edge",
    )

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ----------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        delta_time = get_frame_time()

        update_player(player, envItems, delta_time)

        camera.zoom += get_mouse_wheel_move() * 0.05

        if camera.zoom > 3.0:
            camera.zoom = 3.0
        elif camera.zoom < 0.25:
            camera.zoom = 0.25

        if is_key_pressed(KeyboardKey.KEY_R):
            camera.zoom = 1.0
            player.position = Vector2(400, 280)

        if is_key_pressed(KeyboardKey.KEY_C):
            cameraOption = (cameraOption + 1) % cameraUpdatersLength

        # Call update camera function by its pointer
        cameraUpdaters[cameraOption](camera, player, envItems, delta_time, screenWidth, screenHeight)
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()
        clear_background(LIGHTGRAY)

        begin_mode_2d(camera)

        for envItem in envItems:
            draw_rectangle_rec(envItem.rect, envItem.color)

        player_rect = Rectangle(player.position.x - 20, player.position.y - 40, 40, 40)
        draw_rectangle_rec(player_rect, RED)

        end_mode_2d()

        draw_text("Controls:", 20, 20, 10, BLACK)
        draw_text("- Right/Left to move", 40, 40, 10, DARKGRAY)
        draw_text("- Space to jump", 40, 60, 10, DARKGRAY)
        draw_text("- Mouse Wheel to Zoom in-out, R to reset zoom", 40, 80, 10, DARKGRAY)
        draw_text("- C to change camera mode", 40, 100, 10, DARKGRAY)
        draw_text("Current camera mode:", 20, 120, 10, BLACK)
        draw_text(cameraDescriptions[cameraOption], 40, 140, 10, DARKGRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
