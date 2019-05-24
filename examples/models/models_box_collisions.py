# /*******************************************************************************************
# *
# *   raylib [models] example - Detect basic 3d collisions (box vs sphere vs box)
# *
# *   This example has been created using raylib 1.3 (www.raylib.com)
# *   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# *
# *   Copyright (c) 2015 Ramon Santamaria (@raysan5)
# *
# ********************************************************************************************/

from raylib.static import *

# Initialization
# --------------------------------------------------------------------------------------
screenWidth = 800
screenHeight = 450

InitWindow(screenWidth, screenHeight, b"raylib [models] example - box collisions")

# Define the camera to look into our 3d world
camera = [[0.0, 10.0, 10.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0]

playerPositionPtr = ffi.new("struct Vector3 *", [0.0, 1.0, 2.0])
playerPosition = playerPositionPtr[0]

playerSizePtr = ffi.new("struct Vector3 *", [1.0, 2.0, 1.0])
playerSize = playerSizePtr[0]
playerColor = GREEN

enemyBoxPosPtr =  ffi.new("struct Vector3 *", [-4.0, 1.0, 0.0])
enemyBoxPos = enemyBoxPosPtr[0]
enemyBoxSize = ffi.new("struct Vector3 *",[2.0, 2.0, 2.0])

enemySpherePos = [4.0, 0.0, 0.0]
enemySphereSize = 1.5

collision = False

SetTargetFPS(60)  # Set our game to run at 60 frames-per-second
# --------------------------------------------------------------------------------------

# Main game loop
while not WindowShouldClose():  # Detect window close button or ESC key
    # Update
    # ----------------------------------------------------------------------------------

    # Move player
    if IsKeyDown(KEY_RIGHT):
        playerPosition.x += 0.2
    elif IsKeyDown(KEY_LEFT):
        playerPosition.x -= 0.2
    elif IsKeyDown(KEY_DOWN):
        playerPosition.z += 0.2
    elif IsKeyDown(KEY_UP):
        playerPosition.z -= 0.2

    collision = False

    # Check collisions player vs enemy-box
    if CheckCollisionBoxes([[playerPosition.x - playerSize.x / 2, playerPosition.y - playerSize.y / 2,
                             playerPosition.z - playerSize.z / 2],
                            [playerPosition.x + playerSize.x / 2, playerPosition.y + playerSize.y / 2,
                             playerPosition.z + playerSize.z / 2]],
                           [[enemyBoxPos.x - enemyBoxSize.x / 2,
                             enemyBoxPos.y - enemyBoxSize.y / 2,
                             enemyBoxPos.z - enemyBoxSize.z / 2],
                            [enemyBoxPos.x + enemyBoxSize.x / 2,
                             enemyBoxPos.y + enemyBoxSize.y / 2,
                             enemyBoxPos.z + enemyBoxSize.z / 2]]):
        collision = True

        # Check collisions player vs enemy-sphere
    if CheckCollisionBoxSphere([[playerPosition.x - playerSize.x / 2,
                                 playerPosition.y - playerSize.y / 2,
                                 playerPosition.z - playerSize.z / 2],
                                [playerPosition.x + playerSize.x / 2,
                                 playerPosition.y + playerSize.y / 2,
                                 playerPosition.z + playerSize.z / 2]],
                               enemySpherePos, enemySphereSize):
        collision = True

    if collision:
        playerColor = RED
    else:
        playerColor = GREEN

    # ----------------------------------------------------------------------------------

    # Draw
    # ----------------------------------------------------------------------------------
    BeginDrawing()

    ClearBackground(RAYWHITE)

    BeginMode3D(camera)

    # Draw enemy-box
    DrawCube(enemyBoxPos, enemyBoxSize.x, enemyBoxSize.y, enemyBoxSize.z, GRAY)
    DrawCubeWires(enemyBoxPos, enemyBoxSize.x, enemyBoxSize.y, enemyBoxSize.z, DARKGRAY)

    # Draw enemy-sphere
    DrawSphere(enemySpherePos, enemySphereSize, GRAY)
    DrawSphereWires(enemySpherePos, enemySphereSize, 16, 16, DARKGRAY)

    # Draw player
    DrawCubeV(playerPosition, playerSize, playerColor)

    DrawGrid(10, 1.0)  # Draw a grid

    EndMode3D()

    DrawText(b"Move player with cursors to collide", 220, 40, 20, GRAY)

    DrawFPS(10, 10)

    EndDrawing()
    # ----------------------------------------------------------------------------------


        # De-Initialization
        # --------------------------------------------------------------------------------------
CloseWindow()  # Close window and OpenGL context
        # --------------------------------------------------------------------------------------
