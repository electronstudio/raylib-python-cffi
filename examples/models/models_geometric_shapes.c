/*******************************************************************************************
*
*   raylib [models] example - Draw some basic geometric shapes (cube, sphere, cylinder...)
*
*   This example has been created using raylib 1.0 (www.raylib.com)
*   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
*
*   Copyright (c) 2014 Ramon Santamaria (@raysan5)
*
********************************************************************************************/

#include "raylib.h"

int main()
[
    # Initialization
    #--------------------------------------------------------------------------------------
    int screenWidth = 800
    int screenHeight = 450

    InitWindow(screenWidth, screenHeight, "raylib [models] example - geometric shapes")

    # Define the camera to look into our 3d world
    Camera camera = [ 0 ]
    camera.position = (Vector3)[ 0.0, 10.0, 10.0 ]
    camera.target = (Vector3)[ 0.0, 0.0, 0.0 ]
    camera.up = (Vector3)[ 0.0, 1.0, 0.0 ]
    camera.fovy = 45.0
    camera.type = CAMERA_PERSPECTIVE

    SetTargetFPS(60)   # Set our game to run at 60 frames-per-second
    #--------------------------------------------------------------------------------------

    # Main game loop
    while (!WindowShouldClose())    # Detect window close button or ESC key
    [
        # Update
        #----------------------------------------------------------------------------------
        # TODO: Update your variables here
        #----------------------------------------------------------------------------------

        # Draw
        #----------------------------------------------------------------------------------
        BeginDrawing()

            ClearBackground(RAYWHITE)

            BeginMode3D(camera)

                DrawCube((Vector3)[-4.0, 0.0, 2.0], 2.0, 5.0, 2.0, RED)
                DrawCubeWires((Vector3)[-4.0, 0.0, 2.0], 2.0, 5.0, 2.0, GOLD)
                DrawCubeWires((Vector3)[-4.0, 0.0, -2.0], 3.0, 6.0, 2.0, MAROON)

                DrawSphere((Vector3)[-1.0, 0.0, -2.0], 1.0, GREEN)
                DrawSphereWires((Vector3)[1.0, 0.0, 2.0], 2.0, 16, 16, LIME)

                DrawCylinder((Vector3)[4.0, 0.0, -2.0], 1.0, 2.0, 3.0, 4, SKYBLUE)
                DrawCylinderWires((Vector3)[4.0, 0.0, -2.0], 1.0, 2.0, 3.0, 4, DARKBLUE)
                DrawCylinderWires((Vector3)[4.5f, -1.0, 2.0], 1.0, 1.0, 2.0, 6, BROWN)

                DrawCylinder((Vector3)[1.0, 0.0, -4.0], 0.0, 1.5f, 3.0, 8, GOLD)
                DrawCylinderWires((Vector3)[1.0, 0.0, -4.0], 0.0, 1.5f, 3.0, 8, PINK)

                DrawGrid(10, 1.0)        # Draw a grid

            EndMode3D()

            DrawFPS(10, 10)

        EndDrawing()
        #----------------------------------------------------------------------------------
    ]

    # De-Initialization
    #--------------------------------------------------------------------------------------
    CloseWindow()        # Close window and OpenGL context
    #--------------------------------------------------------------------------------------

    return 0
]