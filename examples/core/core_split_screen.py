"""

raylib [core] example - Split Screen

"""

from pyray import *

cameraPlayer1 = Camera3D([0])
cameraPlayer2 = Camera3D([0])

def draw_scene():
    count = 5
    spacing = 4

    # Grid of cube trees on a plane to make a "world"

    draw_plane(Vector3(0, 0, 0), Vector2(50, 50), BEIGE)

    for x in range(-count*spacing, count*spacing, spacing):
        for z in range(-count*spacing, count*spacing, spacing):
            draw_cube(Vector3(x, 1.5, z), 1, 1, 1, LIME)
            draw_cube(Vector3(x, 0.5, z), 0.25, 1, 0.25, BROWN)

    # Draw a cube at each player's position
    draw_cube(cameraPlayer1.position, 1, 1, 1, RED)
    draw_cube(cameraPlayer2.position, 1, 1, 1, BLUE)

# Initialization

screenWidth = 800
screenHeight = 450

init_window(screenWidth, screenHeight, "raylib [core] example - split screen")

# Setup player 1 camera and screen

cameraPlayer1.fovy = 45.0
cameraPlayer1.up = Vector3(0,1.0,0) 
cameraPlayer1.target = Vector3(0,1.0,0)
cameraPlayer1.position = Vector3(0,1,-3)

screenPlayer1 = load_render_texture(int(screenWidth/2), int(screenHeight))

# Setup player 2 camera and screen
cameraPlayer2.fovy = 45.0
cameraPlayer2.up = Vector3(0,1.0,0)
cameraPlayer2.target = Vector3(0,3.0,0)
cameraPlayer2.position = Vector3(-3,3,0)

screenPlayer2 = load_render_texture(int(screenWidth / 2), int(screenHeight))

# Build a flipped rectangle the size of the split view to use for drawing later
splitScreenRect = Rectangle(0.0, 0.0, screenPlayer1.texture.width, -screenPlayer1.texture.height)

set_target_fps(60)              # Set our game to run at 60 frames-per-second

# Main game loop
while not window_should_close(): # Detect window close button or ESC key

    ''' Update
     If anyone moves this frame, how far will they move based on the time since the last frame
     this moves thigns at 10 world units per second, regardless of the actual FPS'''

    offsetThisFrame = 10.0 * get_frame_time()

    # Move Player1 forward and backwards (no turning)

    if is_key_down(KeyboardKey.KEY_W):
        cameraPlayer1.position.z += offsetThisFrame
        cameraPlayer1.target.z += offsetThisFrame
    
    elif is_key_down(KeyboardKey.KEY_S):
    
        cameraPlayer1.position.z -= offsetThisFrame
        cameraPlayer1.target.z -= offsetThisFrame

    # Move Player2 forward and backwards (no turning)
    if is_key_down(KeyboardKey.KEY_UP):
        cameraPlayer2.position.x += offsetThisFrame
        cameraPlayer2.target.x += offsetThisFrame
    
    elif is_key_down(KeyboardKey.KEY_DOWN):
        cameraPlayer2.position
        cameraPlayer2.position.x -= offsetThisFrame
        cameraPlayer2.target.x -= offsetThisFrame
    
    # Draw Player1 view to the render texture
    begin_texture_mode(screenPlayer1)
    clear_background(SKYBLUE)
    begin_mode_3d(cameraPlayer1)
    draw_scene()
    end_mode_3d()
    draw_text("PLAYER1 W/S to move", 10, 10, 20, RED)
    end_texture_mode()

    # Draw Player2 view to the render texture

    begin_texture_mode(screenPlayer2)
    clear_background(SKYBLUE)
    begin_mode_3d(cameraPlayer2)
    draw_scene()
    end_mode_3d()
    draw_text("PLAYER2 UP/DOWN to move", 10, 10, 20, BLUE)
    end_texture_mode()

    # Draw both views render textures to the screen side by side
    begin_drawing()
    clear_background(BLACK)
    draw_texture_rec(screenPlayer1.texture, splitScreenRect, Vector2(0,0), WHITE)
    draw_texture_rec(screenPlayer2.texture, splitScreenRect, Vector2(screenWidth/2.0, 0 ), WHITE)
    end_drawing()


# De-Initialization
unload_render_texture(screenPlayer1) # Unload render texture
unload_render_texture(screenPlayer2) # Unload render texture

close_window()




