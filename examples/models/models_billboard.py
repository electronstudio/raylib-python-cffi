# /*******************************************************************************************
# *
# *   raylib [models] example - Drawing billboards
# *
# *   This example has been created using raylib 1.3 (www.raylib.com)
# *   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# *
# *   Copyright (c) 2015 Ramon Santamaria (@raysan5)
# *
# ********************************************************************************************/

from raylib.static import *


# Initialization
#--------------------------------------------------------------------------------------
screenWidth = 800
screenHeight = 450

InitWindow(screenWidth, screenHeight, b"raylib [models] example - drawing billboards")

# Define the camera to look into our 3d world
cameraPtr = ffi.new("struct Camera3D *")
camera = cameraPtr[0]

camera.position = [ 5.0, 4.0, 5.0 ]
camera.target = [ 0.0, 2.0, 0.0 ]
camera.up = [ 0.0, 1.0, 0.0 ]
camera.fovy = 45.0
camera.projection = CAMERA_PERSPECTIVE


bill = LoadTexture(b"resources/billboard.png")     # Our texture billboard
billPosition = [ 0.0, 2.0, 0.0 ]                 # Position where draw billboard

SetCameraMode(camera, CAMERA_ORBITAL)  # Set an orbital camera mode

SetTargetFPS(60)                       # Set our game to run at 60 frames-per-second
#--------------------------------------------------------------------------------------

# Main game loop
while not WindowShouldClose()  :          # Detect window close button or ESC key
    # Update
    #----------------------------------------------------------------------------------
    UpdateCamera(cameraPtr)              # Update camera
    #----------------------------------------------------------------------------------

    # Draw
    #----------------------------------------------------------------------------------
    BeginDrawing()

    ClearBackground(RAYWHITE)

    BeginMode3D(camera)

    DrawBillboard(camera, bill, billPosition, 2.0, WHITE)

    DrawGrid(10, 1.0)        # Draw a grid

    EndMode3D()

    DrawFPS(10, 10)

    EndDrawing()
    #----------------------------------------------------------------------------------


# De-Initialization
#--------------------------------------------------------------------------------------
UnloadTexture(bill)        # Unload texture

CloseWindow()              # Close window and OpenGL context
#--------------------------------------------------------------------------------------

