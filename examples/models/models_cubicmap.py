# /*******************************************************************************************
# *
# *   raylib [models] example - Cubicmap loading and drawing
# *
# *   This example has been created using raylib 1.8 (www.raylib.com)
# *   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# *
# *   Copyright (c) 2015 Ramon Santamaria (@raysan5)
# *
# ********************************************************************************************/

from raylib import *


# Initialization
#--------------------------------------------------------------------------------------
screenWidth = 800
screenHeight = 450

InitWindow(screenWidth, screenHeight, b"raylib [models] example - cubesmap loading and drawing")

# Define the camera to look into our 3d world
camera = ffi.new("struct Camera3D *", [[ 16.0, 14.0, 16.0 ], [ 0.0, 0.0, 0.0 ], [ 0.0, 1.0, 0.0 ], 45.0, 0 ])

image = LoadImage(b"resources/cubicmap.png")      # Load cubicmap image (RAM)
cubicmap = LoadTextureFromImage(image)       # Convert image to texture to display (VRAM)

mesh = GenMeshCubicmap(image, [ 1.0, 1.0, 1.0 ])
model = LoadModelFromMesh(mesh)

# NOTE: By default each cube is mapped to one part of texture atlas
texture = LoadTexture(b"resources/cubicmap_atlas.png")    # Load map texture
model.materials[0].maps[MATERIAL_MAP_ALBEDO ].texture = texture                 # Set map diffuse texture

mapPosition = [ -16.0, 0.0, -8.0 ]          # Set model position

UnloadImage(image)     # Unload cubesmap image from RAM, already uploaded to VRAM

SetCameraMode(camera[0], CAMERA_ORBITAL)  # Set an orbital camera mode

SetTargetFPS(60)                       # Set our game to run at 60 frames-per-second
#--------------------------------------------------------------------------------------

# Main game loop
while not WindowShouldClose():          # Detect window close button or ESC key

    # Update
    #----------------------------------------------------------------------------------
    UpdateCamera(camera)              # Update camera
    #----------------------------------------------------------------------------------

    # Draw
    #----------------------------------------------------------------------------------
    BeginDrawing()

    ClearBackground(RAYWHITE)

    BeginMode3D(camera[0])

    DrawModel(model, mapPosition, 1.0, WHITE)

    EndMode3D()

    DrawTextureEx(cubicmap, [ screenWidth - cubicmap.width*4 - 20, 20 ], 0.0, 4.0, WHITE)
    DrawRectangleLines(screenWidth - cubicmap.width*4 - 20, 20, cubicmap.width*4, cubicmap.height*4, GREEN)

    DrawText(b"cubicmap image used to", 658, 90, 10, GRAY)
    DrawText(b"generate map 3d model", 658, 104, 10, GRAY)

    DrawFPS(10, 10)

    EndDrawing()
    #----------------------------------------------------------------------------------


# De-Initialization
#--------------------------------------------------------------------------------------
UnloadTexture(cubicmap)    # Unload cubicmap texture
UnloadTexture(texture)     # Unload map texture
UnloadModel(model)         # Unload map model

CloseWindow()              # Close window and OpenGL context
#--------------------------------------------------------------------------------------

