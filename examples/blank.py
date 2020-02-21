from raylib.dynamic import raylib as rl, ffi
from raylib.colors import *
from camera import CameraFly

rl.SetTraceLogLevel(rl.LOG_ERROR)
rl.SetConfigFlags(rl.FLAG_WINDOW_RESIZABLE)
rl.InitWindow(512, 256, b'Test')
rl.SetTargetFPS(60)
rl.DisableCursor()

flycam = CameraFly()


while not rl.WindowShouldClose():
    flycam.update()
    cam = flycam.get_camera()

    rl.BeginDrawing()
    rl.ClearBackground((0, 200, 255, 255))
    rl.BeginMode3D(cam[0])

    # NOTE(pebaz): For whatever reason, this can solve a percentage of artifacts
    rl.DrawGizmo([100000000, 100000000, 100000000])

    rl.DrawGrid(32, 1)

    rl.EndMode3D()
    rl.EndDrawing()

rl.CloseWindow()
