"""

raylib [textures] example - Bunnymark

"""

# Import
# ------------------------------------------------------------------------------------
from pyray import *
# ------------------------------------------------------------------------------------

# Definitions
# ------------------------------------------------------------------------------------
MAX_BUNNIES = 50000
# This is the maximum amount of elements (quads) per batch
# NOTE: This value is defined in [rlgl] module and can be changed there
MAX_BATCH_ELEMENTS = 8192

class Bunny:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.speed = Vector2(0, 0)
        self.color = Color(0, 0, 0, 255)
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ----------------------------------------------------------------------------------
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 450

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [textures] example - bunnymark")

    # Load bunny texture
    tex_bunny = load_texture("resources/wabbit_alpha.png")

    bunnies = []
    for i in range(0, MAX_BUNNIES):
        bunnies.append(Bunny())

    bunnies_count = 0  # Bunnies counter

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ----------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT):
            # Create more bunnies
            for i in range(0, 100):
                if bunnies_count < MAX_BUNNIES:
                    bunnies[bunnies_count].position = get_mouse_position()
                    bunnies[bunnies_count].speed.x = get_random_value(-250, 250) / 60.0
                    bunnies[bunnies_count].speed.y = get_random_value(-250, 250) / 60.0
                    bunnies[bunnies_count].color = Color(get_random_value(50, 240), get_random_value(80, 240), get_random_value(100, 240), 255)
                    bunnies_count += 1

        # Update bunnies
        for i in range(0, bunnies_count):
            bunnies[i].position.x += bunnies[i].speed.x
            bunnies[i].position.y += bunnies[i].speed.y

            if bunnies[i].position.x + tex_bunny.width / 2 > SCREEN_WIDTH or bunnies[i].position.x + tex_bunny.width / 2 < 0:
                bunnies[i].speed.x *= -1
            if bunnies[i].position.y + tex_bunny.height / 2 > SCREEN_HEIGHT or bunnies[i].position.y + tex_bunny.height / 2 - 40 < 0:
                bunnies[i].speed.y *= -1
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        for i in range(0, bunnies_count):
            # NOTE: When internal batch buffer limit is reached (MAX_BATCH_ELEMENTS),
            # a draw call is launched and buffer starts being filled again;
            # before issuing a draw call, updated vertex data from internal CPU buffer is send to GPU...
            # Process of sending data is costly, and it could happen that GPU data has not been completely
            # processed for drawing while new data is tried to be sent (updating current in-use buffers)
            # it could generate a stall and consequently a frame drop, limiting the number of drawn bunnies
            # draw_texture(tex_bunny, int(bunnies[i].position.x), int(bunnies[i].position.y), bunnies[i].color)
            draw_texture_v(tex_bunny, bunnies[i].position, bunnies[i].color)  # more efficient drawing

        draw_rectangle(0, 0, SCREEN_WIDTH, 40, BLACK)
        text = f"bunnies {bunnies_count}"
        draw_text(text.encode('utf-8'), 120, 10, 20, GREEN)
        text = f"batched draw calls: {1 + int(bunnies_count / MAX_BATCH_ELEMENTS)}"
        draw_text(text.encode('utf-8'), 320, 10, 20, MAROON)

        draw_fps(10, 10)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    unload_texture(tex_bunny)  # Unload bunny texture

    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
