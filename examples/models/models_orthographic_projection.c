/*******************************************************************************************
*
*   raylib [models] example - Show the difference between perspective and orthographic projection 
*
*   This program is heavily based on the geometric objects example
*
*   This example has been created using raylib 1.9.7 (www.raylib.com)
*   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
*
*   Copyright (c) 2018 Max Danielsson & Ramon Santamaria (@raysan5)
*
********************************************************************************************/

#include "raylib.h"

#define FOVY_PERSPECTIVE    45.0
#define WIDTH_ORTHOGRAPHIC  10.0

int main()
[
    # Initialization
    #--------------------------------------------------------------------------------------
    int screenWidth = 800
    int screenHeight = 450

    InitWindow(screenWidth, screenHeight, "raylib [models] example - geometric shapes")

    # Define the camera to look into our 3d world
    Camera camera = [[ 0.0, 10.0, 10.0 ], [ 0.0, 0.0, 0.0 ], [ 0.0, 1.0, 0.0 ], FOVY_PERSPECTIVE, CAMERA_PERSPECTIVE ]

    SetTargetFPS(60)   # Set our game to run at 60 frames-per-second
    #--------------------------------------------------------------------------------------

    # Main game loop
    while (!WindowShouldClose())    # Detect window close button or ESC key
    [
        # Update
        #----------------------------------------------------------------------------------
        if (IsKeyPressed(KEY_SPACE)) 
        [
            if (camera.type == CAMERA_PERSPECTIVE) 
            [
                camera.fovy = WIDTH_ORTHOGRAPHIC
                camera.type = CAMERA_ORTHOGRAPHIC
            ]
            else 
            [
                camera.fovy = FOVY_PERSPECTIVE
                camera.type = CAMERA_PERSPECTIVE
            ]
        ]
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

            DrawText("Press Spacebar to switch camera type", 10, GetScreenHeight() - 30, 20, DARKGRAY)

            if (camera.type == CAMERA_ORTHOGRAPHIC) DrawText("ORTHOGRAPHIC", 10, 40, 20, BLACK)
            else if (camera.type == CAMERA_PERSPECTIVE) DrawText("PERSPECTIVE", 10, 40, 20, BLACK)

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
