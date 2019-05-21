"""
This is an attempt at a CFFI dynamic (ABI) binding.  However, it fails to work in the same place the ctypes binding fails, accessing
materials of a model, because Python can't dynamically tell the difference between a pointer and an array. There's probably
some way to specify this (e.g. in raylib_modified.h) but it's difficult to be sure we fixed them all, and the errors
are often completely silent.
"""
import pathlib
MODULE = pathlib.Path(__file__).parent
print(MODULE)

from raylib.dynamic_binding import ffi, raylib as rl
from raylib.colors import *

rl.InitWindow(800,450,b"foo")
rl.SetTargetFPS(60)



camera = ffi.new("struct Camera3D *",  [[ 18.0, 16.0, 18.0 ], [ 0.0, 0.0, 0.0 ], [ 0.0, 1.0, 0.0 ], 45.0, 0 ])

imageFile = str(MODULE / "examples/models/resources/heightmap.png").encode('utf-8')
image = rl.LoadImage(imageFile)            # Load heightmap image (RAM)
print(image)
texture = rl.LoadTextureFromImage(image)                # Convert image to texture (VRAM)

mesh = rl.GenMeshHeightmap(image, [ 16, 8, 16 ])   # Generate heightmap mesh (RAM and VRAM)

print(mesh)

model = rl.LoadModelFromMesh(mesh)                          # Load model from generated mesh

print(model.materials) # SHOULD BE A pointer to a 'struct Material' but instead is NULL pointer to 'Material'

#model.materials[0].maps[rl.MAP_DIFFUSE].texture = texture        # Set map diffuse texture
mapPosition = ( -8.0, 0.0, -8.0 )                # Define model position

rl.UnloadImage(image)                    # Unload heightmap image from RAM, already uploaded to VRAM

rl.SetCameraMode(camera[0], rl.CAMERA_ORBITAL) # Set an orbital camera mode


while not rl.WindowShouldClose():
    rl.UpdateCamera(camera)
    rl.BeginDrawing()
    rl.ClearBackground(RAYWHITE)
    rl.BeginMode3D(camera[0])
    rl.DrawModel(model, mapPosition, 1.0, RED)
    rl.DrawGrid(20, 1.0)
    rl.EndMode3D()
    rl.DrawText(b"sdfsdf", 190, 200, 20, BLACK)
    rl.EndDrawing()
rl.CloseWindow()