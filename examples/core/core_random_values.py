"""

raylib [core] example - random values

"""
from pyray import *
from raylib.colors import (
    RAYWHITE,
    MAROON,
    LIGHTGRAY
)

# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

init_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'raylib [core] example - random values')

# set_random_seed()   // Set a custom random seed if desired, by default: "time(NULL)"

randValue = get_random_value(-8, 5)  # Get a random integer number between -8 and 5 (both included)

framesCounter = 0  # Variable used to count frames

set_target_fps(60)  # Set our game to run at 60 frames-per-second

# Main game loop
while not window_should_close():  # Detect window close button or ESC key

    # Update
    #  ----------------------------------------------------------------------------------
    framesCounter += 1

    # Every two seconds (120 frames) a new random value is generated
    if ((framesCounter/120)%2) == 1:
        randValue = get_random_value(-8, 5)
        framesCounter = 0

    #  ----------------------------------------------------------------------------------

    # Draw
    #  ----------------------------------------------------------------------------------
    begin_drawing()

    clear_background(RAYWHITE)

    draw_text("Every 2 seconds a new random value is generated:", 130, 100, 20, MAROON)

    draw_text(str(randValue), 360, 180, 80, LIGHTGRAY)

    end_drawing()

# De-Initialization
close_window()  # Close window and OpenGL context
