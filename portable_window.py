from raylib import *
import pyray as pr

screenWidth = 800
screenHeight = 600

SetConfigFlags(FLAG_WINDOW_UNDECORATED)
InitWindow(screenWidth, screenHeight, b"raygui - portable window")


mousePosition = pr.Vector2(0, 0)
windowPosition = pr.Vector2(500, 200 )
panOffset = mousePosition
dragWindow = False

SetWindowPosition(int(windowPosition.x), int(windowPosition.y))

exitWindow = False

SetTargetFPS(60)


while not exitWindow and not WindowShouldClose():

    mousePosition = GetMousePosition()

    if IsMouseButtonPressed(MOUSE_LEFT_BUTTON):
        if CheckCollisionPointRec(mousePosition,  pr.Rectangle(0, 0, screenWidth, 20) ):
            dragWindow = True
            panOffset = mousePosition



    if (dragWindow):
        windowPosition.x += (mousePosition.x - panOffset.x)
        windowPosition.y += (mousePosition.y - panOffset.y)
        if IsMouseButtonReleased(MOUSE_LEFT_BUTTON):
            dragWindow = False

        SetWindowPosition(int(windowPosition.x), int(windowPosition.y))


    BeginDrawing()
    ClearBackground(RAYWHITE)
    exitWindow = GuiWindowBox(pr.Rectangle(0, 0, screenWidth, screenHeight) , b"#198# PORTABLE WINDOW")
    pr.draw_text(f"Mouse Position: {mousePosition.x} {mousePosition.y}", 10, 40, 10, DARKGRAY)
    EndDrawing()

CloseWindow()