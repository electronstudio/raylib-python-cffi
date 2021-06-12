"""
This shows how to use the CFFI dynamic (ABI) binding.  Note that is slower and more likely to run into silent errors and segfaults.
But it doesnt require any C compiler to build.
"""
from raylib.dynamic import ffi, raylib as rl
from raylib.colors import *

rl.InitWindow(800, 450, b"Raylib dynamic binding test")
rl.SetTargetFPS(60)

camera = ffi.new("struct Camera3D *", [[18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0])
image = rl.LoadImage(b"examples/models/resources/heightmap.png")
texture = rl.LoadTextureFromImage(image)
mesh = rl.GenMeshHeightmap(image, [16, 8, 16])
model = rl.LoadModelFromMesh(mesh)
print(model.materials)  # SHOULD BE A pointer to a 'struct Material' but some is NULL pointer to 'Material' ?
model.materials.maps[rl.MATERIAL_MAP_DIFFUSE].texture = texture

rl.UnloadImage(image)
rl.SetCameraMode(camera[0], rl.CAMERA_ORBITAL)

while not rl.WindowShouldClose():
    rl.UpdateCamera(camera)
    rl.BeginDrawing()
    rl.ClearBackground(RAYWHITE)
    rl.BeginMode3D(camera[0])
    rl.DrawModel(model, (-8.0, 0.0, -8.0), 1.0, RED)
    rl.DrawGrid(20, 1.0)
    rl.EndMode3D()
    rl.DrawText(b"This mesh should be textured", 190, 200, 20, VIOLET)
    rl.EndDrawing()
rl.CloseWindow()

"""
Previously this failed to work in the same place the ctypes binding fails, accessing
materials of a model.  I though it was because Python can't dynamically tell the difference between a pointer and an array.
"""
