# Tested with version: 5.5.0.2
# by @Lightnet

from pyray import *


currentFrame = 0
framesCounter = 0
framesSpeed = 8
# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

MAX_FRAME_SPEED = 15
MIN_FRAME_SPEED = 1

init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [texture] example - sprite anim")

#need to set in case of animation snyc
set_target_fps(60)                 # Set our game to run at 60 frames-per-second

scarfy = load_texture("resources/scarfy.png")  # Texture loading

frameRec = Rectangle(0.0, 0.0, scarfy.width/6, scarfy.height)

position = Vector2(350.0, 280.0)

# Main game loop
while not window_should_close():  # Detect window close button or ESC key

    framesCounter += 1

    if framesCounter >= 60/framesSpeed:
        framesCounter = 0
        currentFrame += 1
        if currentFrame > 5:
            currentFrame = 0

        frameRec.x = float(currentFrame) * float(scarfy.width/6)
    # Control speed animation
    if (is_key_pressed(KeyboardKey.KEY_RIGHT)):
        framesSpeed += 1
    elif is_key_pressed(KeyboardKey.KEY_LEFT):
        framesSpeed -= 1

    if framesSpeed > MAX_FRAME_SPEED:
        framesSpeed = MAX_FRAME_SPEED
    elif framesSpeed < MIN_FRAME_SPEED:
        framesSpeed = MIN_FRAME_SPEED

    begin_drawing()

    clear_background(RAYWHITE)
    #draw sheet block
    draw_rectangle_lines(15, 40, scarfy.width, scarfy.height, LIME)
    #draw current frame render
    draw_rectangle_lines(15 + int(frameRec.x), 40 + int(frameRec.y), int(frameRec.width), int(frameRec.height), RED)
    draw_text("FRAME SPEED: ", 165, 210, 10, DARKGRAY)
    draw_text(f" FPS {framesSpeed}", 575, 210, 10, DARKGRAY) #format string
    draw_text("PRESS RIGHT/LEFT KEYS to CHANGE SPEED!", 290, 240, 10, DARKGRAY)
    #display bar framesSpeed cap
    for i in range(MAX_FRAME_SPEED):
        if i < framesSpeed:
            draw_rectangle(250 + 21*i, 205, 20, 20, RED)
        draw_rectangle_lines(250 + 21*i, 205, 20, 20, MAROON)
    #draw sprite sheet texture
    draw_texture(scarfy, 15, 40, WHITE)
    #draw sprite animation
    draw_texture_rec(scarfy, frameRec, position,WHITE)

    draw_text("(c) Scarfy sprite by Eiden Marsal", SCREEN_WIDTH - 200, SCREEN_HEIGHT - 20, 10, GRAY)

    end_drawing()

# De-Initialization
unload_texture(scarfy)

close_window()  # Close window and OpenGL context
