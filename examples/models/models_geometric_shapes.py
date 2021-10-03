# /*******************************************************************************************
# *
# *   raylib [models] example - Draw some basic geometric shapes (cube, sphere, cylinder...)
# *
# *   This example has been created using raylib 1.0 (www.raylib.com)
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

InitWindow(screenWidth, screenHeight, b"raylib [models] example - geometric shapes")

# Define the camera to look into our 3d world
cameraPtr = ffi.new("struct Camera3D *")
camera = cameraPtr[0]
camera.position = [ 0.0, 10.0, 10.0 ]
camera.target = [ 0.0, 0.0, 0.0 ]
camera.up = [ 0.0, 1.0, 0.0 ]
camera.fovy = 45.0
camera.projection = CAMERA_PERSPECTIVE

SetTargetFPS(60)   # Set our game to run at 60 frames-per-second
#--------------------------------------------------------------------------------------

# Main game loop
while not WindowShouldClose():    # Detect window close button or ESC key
    # Update
    #----------------------------------------------------------------------------------
    # TODO: Update your variables here
    #----------------------------------------------------------------------------------

    # Draw
    #----------------------------------------------------------------------------------
    BeginDrawing()

    ClearBackground(RAYWHITE)

    BeginMode3D(camera)

    DrawCube([-4.0, 0.0, 2.0], 2.0, 5.0, 2.0, RED)
    DrawCubeWires([-4.0, 0.0, 2.0], 2.0, 5.0, 2.0, GOLD)
    DrawCubeWires([-4.0, 0.0, -2.0], 3.0, 6.0, 2.0, MAROON)

    DrawSphere([-1.0, 0.0, -2.0], 1.0, GREEN)
    DrawSphereWires([1.0, 0.0, 2.0], 2.0, 16, 16, LIME)

    DrawCylinder([4.0, 0.0, -2.0], 1.0, 2.0, 3.0, 4, SKYBLUE)
    DrawCylinderWires([4.0, 0.0, -2.0], 1.0, 2.0, 3.0, 4, DARKBLUE)
    DrawCylinderWires([4.5, -1.0, 2.0], 1.0, 1.0, 2.0, 6, BROWN)

    DrawCylinder([1.0, 0.0, -4.0], 0.0, 1.5, 3.0, 8, GOLD)
    DrawCylinderWires([1.0, 0.0, -4.0], 0.0, 1.5, 3.0, 8, PINK)

    DrawGrid(10, 1.0)        # Draw a grid

    EndMode3D()

    DrawFPS(10, 10)

    EndDrawing()
    #----------------------------------------------------------------------------------


# De-Initialization
#--------------------------------------------------------------------------------------
CloseWindow()        # Close window and OpenGL context
#--------------------------------------------------------------------------------------
