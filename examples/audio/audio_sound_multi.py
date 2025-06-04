"""checked with raylib-python-cffi 5.5.0.2
raylib [audio] example - Playing sound multiple times
Example complexity rating: [★★☆☆] 2/4
Example originally created with raylib 4.6, last time updated with raylib 4.6
Example contributed by Jeffery Myers (@JeffM2501) and reviewed by Ramon Santamaria (@raysan5)
Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
BSD-like license that allows static linking with closed source software
Copyright (c) 2023-2025 Jeffery Myers (@JeffM2501)

This source has been converted from C raylib examples to Python.
"""

from typing import List

import pyray as rl
from pathlib import Path

# Get the directory where this script is located
THIS_DIR = Path(__file__).resolve().parent

MAX_SOUNDS = 10
sound_array: List[rl.Sound] = []
current_sound = 0

# Initialization
# --------------------------------------------------------------------------------------
screen_width = 800
screen_height = 450

rl.init_window(
    screen_width, screen_height, "raylib [audio] example - playing sound multiple times"
)

rl.init_audio_device()  # Initialize audio device

# Load the sound list
sound_array.append(
    rl.load_sound(str(THIS_DIR / "resources/sound.wav"))
)  # Load WAV audio file into the first slot as the 'source' sound
# this sound owns the sample data
for i in range(1, MAX_SOUNDS):
    sound_array.append(
        rl.load_sound_alias(sound_array[0])
    )  # Load an alias of the sound into slots 1-9
    # These do not own the sound data, but can be played
current_sound = 0  # Set the sound list to the start

rl.set_target_fps(60)  # Set our game to run at 60 frames-per-second
# --------------------------------------------------------------------------------------

# Main game loop
while not rl.window_should_close():  # Detect window close button or ESC key
    # Update
    # ----------------------------------------------------------------------------------
    if rl.is_key_pressed(rl.KeyboardKey.KEY_SPACE):
        rl.play_sound(sound_array[current_sound])  # Play the next open sound slot
        current_sound += 1  # Increment the sound slot
        if (
            current_sound >= MAX_SOUNDS
        ):  # If the sound slot is out of bounds, go back to 0
            current_sound = 0

        # Note: a better way would be to look at the list for the first sound that is not playing and use that slot
    # ----------------------------------------------------------------------------------

    # Draw
    # ----------------------------------------------------------------------------------
    rl.begin_drawing()

    rl.clear_background(rl.RAYWHITE)

    rl.draw_text("Press SPACE to PLAY a WAV sound!", 200, 180, 20, rl.LIGHTGRAY)

    rl.end_drawing()
    # ----------------------------------------------------------------------------------

# De-Initialization
# --------------------------------------------------------------------------------------
for i in range(1, MAX_SOUNDS):
    rl.unload_sound_alias(sound_array[i])  # Unload sound aliases
rl.unload_sound(sound_array[0])  # Unload source sound data

rl.close_audio_device()  # Close audio device

rl.close_window()  # Close window and OpenGL context
# --------------------------------------------------------------------------------------
