"""

raylib [audio] example - playing

"""
import dataclasses
import pyray
import raylib as rl
from raylib.colors import (
    RAYWHITE,
    ORANGE,
    RED,
    GOLD,
    LIME,
    BLUE,
    VIOLET,
    BROWN,
    LIGHTGRAY,
    PINK,
    YELLOW,
    GREEN,
    SKYBLUE,
    PURPLE,
    BEIGE,
    MAROON,
    GRAY,
    BLACK
)


MAX_CIRCLES=64


@dataclasses.dataclass
class CircleWave:
    position: 'rl.Vector2'
    radius: float
    alpha: float
    speed: float
    color: 'rl.Color'


screenWidth = 800
screenHeight = 450

rl.SetConfigFlags(rl.FLAG_MSAA_4X_HINT)  # NOTE: Try to enable MSAA 4X

rl.InitWindow(screenWidth, screenHeight, b"raylib [audio] example - module playing (streaming)")

rl.InitAudioDevice()                  # Initialize audio device

colors = [ ORANGE, RED, GOLD, LIME, BLUE, VIOLET, BROWN, LIGHTGRAY, PINK,
           YELLOW, GREEN, SKYBLUE, PURPLE, BEIGE ]

# Creates some circles for visual effect
circles = []

for i in range(MAX_CIRCLES):
    rad = rl.GetRandomValue(10, 40)
    pos = pyray.Vector2(
        float(rl.GetRandomValue(rad, int(screenWidth) - rad)),
        float(rl.GetRandomValue(rad, int(screenHeight) - rad))
    )
    c = CircleWave(
        alpha=0.0,
        radius=float(rad),
        position=pos,
        speed=float(rl.GetRandomValue(1, 100))/2000.0,
        color=colors[rl.GetRandomValue(0, 13)]
    )
    circles.append(c)

music = rl.LoadMusicStream(b"resources/mini1111.xm")
music.looping = False
pitch = 1.0

rl.PlayMusicStream(music)
timePlayed = 0.0
pause = False

rl.SetTargetFPS(60) # Set our game to run at 60 frames-per-second


# Main game loop
while not rl.WindowShouldClose():    # Detect window close button or ESC key
    # Update
    #----------------------------------------------------------------------------------
    rl.UpdateMusicStream(music)      # Update music buffer with new stream data

    # Restart music playing (stop and play)
    if rl.IsKeyPressed(rl.KEY_SPACE):
        rl.StopMusicStream(music)
        rl.PlayMusicStream(music)
        pause = False

    # Pause/Resume music playing
    if rl.IsKeyPressed(rl.KEY_P):
        pause = not pause
        if pause:
            rl.PauseMusicStream(music)
        else:
            rl.ResumeMusicStream(music)


    if rl.IsKeyDown(rl.KEY_DOWN):
        pitch -= 0.01
    elif rl.IsKeyDown(rl.KEY_UP):
        pitch += 0.01

    rl.SetMusicPitch(music, pitch)

    # Get timePlayed scaled to bar dimensions
    timePlayed = (rl.GetMusicTimePlayed(music) / rl.GetMusicTimeLength(music))*(screenWidth - 40)

    # Color circles animation
    for i in range(MAX_CIRCLES):
        if pause:
            break

        circles[i].alpha += circles[i].speed
        circles[i].radius += circles[i].speed*10.0

        if circles[i].alpha > 1.0:
            circles[i].speed *= -1

        if circles[i].alpha <= 0.0:
            circles[i].alpha = 0.0
            rad = rl.GetRandomValue(10, 40)
            pos = pyray.Vector2(
                float(rl.GetRandomValue(rad, int(screenWidth) - rad)),
                float(rl.GetRandomValue(rad, int(screenHeight) - rad))
            )
            circles[i].position = pos
            circles[i].radius = float(rad)
            circles[i].speed = float(rl.GetRandomValue(1, 100)) / 2000.0
            circles[i].color = colors[rl.GetRandomValue(0, 13)]

    #----------------------------------------------------------------------------------

    # Draw
    #----------------------------------------------------------------------------------
    pyray.begin_drawing()

    pyray.clear_background(RAYWHITE)

    for i in range(MAX_CIRCLES):
        pyray.draw_circle_v(circles[i].position, circles[i].radius, rl.Fade(circles[i].color, circles[i].alpha))

    # Draw time bar
    pyray.draw_rectangle(20, screenHeight - 20 - 12, screenWidth - 40, 12, LIGHTGRAY)
    pyray.draw_rectangle(20, screenHeight - 20 - 12, int(timePlayed), 12, MAROON)
    pyray.draw_rectangle_lines(20, screenHeight - 20 - 12, screenWidth - 40, 12, GRAY)

    # Draw help instructions
    pyray.draw_rectangle(20, 20, 425, 145, RAYWHITE)
    pyray.draw_rectangle_lines(20, 20, 425, 145, GRAY)
    pyray.draw_text("PRESS SPACE TO RESTART MUSIC", 40, 40, 20, BLACK)
    pyray.draw_text("PRESS P TO PAUSE/RESUME", 40, 70, 20, BLACK)
    pyray.draw_text("PRESS UP/DOWN TO CHANGE SPEED", 40, 100, 20, BLACK)
    pyray.draw_text(f"SPEED: {pitch}", 40, 130, 20, MAROON)

    pyray.end_drawing()
    #----------------------------------------------------------------------------------


# De-Initialization
#--------------------------------------------------------------------------------------
rl.UnloadMusicStream(music)          # Unload music stream buffers from RAM

rl.CloseAudioDevice()     # Close audio device (music streaming is automatically stopped)

rl.CloseWindow()          # Close window and OpenGL context
