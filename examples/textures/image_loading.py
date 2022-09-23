from raylib import *

screenWidth = 800
screenHeight = 450

InitWindow(screenWidth, screenHeight, b"raylib [textures] example - image loading")

image = LoadImage(b"resources/raylib_logo.png")
texture = LoadTextureFromImage(image)

UnloadImage(image)

while not WindowShouldClose():

    BeginDrawing()

    ClearBackground(RAYWHITE)

    DrawTexture(texture, int(screenWidth/2 - texture.width/2), int(screenHeight/2 - texture.height/2), WHITE)

    DrawText(b"this IS a texture loaded from an image!", 300, 370, 10, GRAY)

    EndDrawing()

UnloadTexture(texture)

CloseWindow()               
