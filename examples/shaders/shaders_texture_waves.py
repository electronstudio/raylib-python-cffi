import raylib as rl
from raylib.colors import *
import math

# a few functions ported from raymath
from rlmath import *

from ctypes import byref

#// Initialization
#//--------------------------------------------------------------------------------------
screenWidth = 800;
screenHeight = 450;

rl.SetConfigFlags(rl.FLAG_MSAA_4X_HINT| rl.FLAG_WINDOW_RESIZABLE);  # Enable Multi Sampling Anti Aliasing 4x (if available)
rl.InitWindow(screenWidth, screenHeight, b"raylib [shaders]")

camera = rl.ffi.new('struct Camera3D *', [
    [2, 12, 6],
    [0, .5, 0],
    [0, 1, 0],
    45,
    rl.CAMERA_PERSPECTIVE
])

texture = rl.LoadTexture(b"resources/space.png")

shader = rl.LoadShader(b"", b"resources/shaders/glsl330/wave.fs")
secondsLoc = rl.GetShaderLocation(shader, b"secondes")
freqXLoc = rl.GetShaderLocation(shader, b"freqX")
freqYLoc = rl.GetShaderLocation(shader, b"freqY")
ampXLoc = rl.GetShaderLocation(shader, b"ampX")
ampYLoc = rl.GetShaderLocation(shader, b"ampY")
speedXLoc = rl.GetShaderLocation(shader, b"speedX")
speedYLoc = rl.GetShaderLocation(shader, b"speedY")

freqX = rl.ffi.new("float *", 25.0)
freqY = rl.ffi.new("float *", 25.0)
ampX = rl.ffi.new("float *", 5.0)
ampY = rl.ffi.new("float *", 5.0)
speedX = rl.ffi.new("float *", 8.0)
speedY = rl.ffi.new("float *", 8.0)

screenSize = rl.ffi.new("struct Vector2 *",[ rl.GetScreenWidth(), rl.GetScreenHeight() ])
rl.SetShaderValue(shader, rl.GetShaderLocation(shader, b"size"), screenSize, rl.SHADER_UNIFORM_VEC2)

rl.SetShaderValue(shader, freqXLoc, freqX, rl.SHADER_UNIFORM_FLOAT)
rl.SetShaderValue(shader, freqYLoc, freqY, rl.SHADER_UNIFORM_FLOAT)
rl.SetShaderValue(shader, ampXLoc, ampX, rl.SHADER_UNIFORM_FLOAT)
rl.SetShaderValue(shader, ampYLoc, ampY, rl.SHADER_UNIFORM_FLOAT)
rl.SetShaderValue(shader, speedXLoc, speedX, rl.SHADER_UNIFORM_FLOAT)
rl.SetShaderValue(shader, speedYLoc, speedY, rl.SHADER_UNIFORM_FLOAT)
    
seconds = rl.ffi.new("float *", 0.0)

rl.SetTargetFPS(60)                      # // Set our game to run at 60 frames-per-second
#//--------------------------------------------------------------------------------------

#// Main game loop
while not rl.WindowShouldClose():            #// Detect window close button or ESC key
    #// Update
    #//----------------------------------------------------------------------------------
    seconds[0] += rl.GetFrameTime()
    rl.SetShaderValue(shader, secondsLoc, seconds, rl.SHADER_UNIFORM_FLOAT)
    #//----------------------------------------------------------------------------------

    #// Draw
    #//----------------------------------------------------------------------------------
    rl.BeginDrawing()


    rl.ClearBackground(RAYWHITE)
    rl.BeginShaderMode(shader);
    
    rl.DrawTexture(texture, 0, 0, WHITE);
    rl.DrawTexture(texture, texture.width, 0, WHITE);
        
    rl.EndShaderMode();

    rl.EndDrawing()
#//----------------------------------------------------------------------------------


#// De-Initialization
#//--------------------------------------------------------------------------------------


rl.CloseWindow()              #// Close window and OpenGL context
