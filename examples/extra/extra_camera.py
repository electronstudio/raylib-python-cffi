# python3 -m pip install pyglm

from math import sin, cos
import glm # type: ignore
from raylib import rl, ffi


class CameraFly:
    def __init__(self, x=0, y=0, z=0, fov=70.0):
        self.last_mouse = ffi.new("struct Vector2 *", [0, 0])
        self.fov = fov
        self.yaw = -46.33
        self.pitch = 0.0
        self.front = glm.vec3()
        self.up = glm.vec3()
        self.right = glm.vec3()
        self.position = glm.vec3(x, y, z)
        self.world_up = glm.vec3(0, 1, 0)
        self.fps_facing = glm.vec3()
        self.movement_speed = 10
        self.mouse_sensitivity = 0.002
        self.last_time = rl.GetFrameTime()

    def get_camera(self):
        return ffi.new(
            "struct Camera3D *",
            [
                self.get_ray_front(),
                self.get_ray_position(),
                self.get_ray_up(),
                self.fov,
                rl.CAMERA_PERSPECTIVE
            ]
        )

    def get_ray_front(self):
        return list(self.position + self.front)
    
    def get_ray_up(self):
        return list(self.up)

    def get_ray_position(self):
        return list(self.position)

    def update_keyboard(self):
        boost = 4 if rl.IsKeyDown(rl.KEY_LEFT_SHIFT) else 1
        velocity = self.movement_speed * boost * rl.GetFrameTime()

        if rl.IsKeyDown(rl.KEY_W):
            self.position = self.position - self.fps_facing * velocity

        if rl.IsKeyDown(rl.KEY_S):
            self.position = self.position + self.fps_facing * velocity

        if rl.IsKeyDown(rl.KEY_D):
            dirr = glm.normalize(glm.cross(self.fps_facing, self.world_up))
            self.position = self.position - dirr * velocity

        if rl.IsKeyDown(rl.KEY_A):
            dirr = glm.normalize(glm.cross(self.fps_facing, self.world_up))
            self.position = self.position + dirr * velocity

        if rl.IsKeyDown(rl.KEY_SPACE):
            self.position = self.position + self.world_up * velocity

        if rl.IsKeyDown(rl.KEY_LEFT_CONTROL) or rl.IsKeyDown(rl.KEY_RIGHT_CONTROL):
            self.position = self.position - self.world_up * velocity

    def update_mouse(self):
        pos = rl.GetMousePosition()
        width = rl.GetScreenWidth()
        height = rl.GetScreenHeight()

        mouse_coordinates = ffi.new("struct Vector2 *", [
            pos.x - self.last_mouse.x,
            pos.y - self.last_mouse.y
        ])

        self.yaw   += mouse_coordinates.x * self.mouse_sensitivity
        self.pitch += (mouse_coordinates.y * self.mouse_sensitivity)
        self.pitch = min(self.pitch, 1.5)
        self.pitch = max(self.pitch, -1.5)
        self.last_mouse = rl.GetMousePosition()

    def update(self):
        # NOTE(pebaz): Comment out these lines to control them in a game loop
        self.update_keyboard()
        self.update_mouse()

        # Update all camera vectors to reflect changes
        self.fps_facing = glm.vec3(
            cos((self.yaw)) * cos((0)),
            sin((0)),
            sin((self.yaw)) * cos((0))
        )
        self.fps_facing = glm.normalize(self.fps_facing)

        front = glm.vec3(
            cos((self.yaw)) * cos((self.pitch)),
            sin((self.pitch)),
            sin((self.yaw)) * cos((self.pitch))
        )

        self.front = glm.normalize(front)
        self.right = glm.normalize(glm.cross(self.front, self.world_up))
        self.up = glm.normalize(glm.cross(self.right, self.front))


def camera_test():
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
        #rl.DrawGizmo([100000000, 100000000, 100000000])

        rl.DrawGrid(32, 1)

        rl.EndMode3D()
        rl.EndDrawing()

    rl.CloseWindow()

if __name__ == '__main__':
    camera_test()