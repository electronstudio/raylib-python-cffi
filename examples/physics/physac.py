"""
raylib [physac] example - physics demo
"""

from pyray import Vector2
from raylib import *
from raylib.colors import (
    BLACK,
    GREEN,
    WHITE
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

SetConfigFlags(FLAG_MSAA_4X_HINT)
InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, b'[physac] Basic demo')

InitPhysics()

floor = CreatePhysicsBodyRectangle(Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT), 500, 100, 10)
floor.enabled = False

circle = CreatePhysicsBodyCircle(Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 45, 10)
circle.enabled = False

SetTargetFPS(60)

while not WindowShouldClose():
    # Update
    # ----------------------------------------------------------------------
    UpdatePhysics()  # Update physics system

    if IsKeyPressed(KEY_R):  # Reset physics system
        ResetPhysics()

        floor = CreatePhysicsBodyRectangle(Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT), 500, 100, 10)
        floor.enabled = False

        circle = CreatePhysicsBodyCircle(Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 45, 10)
        circle.enabled = False

    # Physics body creation inputs
    if IsMouseButtonPressed(MOUSE_BUTTON_LEFT):
        CreatePhysicsBodyPolygon(GetMousePosition(), GetRandomValue(20, 80), GetRandomValue(3, 8), 10)
    elif IsMouseButtonPressed(MOUSE_BUTTON_RIGHT):
        CreatePhysicsBodyCircle(GetMousePosition(), GetRandomValue(10, 45), 10)

    # Destroy falling physics bodies
    bodies_count = GetPhysicsBodiesCount()
    for i in reversed(range(bodies_count)):
        body = GetPhysicsBody(i)

        if body and body.position.y > SCREEN_HEIGHT * 2:
            DestroyPhysicsBody(body)
    # ----------------------------------------------------------------------

    # Draw
    # ----------------------------------------------------------------------
    BeginDrawing()

    ClearBackground(BLACK)
    DrawFPS(SCREEN_WIDTH - 90, SCREEN_HEIGHT - 30)

    # Draw created physics bodies
    bodies_count = GetPhysicsBodiesCount()
    for i in range(bodies_count):
        body = GetPhysicsBody(i)

        if body:
            vertex_count = GetPhysicsShapeVerticesCount(i)
            for j in range(vertex_count):
                # Get physics bodies shape vertices to draw lines
                # Note: GetPhysicsShapeVertex() already calculates rotation transformations
                vertexA = GetPhysicsShapeVertex(body, j)

                # Get next vertex or first to close the shape
                jj = (j + 1) if (j+1) < vertex_count else 0
                vertexB = GetPhysicsShapeVertex(body, jj)

                # Draw a line between two vertex positions
                DrawLineV(vertexA, vertexB, GREEN)

    DrawText(b'Left mouse button to create a polygon', 10, 10, 10, WHITE)
    DrawText(b'Right mouse button to create a circle', 10, 25, 10, WHITE)
    DrawText(b"Press 'R' to reset example", 10, 40, 10, WHITE)

    EndDrawing()
    # ----------------------------------------------------------------------

ClosePhysics()
CloseWindow()
