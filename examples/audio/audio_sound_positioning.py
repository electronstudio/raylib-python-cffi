"""checked with raylib-python-cffi 5.5.0.2
raylib [audio] example - Playing spatialized 3D sound
Example complexity rating: [★★☆☆] 2/4
Example originally created with raylib 5.5, last time updated with raylib 5.5
Example contributed by Le Juez Victor (@Bigfoot71) and reviewed by Ramon Santamaria (@raysan5)
Example licensed under an unmodified zlib/libpng license, which is an OSI-certified,
BSD-like license that allows static linking with closed source software
Copyright (c) 2025 Le Juez Victor (@Bigfoot71)

This source has been converted from C raylib examples to Python.
"""

import pyray as rl
import math
from pathlib import Path

# Get the directory where this script is located
THIS_DIR = Path(__file__).resolve().parent


# Sound positioning function
def set_sound_position(listener, sound, position, max_dist):
    # Calculate direction vector and distance between listener and sound source
    direction = rl.vector3_subtract(position, listener.position)
    distance = rl.vector3_length(direction)

    # Apply logarithmic distance attenuation and clamp between 0-1
    attenuation = 1.0 / (1.0 + (distance / max_dist))
    attenuation = rl.clamp(attenuation, 0.0, 1.0)

    # Calculate normalized vectors for spatial positioning
    normalized_direction = rl.vector3_normalize(direction)
    forward = rl.vector3_normalize(
        rl.vector3_subtract(listener.target, listener.position)
    )
    right = rl.vector3_normalize(rl.vector3_cross_product(listener.up, forward))

    # Reduce volume for sounds behind the listener
    dot_product = rl.vector3_dot_product(forward, normalized_direction)
    if dot_product < 0.0:
        attenuation *= 1.0 + dot_product * 0.5

    # Set stereo panning based on sound position relative to listener
    pan = 0.5 + 0.5 * rl.vector3_dot_product(normalized_direction, right)

    # Apply final sound properties
    rl.set_sound_volume(sound, attenuation)
    rl.set_sound_pan(sound, pan)


# Initialization
# --------------------------------------------------------------------------------------
screen_width = 800
screen_height = 450

rl.init_window(
    screen_width, screen_height, "raylib [audio] example - Playing spatialized 3D sound"
)

rl.init_audio_device()

sound = rl.load_sound(str(THIS_DIR / "resources/coin.wav"))

camera = rl.Camera3D(
    (0, 5, 5),
    (0, 0, 0),
    (0, 1, 0),
    60.0,
    rl.CameraProjection.CAMERA_PERSPECTIVE,
)

rl.disable_cursor()

rl.set_target_fps(60)
# --------------------------------------------------------------------------------------

# Main game loop
while not rl.window_should_close():
    # Update
    # ----------------------------------------------------------------------------------
    rl.update_camera(camera, rl.CameraMode.CAMERA_FREE)

    th = rl.get_time()

    sphere_pos = rl.Vector3(5.0 * math.cos(th), 0.0, 5.0 * math.sin(th))

    set_sound_position(camera, sound, sphere_pos, 20.0)
    if not rl.is_sound_playing(sound):
        rl.play_sound(sound)
    # ----------------------------------------------------------------------------------

    # Draw
    # ----------------------------------------------------------------------------------
    rl.begin_drawing()

    rl.clear_background(rl.RAYWHITE)

    rl.begin_mode_3d(camera)
    rl.draw_grid(10, 2)
    rl.draw_sphere(sphere_pos, 0.5, rl.RED)
    rl.end_mode_3d()

    rl.end_drawing()
    # ----------------------------------------------------------------------------------

# De-Initialization
# --------------------------------------------------------------------------------------
rl.unload_sound(sound)
rl.close_audio_device()  # Close audio device

rl.close_window()  # Close window and OpenGL context
# --------------------------------------------------------------------------------------
