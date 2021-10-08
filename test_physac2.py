from raylib import *

VELOCITY  = 0.5

screenWidth = 800
screenHeight = 450

SetConfigFlags(FLAG_MSAA_4X_HINT)
InitWindow(screenWidth, screenHeight, b"[physac] Basic demo")
logoX = screenWidth - MeasureText(b"Physac", 30) - 10
logoY = 15


InitPhysics()

floor = CreatePhysicsBodyRectangle([screenWidth/2, screenHeight ], screenWidth, 100, 10)
platformLeft = CreatePhysicsBodyRectangle([screenWidth*0.25, screenHeight*0.6 ], screenWidth*0.25, 10, 10)
platformRight = CreatePhysicsBodyRectangle([screenWidth*0.75, screenHeight*0.6 ], screenWidth*0.25, 10, 10)
wallLeft = CreatePhysicsBodyRectangle([-5, screenHeight/2 ], 10, screenHeight, 10)
wallRight = CreatePhysicsBodyRectangle([screenWidth + 5, screenHeight/2 ], 10, screenHeight, 10)


floor.enabled = False
platformLeft.enabled = False
platformRight.enabled = False
wallLeft.enabled = False
wallRight.enabled = False


body = CreatePhysicsBodyRectangle([screenWidth/2, screenHeight/2 ], 50, 50, 1)
body.freezeOrient = True  

SetTargetFPS(60)

while not WindowShouldClose():

    UpdatePhysics();

    if IsKeyDown(KEY_RIGHT):
        body.velocity.x = VELOCITY
    elif IsKeyDown(KEY_LEFT):
        body.velocity.x = -VELOCITY


    if IsKeyDown(KEY_UP) and body.isGrounded:
        body.velocity.y = -VELOCITY*4

    BeginDrawing()

    ClearBackground(BLACK)

    DrawFPS(screenWidth - 90, screenHeight - 30)


    bodiesCount = GetPhysicsBodiesCount()
    for i in range(bodiesCount):
        body = GetPhysicsBody(i)
        vertexCount = GetPhysicsShapeVerticesCount(i)
        for j in range(vertexCount):
            vertexA = GetPhysicsShapeVertex(body, j)

            jj = j + 1 if j + 1 < vertexCount else 0
            vertexB = GetPhysicsShapeVertex(body, jj)

            DrawLineV(vertexA, vertexB, GREEN)

    DrawText(b"Use 'ARROWS' to move player", 10, 10, 10, WHITE)

    DrawText(b"Physac", logoX, logoY, 30, WHITE)
    DrawText(b"Powered by", logoX + 50, logoY - 7, 10, WHITE)

    EndDrawing()

ClosePhysics()

CloseWindow()