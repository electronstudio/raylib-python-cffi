#!/usr/bin/env python3
# /*******************************************************************************************
# *
# *   raylib [shaders] example - basic lighting
# *
# *   NOTE: This example requires raylib OpenGL 3.3 or ES2 versions for shaders support,
#     *         OpenGL 1.1 does not support shaders, recompile raylib to OpenGL 3.3 version.
# *
# *   NOTE: Shaders used in this example are #version 330 (OpenGL 3.3).
# *
# *   This example has been created using raylib 2.5 (www.raylib.com)
# *   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# *
# *   Example contributed by Chris Camacho (@codifies) and reviewed by Ramon Santamaria (@raysan5)
# *
# *   Chris Camacho (@codifies -  http://bedroomcoders.co.uk/) notes:
# *
# *   This is based on the PBR lighting example, but greatly simplified to aid learning...
# *   actually there is very little of the PBR example left!
# *   When I first looked at the bewildering complexity of the PBR example I feared
# *   I would never understand how I could do simple lighting with raylib however its
# *   a testement to the authors of raylib (including rlights.h) that the example
# *   came together fairly quickly.
# *
# *   Copyright (c) 2019 Chris Camacho (@codifies) and Ramon Santamaria (@raysan5)
# *
# *
# ********************************************************************************************/

from raylib.dynamic import raylib as rl, ffi
from raylib.colors import *
import math

# a few functions ported from raymath
from rlmath import *


#// Initialization
#//--------------------------------------------------------------------------------------
screenWidth = 800;
screenHeight = 450;

rl.SetConfigFlags(rl.FLAG_MSAA_4X_HINT| rl.FLAG_WINDOW_RESIZABLE);  # Enable Multi Sampling Anti Aliasing 4x (if available)
rl.InitWindow(screenWidth, screenHeight, b"raylib [shaders] example - basic lighting")

camera = ffi.new('struct Camera3D *', [
    [2, 12, 6],
    [0, .5, 0],
    [0, 1, 0],
    45,
    rl.CAMERA_PERSPECTIVE
])

model = rl.LoadModel(b"resources/models/barracks.obj")                  # // Load OBJ model
texture = rl.LoadTexture(b"resources/models/barracks_diffuse.png")      # // Load model texture (diffuse map)

#// Assign texture to default model material
model.materials[0].maps[rl.MAP_DIFFUSE].texture = texture
#// NOTE: Defining 0 (NULL) for vertex shader forces usage of internal default vertex shader
shader = rl.LoadShader(b"", b"resources/shaders/glsl330/swirl.fs")
swirlCenterLoc = rl.GetShaderLocation(shader, b"center")
angle = 6.282;



swirl = ffi.new("struct Vector2 *", [0,0])

target = rl.LoadRenderTexture(screenWidth, screenHeight)

rl.SetTargetFPS(60)                      # // Set our game to run at 60 frames-per-second
#//--------------------------------------------------------------------------------------

#// Main game loop
while not rl.WindowShouldClose():            #// Detect window close button or ESC key
    #// Update
    #//----------------------------------------------------------------------------------

    angle -= 0.002
    camera.position.x = math.sin(angle) * 30.0
    camera.position.z = math.cos(angle) * 30.0
    rl.UpdateCamera(camera)              #// Update camera

    swirl.x = rl.GetMouseX()
    swirl.y = screenHeight - rl.GetMouseY()
    rl.SetShaderValue(shader, swirlCenterLoc, swirl, rl.UNIFORM_VEC2);
    #//----------------------------------------------------------------------------------

    #// Draw
    #//----------------------------------------------------------------------------------
    rl.BeginDrawing()


    rl.BeginTextureMode(target)
    rl.ClearBackground(RAYWHITE)
    rl.BeginMode3D(camera[0])

    #// Draw the three models
    rl.DrawModel(model, [0,0,0], 1.0, WHITE)

    rl.DrawGrid(10, 1.0)

    rl.EndTextureMode()
    rl.EndMode3D()
    
    rl.BeginShaderMode(shader)
    #// NOTE: Render texture must be y-flipped due to default OpenGL coordinates (left-bottom)
    rl.DrawTextureRec(target.texture, [ 0, 0, target.texture.width,-target.texture.height], [0.0], WHITE)
    rl.EndShaderMode()
    #// Draw some 2d text over drawn texture
    rl.DrawText(b"(c) Barracks 3D model by Alberto Cano", screenWidth - 220, screenHeight - 20, 10, GRAY);

    
    rl.DrawFPS(10, 10)

    rl.EndDrawing()
#//----------------------------------------------------------------------------------


#// De-Initialization
#//--------------------------------------------------------------------------------------
rl.UnloadModel(model) #        // Unload the model

rl.UnloadTexture(texture)     #// Unload the texture

rl.CloseWindow()              #// Close window and OpenGL context
