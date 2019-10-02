"""
Example converted to Python from:
http://bedroomcoders.co.uk/raylib-fog/
"""

from raylib.dynamic import raylib as rl, ffi
from raylib.colors import *

rl.SetConfigFlags(rl.FLAG_MSAA_4X_HINT | rl.FLAG_WINDOW_RESIZABLE)
rl.InitWindow(1280, 768, b'Fog Test')

camera = ffi.new('struct Camera3D *', [
	[2, 2, 6],
	[0, 5, 0],
	[0, 1, 0],
	45,
	rl.CAMERA_PERSPECTIVE
])

model = rl.LoadModelFromMesh(rl.GenMeshTorus(0.4, 1, 16, 32))
model2 = rl.LoadModelFromMesh(rl.GenMeshCube(1, 1, 1))
model3 = rl.LoadModelFromMesh(rl.GenMeshSphere(0.5, 32, 32))

texture = rl.LoadTexture(b'resources/test.png')

model.materials[0].maps[rl.MAP_DIFFUSE].texture = texture
model2.materials[0].maps[rl.MAP_DIFFUSE].texture = texture
model3.materials[0].maps[rl.MAP_DIFFUSE].texture = texture

shader = rl.LoadShader(b'resources/shaders/fogLight.vs', b'resources/shaders/fogLight.fs')
shader.locs[rl.LOC_MATRIX_MODEL] = rl.GetShaderLocation(shader, b'matModel')
shader.locs[rl.LOC_VECTOR_VIEW] = rl.GetShaderLocation(shader, b'viewPos')

amb = rl.GetShaderLocation(shader, b'ambient')
rl.SetShaderValue(shader, amb, ffi.new('float[]', [0.2, 0.2, 0.2, 1.0]), rl.UNIFORM_VEC4)

fog_color = [0.2, 0.2, 1.0, 1.0]
fogC = rl.GetShaderLocation(shader, b'fogColor')
rl.SetShaderValue(shader, fogC, ffi.new('float[]', fog_color), rl.UNIFORM_VEC4)

fogD = rl.GetShaderLocation(shader, b'FogDensity')
fogDensity = 0.12
rl.SetShaderValue(shader, fogD, ffi.new('float[]', [fogDensity]), rl.UNIFORM_FLOAT)


model.materials[0].shader = shader
model2.materials[0].shader = shader
model3.materials[0].shader = shader

rl.SetCameraMode(camera[0], rl.CAMERA_ORBITAL)
rl.SetTargetFPS(60)

while not rl.WindowShouldClose():
	rl.UpdateCamera(camera)

	if rl.IsKeyDown(rl.KEY_UP):
		fogDensity = min(fogDensity + 0.001, 1)

	if rl.IsKeyDown(rl.KEY_DOWN):
		fogDensity = max(fogDensity - 0.001, 0)

	rl.SetShaderValue(shader, fogD, ffi.new('float[]', [fogDensity]), rl.UNIFORM_FLOAT)

	rl.SetShaderValue(shader, shader.locs[rl.LOC_VECTOR_VIEW], ffi.new('float[]', [camera.position.x]), rl.UNIFORM_VEC3)

	rl.BeginDrawing()

	rl.ClearBackground([int(255 * i) for i in fog_color])

	rl.BeginMode3D(camera[0])
	rl.DrawModel(model, [0] * 3, 1, WHITE)
	rl.DrawModel(model2, [-2.6, 0, 0], 1, WHITE)
	rl.DrawModel(model3, [ 2.6, 0, 0], 1, WHITE)

	for i in range(-20, 20, 2):
		rl.DrawModel(model, [i, 0, 2], 1, WHITE)


	rl.DrawGizmo([1000, 1000, 1000])

	rl.EndMode3D()

	rl.DrawFPS(10, 10)
	rl.DrawText(f'Up/Down to change fog density: {fogDensity}'.encode('utf-8'), 10, 30, 20, WHITE)

	rl.EndDrawing()


rl.CloseWindow()
rl.UnloadModel(model)
rl.UnloadModel(model2)
rl.UnloadModel(model3)
rl.UnloadTexture(texture)
rl.UnloadShader(shader)
