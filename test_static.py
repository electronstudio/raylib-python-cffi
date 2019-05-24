from raylib.static import *


InitWindow(800,450,b"Raylib texture test")
SetTargetFPS(60)

print(Vector3(1,1,1))

camera = ffi.new("struct Camera3D *",  [[ 18.0, 16.0, 18.0 ], [ 0.0, 0.0, 0.0 ], [ 0.0, 1.0, 0.0 ], 45.0, 0 ])


image = LoadImage(b"examples/models/resources/heightmap.png")            # Load heightmap image (RAM)
print(image)
texture = LoadTextureFromImage(image)                # Convert image to texture (VRAM)

mesh = GenMeshHeightmap(image, ( 16, 8, 16 ))   # Generate heightmap mesh (RAM and VRAM)
print(mesh)
model = LoadModelFromMesh(mesh)                          # Load model from generated mesh

print(model.meshes)
print(model.meshes[1])

print(model.materials)
print(model.materialCount)
print(model.materials[0].maps[rl.MAP_DIFFUSE])

model.materials.maps[MAP_DIFFUSE].texture = texture        # Set map diffuse texture
print(model.materials[0].maps[rl.MAP_DIFFUSE].value)


mapPosition = ( -8.0, 0.0, -8.0 )                # Define model position

UnloadImage(image)                    # Unload heightmap image from RAM, already uploaded to VRAM

SetCameraMode(camera[0], CAMERA_ORBITAL) # Set an orbital camera mode


while not WindowShouldClose():
    UpdateCamera(camera)
    BeginDrawing()
    ClearBackground(RAYWHITE)
    BeginMode3D(camera[0])
    DrawModel(model, mapPosition, 1.0, RED)
    DrawGrid(20, 1.0)
    EndMode3D()
    DrawText(b"This mesh should be textured", 190, 200, 20, VIOLET)
    EndDrawing()
CloseWindow()