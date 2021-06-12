"""
This shows how to use the CFFI static (API) binding.  It should be fast and code be as close as possible to original
C code.
"""

from raylib.static import *

InitWindow(800, 450, b"Raylib static texture test")
SetTargetFPS(60)

camera = ffi.new("struct Camera3D *", [[18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0])
image = LoadImage(b"examples/models/resources/heightmap.png")
texture = LoadTextureFromImage(image)
mesh = GenMeshHeightmap(image, (16, 8, 16))
model = LoadModelFromMesh(mesh)
model.materials.maps[MATERIAL_MAP_DIFFUSE].texture = texture

UnloadImage(image)
SetCameraMode(camera[0], CAMERA_ORBITAL)

while not WindowShouldClose():
    UpdateCamera(camera)
    BeginDrawing()
    ClearBackground(RAYWHITE)
    BeginMode3D(camera[0])
    DrawModel(model, (-8.0, 0.0, -8.0), 1.0, RED)
    DrawGrid(20, 1.0)
    EndMode3D()
    DrawText(b"This mesh should be textured", 190, 200, 20, VIOLET)
    EndDrawing()
CloseWindow()
