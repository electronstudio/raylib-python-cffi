# /*******************************************************************************************
# *
# *   raylib [textures] example - Bunnymark
# *
# *   This example has been created using raylib 1.6 (www.raylib.com)
# *   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# *
# *   Copyright (c) 2014-2019 Ramon Santamaria (@raysan5)
# *
# ********************************************************************************************/

from raylib import *
MAX_BUNNIES      =  500000

# This is the maximum amount of elements (quads) per batch
# NOTE: This value is defined in [rlgl] module and can be changed there
MAX_BATCH_ELEMENTS  = 8192


class Bunny:
    def __init__(self):
        self.position = ffi.new('struct Vector2 *', [0.0, 0.0])
        self.speed = ffi.new('struct Vector2 *', [0.0, 0.0])
        self.color = ffi.new('struct Color *', [0, 0, 0, 0])


# // Initialization
# //--------------------------------------------------------------------------------------
screenWidth = 1920;
screenHeight = 1080;

InitWindow(screenWidth, screenHeight, b"raylib [textures] example - bunnymark")

# // Load bunny texture
texBunny = LoadTexture(b"resources/wabbit_alpha.png")

bunnies = []
for i in range(0, MAX_BUNNIES):
    bunnies.append(Bunny())

bunniesCount = 0;          # Bunnies counter

SetTargetFPS(60);               # Set our game to run at 60 frames-per-second
#//--------------------------------------------------------------------------------------

#// Main game loop
while not WindowShouldClose():    #// Detect window close button or ESC key
    #// Update
    #//----------------------------------------------------------------------------------
    if IsMouseButtonDown(MOUSE_BUTTON_LEFT):
        #// Create more bunnies
        for i in range(0, 100):
            if bunniesCount < MAX_BUNNIES:
                bunnies[bunniesCount].position = GetMousePosition()
                bunnies[bunniesCount].speed.x = GetRandomValue(-250, 250)/60.0
                bunnies[bunniesCount].speed.y = GetRandomValue(-250, 250)/60.0
                bunnies[bunniesCount].color = (GetRandomValue(50, 240),
                                                   GetRandomValue(80, 240),
                                                   GetRandomValue(100, 240), 255 )

                bunniesCount+=1


    # // Update bunnies
    for i in range(0, bunniesCount):
        bunnies[i].position.x += bunnies[i].speed.x;
        bunnies[i].position.y += bunnies[i].speed.y;

        if ((bunnies[i].position.x + texBunny.width/2) > GetScreenWidth()) or ((bunnies[i].position.x + texBunny.width/2) < 0):
            bunnies[i].speed.x *= -1
        if ((bunnies[i].position.y + texBunny.height/2) > GetScreenHeight()) or ((bunnies[i].position.y + texBunny.height/2 - 40) < 0):
            bunnies[i].speed.y *= -1

    # //----------------------------------------------------------------------------------
    #
    # // Draw
    # //----------------------------------------------------------------------------------
    BeginDrawing()

    ClearBackground(RAYWHITE)

    for i in range(0, bunniesCount):
        # // NOTE: When internal batch buffer limit is reached (MAX_BATCH_ELEMENTS),
        # // a draw call is launched and buffer starts being filled again;
        # // before issuing a draw call, updated vertex data from internal CPU buffer is send to GPU...
        # // Process of sending data is costly and it could happen that GPU data has not been completely
        # // processed for drawing while new data is tried to be sent (updating current in-use buffers)
        # // it could generates a stall and consequently a frame drop, limiting the number of drawn bunnies
        DrawTexture(texBunny, int(bunnies[i].position.x), int(bunnies[i].position.y), bunnies[i].color)

    DrawRectangle(0, 0, screenWidth, 40, BLACK)
    text = f"bunnies {bunniesCount}"
    DrawText(text.encode('utf-8'), 120, 10, 20, GREEN)
    text = f"batched draw calls: { 1 + int(bunniesCount/MAX_BATCH_ELEMENTS)}"
    DrawText(text.encode('utf-8'), 320, 10, 20, MAROON)

    DrawFPS(10, 10)

    EndDrawing()
    #//----------------------------------------------------------------------------------


#// De-Initialization
#//--------------------------------------------------------------------------------------


UnloadTexture(texBunny);   #Unload bunny texture

CloseWindow()              # Close window and OpenGL context
#//--------------------------------------------------------------------------------------

