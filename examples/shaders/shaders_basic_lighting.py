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

#<<<<<<< HEAD
#<<<<<<< HEAD
#<<<<<<< HEAD
from raylib import rl, ffi
#=======
#from raylib.dynamic import raylib as rl, ffi
#>>>>>>> ffe4403 (complete fog example)
#=======
#from raylib.static import rl, ffi
#>>>>>>> 10b63b9 (added shaders_texture_waves.py)
#=======
#from raylib.static import rl, ffi
#>>>>>>> 1775ffc4b093c881ee44a8027b4143add066d738
from raylib.colors import *
from dataclasses import dataclass
from enum import Enum
from typing import Any
import math

# a few functions ported from raymath
from rlmath import *

# lighting system
from light_system import *

#// Initialization
#//--------------------------------------------------------------------------------------
screenWidth = 1200;
screenHeight = 720;

rl.SetConfigFlags(rl.FLAG_MSAA_4X_HINT| rl.FLAG_WINDOW_RESIZABLE);  # Enable Multi Sampling Anti Aliasing 4x (if available)
rl.InitWindow(screenWidth, screenHeight, b"raylib [shaders] example - basic lighting")

camera = ffi.new('struct Camera3D *', [
    [2, 2, 6],
    [0, .5, 0],
    [0, 1, 0],
    45,
    rl.CAMERA_PERSPECTIVE
])

#// Load models
modelA = rl.LoadModelFromMesh(rl.GenMeshTorus(0.4, 1.0, 16, 32))
modelB = rl.LoadModelFromMesh(rl.GenMeshCube(1.0, 1.0, 1.0))
modelC = rl.LoadModelFromMesh(rl.GenMeshSphere(0.5, 32, 32))

#// Load models texture
texture = rl.LoadTexture(b"resources/texel_checker.png")

#// Assign texture to default model material
modelA.materials[0].maps[rl.MAP_DIFFUSE].texture = texture
modelB.materials[0].maps[rl.MAP_DIFFUSE].texture = texture
modelC.materials[0].maps[rl.MAP_DIFFUSE].texture = texture

angle = 6.282;

#// Using 4 point lights, white, red, green and blue

lights0 = Light(LIGHT_POINT,  [ 4, 2, 4 ], Vector3Zero(), WHITE)
lights1 = Light(LIGHT_POINT, [4, 2, 4 ], Vector3Zero(), RED)
lights2 = Light(LIGHT_POINT, [ 0, 4, 2 ], Vector3Zero(), GREEN)
lights3 = Light(LIGHT_POINT, [ 0, 4, 2 ], Vector3Zero(), BLUE)

lightSystem = LightSystem([ 0.2, 0.2, 0.2, 1.0 ], lights0, lights1, lights2, lights3)
fogD = rl.GetShaderLocation(lightSystem.shader, b'FogDensity')
fogDensity = 0.0

#// All models use the same shader - which lights them
modelA.materials[0].shader = lightSystem.shader
modelB.materials[0].shader = lightSystem.shader
modelC.materials[0].shader = lightSystem.shader

rl.SetCameraMode(camera[0], rl.CAMERA_ORBITAL)  # Set an orbital camera mode

rl.SetTargetFPS(60)                      # // Set our game to run at 60 frames-per-second
#//--------------------------------------------------------------------------------------

#// Main game loop
while not rl.WindowShouldClose():            #// Detect window close button or ESC key
    #// Update
    #//----------------------------------------------------------------------------------
    if rl.IsKeyPressed(rl.KEY_W):  lights0.enabled = not lights0.enabled
    if rl.IsKeyPressed(rl.KEY_R):  lights1.enabled = not lights1.enabled
    if rl.IsKeyPressed(rl.KEY_G):  lights2.enabled = not lights2.enabled
    if rl.IsKeyPressed(rl.KEY_B):  lights3.enabled = not lights3.enabled

    rl.UpdateCamera(camera)              #// Update camera

    #// Make the lights do differing orbits
    angle -= 0.02
    lights0.position.x = math.cos(angle)*4.0
    lights0.position.z = math.sin(angle)*4.0
    lights1.position.x = math.cos(-angle*0.6)*4.0
    lights1.position.z = math.sin(-angle*0.6)*4.0
    lights2.position.y = math.cos(angle*0.2)*4.0
    lights2.position.z = math.sin(angle*0.2)*4.0
    lights3.position.y = math.cos(-angle*0.35)*4.0
    lights3.position.z = math.sin(-angle*0.35)*4.0

    #// Update the light shader with the camera view position

    lightSystem.update(camera.position)


# ffi.cast('wchar_t', x)
#    modelA.transform = ffi.cast('Matrix *', MatrixRotateY(angle*1.7))[0]
#    modelA.transform = MatrixRotateY(angle*1.7)
    #// Rotate the torus
#    modelA.transform = MatrixMultiply(modelA.transform, MatrixRotateX(-0.025)[0])[0]
#    modelA.transform = MatrixMultiply(modelA.transform, MatrixRotateZ(0.012)[0])[0]
    modelA.transform = ffi.cast('Matrix *', MatrixMultiply(modelA.transform, MatrixRotateX(-0.025)))[0]
    modelA.transform = ffi.cast('Matrix *', MatrixMultiply(modelA.transform, MatrixRotateZ(0.012)))[0]

    if (rl.IsKeyPressed(rl.KEY_F)):
        rl.ToggleFullscreen()


    #//----------------------------------------------------------------------------------

    #// Draw
    #//----------------------------------------------------------------------------------
    rl.BeginDrawing()

    rl.ClearBackground(RAYWHITE)

    rl.BeginMode3D(camera[0])

    #// Draw the three models
    rl.DrawModel(modelA, [0,0,0], 1.0, WHITE)
    rl.DrawModel(modelB, [-1.6,0,0], 1.0, WHITE)
    rl.DrawModel(modelC, [ 1.6,0,0], 1.0, WHITE)

    #// Draw markers to show where the lights are
    lightSystem.draw()


    rl.DrawGrid(10, 1.0)

    rl.EndMode3D()

    rl.DrawFPS(10, 10)

    rl.DrawText(b"Keys RGB & W toggle lights", 10, 30, 20, DARKGRAY)

    rl.EndDrawing()
#//----------------------------------------------------------------------------------


#// De-Initialization
#//--------------------------------------------------------------------------------------
rl.UnloadModel(modelA) #        // Unload the modelA
rl.UnloadModel(modelB) #        // Unload the modelB
rl.UnloadModel(modelC) #        // Unload the modelC

rl.UnloadTexture(texture)     #// Unload the texture

rl.UnloadShader(lightSystem.shader)

rl.CloseWindow()              #// Close window and OpenGL context
