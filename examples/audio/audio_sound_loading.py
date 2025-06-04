"""checked with raylib-python-cffi 5.5.0.2
raylib [audio] example - Sound loading and playing
Example complexity rating: [★☆☆☆] 1/4
Example originally created with raylib 1.1, last time updated with raylib 3.5
Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
BSD-like license that allows static linking with closed source software
Copyright (c) 2014-2025 Ramon Santamaria (@raysan5)

This source has been converted from C raylib examples to Python.
"""

import pyray as rl
from pathlib import Path

# Get the directory where this script is located
THIS_DIR = Path(__file__).resolve().parent

# Initialization
# --------------------------------------------------------------------------------------
screen_width = 800
screen_height = 450

rl.init_window(
    screen_width, screen_height, "raylib [audio] example - sound loading and playing"
)

rl.init_audio_device()  # Initialize audio device

# Load WAV audio file using proper path resolution
fx_wav = rl.load_sound(str(THIS_DIR / "resources/sound.wav"))
# Load OGG audio file using proper path resolution
fx_ogg = rl.load_sound(str(THIS_DIR / "resources/target.ogg"))

rl.set_target_fps(60)  # Set our game to run at 60 frames-per-second
# --------------------------------------------------------------------------------------

# Main game loop
while not rl.window_should_close():  # Detect window close button or ESC key
    # Update
    # ----------------------------------------------------------------------------------
    if rl.is_key_pressed(rl.KeyboardKey.KEY_SPACE):
        rl.play_sound(fx_wav)  # Play WAV sound
    if rl.is_key_pressed(rl.KeyboardKey.KEY_ENTER):
        rl.play_sound(fx_ogg)  # Play OGG sound
    # ----------------------------------------------------------------------------------

    # Draw
    # ----------------------------------------------------------------------------------
    rl.begin_drawing()

    rl.clear_background(rl.RAYWHITE)

    rl.draw_text("Press SPACE to PLAY the WAV sound!", 200, 180, 20, rl.LIGHTGRAY)
    rl.draw_text("Press ENTER to PLAY the OGG sound!", 200, 220, 20, rl.LIGHTGRAY)

    rl.end_drawing()
    # ----------------------------------------------------------------------------------

# De-Initialization
# --------------------------------------------------------------------------------------
rl.unload_sound(fx_wav)  # Unload sound data
rl.unload_sound(fx_ogg)  # Unload sound data

rl.close_audio_device()  # Close audio device

rl.close_window()  # Close window and OpenGL context
# --------------------------------------------------------------------------------------
