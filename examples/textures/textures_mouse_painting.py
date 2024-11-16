"""

raylib [texture] example - Mouse Painting

"""
from pyray import *

MAX_COLORS_COUNT = 23  # Number of colors available

# Initialization
screenWidth = 800
screenHeight = 450

init_window(screenWidth, screenHeight, "raylib [textures] example - mouse painting")

# Colours to choose from
colors = [RAYWHITE, YELLOW, GOLD, ORANGE, PINK, RED, MAROON, GREEN, LIME, DARKGREEN,
          SKYBLUE, BLUE, DARKBLUE, PURPLE, VIOLET, DARKPURPLE, BEIGE, BROWN, DARKBROWN,
          LIGHTGRAY, GRAY, DARKGRAY, BLACK]

colorsRecs = []

# Define colorsRecs data (for every rectangle)
for i in range(MAX_COLORS_COUNT):
    colorsRecs.append(Rectangle(10 + 30.0 * i + 2 * i, 10, 30, 30))

colorSelected = 0
colorSelectedPrev = colorSelected
colorMouseHover = 0
brushSize = 20.0
mouseWasPressed = False

btnSaveRec = Rectangle(750, 10, 40, 30)
btnSaveMouseHover = False
showSaveMessage = False
saveMessageCounter = 0

# Create a RenderTexture2D to use as a canvas
target = load_render_texture(screenWidth, screenHeight)

# Clear render texture before entering the game loop
begin_texture_mode(target)
clear_background(colors[0])
end_texture_mode()

set_target_fps(120)  # Set our game to run at 120 frames-per-second

# Main game loop
while not window_should_close():  # Detect window close button or ESC key
    # Update
    # ----------------------------------------------------------------------------------
    mousePos = get_mouse_position()

    # Move between colors with keys
    if is_key_pressed(KeyboardKey.KEY_RIGHT):
        colorSelected += 1
    elif is_key_pressed(KeyboardKey.KEY_LEFT):
        colorSelected -= 1

    if colorSelected >= MAX_COLORS_COUNT:
        colorSelected = MAX_COLORS_COUNT - 1
    elif colorSelected < 0:
        colorSelected = 0

    # Choose color with mouse
    for i in range(MAX_COLORS_COUNT):
        if check_collision_point_rec(mousePos, colorsRecs[i]):
            colorMouseHover = i
            break
        else:
            colorMouseHover = -1

    if colorMouseHover >= 0 and is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
        colorSelected = colorMouseHover
        colorSelectedPrev = colorSelected

    # Change brush size
    brushSize += get_mouse_wheel_move() * 5
    if brushSize < 2: brushSize = 2
    if brushSize > 50: brushSize = 50

    if is_key_pressed(KeyboardKey.KEY_C):
        # Clear render texture to clear color
        begin_texture_mode(target)
        clear_background(colors[0])
        end_texture_mode()

    if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT) or get_gesture_detected() == Gesture.GESTURE_DRAG:

        # Paint circle into render texture
        # NOTE: To avoid discontinuous circles, we could store
        # previous-next mouse points and just draw a line using brush size
        begin_texture_mode(target)
        if mousePos.y > 50:
            draw_circle(int(mousePos.x), int(mousePos.y), brushSize, colors[colorSelected])
        end_texture_mode()
    if is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT):

        if not mouseWasPressed:
            colorSelectedPrev = colorSelected
            colorSelected = 0

        mouseWasPressed = True

        # Erase circle from render texture
        begin_texture_mode(target)
        if mousePos.y > 50: draw_circle(int(mousePos.x), int(mousePos.y), brushSize, colors[0])
        end_texture_mode()

    elif is_mouse_button_released(MouseButton.MOUSE_BUTTON_RIGHT) and mouseWasPressed:

        colorSelected = colorSelectedPrev
        mouseWasPressed = False

    # Check mouse hover save button
    if check_collision_point_rec(mousePos, btnSaveRec):
        btnSaveMouseHover = True
    else:
        btnSaveMouseHover = False

    # Image saving logic
    # NOTE: Saving painted texture to a default named image
    if (btnSaveMouseHover and is_mouse_button_released(MouseButton.MOUSE_BUTTON_LEFT)) or is_key_pressed(KeyboardKey.KEY_S):
        image = load_image_from_texture(target.texture)
        image_flip_vertical(image)
        export_image(image, "my_amazing_texture_painting.png")
        unload_image(image)
        showSaveMessage = True

    if showSaveMessage:
        # On saving, show a full screen message for 2 seconds
        saveMessageCounter += 1
        if saveMessageCounter > 240:
            showSaveMessage = False
            saveMessageCounter = 0

    # ----------------------------------------------------------------------------------

    # Draw
    # ----------------------------------------------------------------------------------
    begin_drawing()
    clear_background(RAYWHITE)

    # NOTE: Render texture must be y-flipped due to default OpenGL coordinates (left-bottom)
    draw_texture_rec(target.texture, Rectangle(0, 0, float(target.texture.width), float(-target.texture.height)),
                     Vector2(0, 0), WHITE)

    # Draw drawing circle for reference
    if mousePos.y > 50:
        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT):
            draw_circle_lines(int(mousePos.x), int(mousePos.y), brushSize, GRAY)
        else:
            draw_circle(get_mouse_x(), get_mouse_y(), brushSize, colors[colorSelected])
    # Draw top panel
    draw_rectangle(0, 0, get_screen_width(), 50, RAYWHITE)
    draw_line(0, 50, get_screen_width(), 50, LIGHTGRAY)

    # Draw color selection rectangles
    for i in range(MAX_COLORS_COUNT):
        draw_rectangle_rec(colorsRecs[i], colors[i])
    draw_rectangle_lines(10, 10, 30, 30, LIGHTGRAY)

    if colorMouseHover >= 0: draw_rectangle_rec(colorsRecs[colorMouseHover], fade(WHITE, 0.6))

    draw_rectangle_lines_ex(
        Rectangle(colorsRecs[colorSelected].x - 2, colorsRecs[colorSelected].y - 2, colorsRecs[colorSelected].width + 4,
                  colorsRecs[colorSelected].height + 4), 2, BLACK)

    # Draw save image button
    draw_rectangle_lines_ex(btnSaveRec, 2, RED if btnSaveMouseHover else BLACK)
    draw_text("SAVE!", 755, 20, 10, RED if btnSaveMouseHover else BLACK)

    if showSaveMessage:
        draw_rectangle(0, 0, get_screen_width(), get_screen_height(), fade(RAYWHITE, 0.8))
        draw_rectangle(0, 150, get_screen_width(), 80, BLACK)
        draw_text("IMAGE SAVED:  my_amazing_texture_painting.png", 150, 180, 20, RAYWHITE)

    end_drawing()

    # ----------------------------------------------------------------------------------

# De-Initialization
# ----------------------------------------------------------------------------------
unload_render_texture(target)  # Unload render texture

close_window()  # Close window and OpenGL context
