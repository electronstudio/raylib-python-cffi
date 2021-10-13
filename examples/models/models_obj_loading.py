# /*******************************************************************************************
# *
# *   raylib [models] example - Load and draw a 3d model (OBJ)
# *
# *   This example has been created using raylib 1.3 (www.raylib.com)
# *   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# *
# *   Copyright (c) 2014 Ramon Santamaria (@raysan5)
# *
# ********************************************************************************************/

from raylib import *

# Initialization
#--------------------------------------------------------------------------------------
screenWidth = 800
screenHeight = 450

InitWindow(screenWidth, screenHeight, b"raylib [models] example - obj model loading")

# Define the camera to look into our 3d world
camera =  ffi.new("struct Camera3D *")
camera.position = [ 5.0, 5.0, 5.0 ]    # Camera position
camera.target = [ 0.0, 2.5, 0.0 ]      # Camera looking at point
camera.up = [ 0.0, 1.0, 0.0 ]          # Camera up vector (rotation towards target)
camera.fovy = 45.0                                # Camera field-of-view Y
camera.projection = CAMERA_PERSPECTIVE                   # Camera mode type

rl.SetCameraMode(camera[0], rl.CAMERA_ORBITAL)

model = LoadModel(b"resources/models/house.obj")                 # Load OBJ model
texture = LoadTexture(b"resources/models/house_diffuse.png") # Load model texture
model.materials.maps[MATERIAL_MAP_ALBEDO].texture = texture                     # Set map diffuse texture
position = [ 0.0, 0.0, 0.0 ]                                # Set model position

SetTargetFPS(60)   # Set our game to run at 60 frames-per-second
#--------------------------------------------------------------------------------------

# Main game loop
while not WindowShouldClose():    # Detect window close button or ESC key
    # Update
    #----------------------------------------------------------------------------------
    #...
    #----------------------------------------------------------------------------------
    rl.UpdateCamera(camera);
    # Draw
    #----------------------------------------------------------------------------------
    BeginDrawing()

    ClearBackground(RAYWHITE)

    BeginMode3D(camera[0])

    DrawModel(model, position, 0.2, WHITE)   # Draw 3d model with texture

    DrawGrid(10, 1.0)         # Draw a grid

    EndMode3D()

    DrawText(b"(c) Castle 3D model by Alberto Cano", screenWidth - 200, screenHeight - 20, 10, GRAY)

    DrawFPS(10, 10)

    EndDrawing()
    #----------------------------------------------------------------------------------


# De-Initialization
#--------------------------------------------------------------------------------------
UnloadTexture(texture)     # Unload texture
UnloadModel(model)         # Unload model

CloseWindow()              # Close window and OpenGL context
#--------------------------------------------------------------------------------------

