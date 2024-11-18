#type: ignore
import raylib as rl
from raylib.colors import *

screenWidth = 1260
screenHeight = 768

rl.InitWindow(screenWidth, screenHeight, b'Skymap Demo')

camera = rl.ffi.new('struct Camera3D *', [[1, 1, 1], [4, 1, 4], [0, 1, 0], 70, 0])

cube = rl.GenMeshCube(100, 100, 100)
skybox = rl.LoadModelFromMesh(cube)

skybox.materials[0].shader = rl.LoadShader(
	b'resources/shaders/skybox.vs',
	b'resources/shaders/skybox.fs'
)

rl.SetShaderValue(
	skybox.materials[0].shader,
	rl.GetShaderLocation(skybox.materials[0].shader, b"environmentMap"),
	rl.ffi.new('int[]', [rl.MATERIAL_MAP_CUBEMAP]),
	rl.RL_SHADER_UNIFORM_INT
)

shdrCubemap = rl.LoadShader(
	b'resources/shaders/cubemap.vs',
	b'resources/shaders/cubemap.fs'
)

rl.SetShaderValue(
	shdrCubemap,
	rl.GetShaderLocation(shdrCubemap, b'equirectangularMap'),
	rl.ffi.new('int[]', [0]),
	rl.SHADER_UNIFORM_INT
)

texHDR = rl.LoadTexture(b'resources/dresden_square.hdr')

# THIS FUNCTION NO LONGER EXISTS, will require porting a lot of C code from the C example to replace it
skybox.materials[0].maps[rl.MAP_CUBEMAP].texture = rl.GenTextureCubemap(shdrCubemap, texHDR, 512, rl.UNCOMPRESSED_R32G32B32)


rl.UnloadTexture(texHDR)
rl.UnloadShader(shdrCubemap)

rl.SetTargetFPS(60)

while not rl.WindowShouldClose():
	rl.UpdateCamera(camera, rl.CAMERA_FIRST_PERSON)
	rl.BeginDrawing()
	rl.ClearBackground(RAYWHITE)
	rl.BeginMode3D(camera[0])
	rl.DrawModel(skybox, [0, 0, 0], 1.0, WHITE)
	rl.DrawGrid(10, 1.0)
	for x in range(10):
		for y in range(10):
			rl.DrawCube([x * 2, 0, y * 2], 1, 1, 1, MAROON)
			rl.DrawCubeWires([x * 2, 0, y * 2], 1, 1, 1, RED)
	rl.EndMode3D()
	rl.DrawFPS(10, 10)
	rl.EndDrawing()

rl.CloseWindow()
rl.UnloadShader(skybox.materials[0].shader)
rl.UnloadTexture(skybox.materials[0].maps[rl.MAP_CUBEMAP].texture)
rl.UnloadModel(skybox)
