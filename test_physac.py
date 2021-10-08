from raylib import *

screenWidth = 800
screenHeight = 450

SetConfigFlags(FLAG_MSAA_4X_HINT)
InitWindow(screenWidth, screenHeight, b"[physac] Basic demo")


logoX = screenWidth - MeasureText(b"Physac", 30) - 10
logoY = 15


InitPhysics()


floor = CreatePhysicsBodyRectangle([screenWidth/2, screenHeight ], 500, 100, 10)
floor.enabled = False


circle = CreatePhysicsBodyCircle([screenWidth/2, screenHeight/2], 45, 10)
circle.enabled = False

SetTargetFPS(60)

while not WindowShouldClose():

    UpdatePhysics();

    if IsMouseButtonPressed(MOUSE_LEFT_BUTTON):
        body = CreatePhysicsBodyPolygon(GetMousePosition(), GetRandomValue(20, 80), GetRandomValue(3, 8), 10)

    elif IsMouseButtonPressed(MOUSE_RIGHT_BUTTON):
        CreatePhysicsBodyCircle(GetMousePosition(), GetRandomValue(10, 45), 10)


    bodiesCount = GetPhysicsBodiesCount()
    for i in range(bodiesCount):
        body = GetPhysicsBody(i)
        if body and (body.position.y > screenHeight*2):
            DestroyPhysicsBody(body)


    BeginDrawing()
    ClearBackground(BLACK)
    DrawFPS(screenWidth - 90, screenHeight - 30)


    bodiesCount = GetPhysicsBodiesCount()
    for i in range(bodiesCount):
        body = GetPhysicsBody(i)
        if body:
            vertexCount = GetPhysicsShapeVerticesCount(i)
            for j in range(vertexCount):
                vertexA = GetPhysicsShapeVertex(body, j)
                jj = j + 1 if (j + 1) < vertexCount else 0
                vertexB = GetPhysicsShapeVertex(body, jj)
                DrawLineV(vertexA, vertexB, GREEN)

    DrawText(b"Left mouse button to create a polygon", 10, 10, 10, WHITE)
    DrawText(b"Right mouse button to create a circle", 10, 25, 10, WHITE)

    DrawText(b"Physac", logoX, logoY, 30, WHITE)
    DrawText(b"Powered by", logoX + 50, logoY - 7, 10, WHITE)

    EndDrawing()

ClosePhysics()

CloseWindow()