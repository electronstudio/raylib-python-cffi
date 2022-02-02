"""
RenderTexture example

Run with:

python3 flow-field
        flow-field bees
"""

import sys, math, time, random
import glm
from raylib import rl, ffi
from raylib.colors import *

CTM = lambda: round(time.time() * 1000)



BEES = bool(sys.argv[1:])




rl.SetTraceLogLevel(rl.LOG_ERROR)
rl.SetConfigFlags(rl.FLAG_WINDOW_RESIZABLE)
rl.InitWindow(512, 512, b'Friendly Bees')
rl.SetTargetFPS(60)
#rl.DisableCursor()

canvas = rl.LoadRenderTexture(rl.GetScreenWidth(), rl.GetScreenHeight())
rl.SetTextureWrap(canvas.texture, rl.WRAP_MIRROR_REPEAT)

def random_point_in_circle(center, radius):
    a = random.random() * 2 * math.pi
    r = radius * math.sqrt(random.random())
    x = r * math.cos(a)
    z = r * math.sin(a)
    return glm.vec3(
        x + center.x,
        center.y,
        z + center.z
    )

class Particle:
    def __init__(self, pos):
        self.pos = pos
        self.scl = 16 if BEES else 2
        self.ang = math.radians(random.randint(0, 359))
        self.spd = random.randint(4, 10)
        self.start = CTM()
        self.clr = [255, 200, 0, 155] if BEES else [*(random.randint(55, 255) for i in range(3)), 55]
        self.mem = (0, 0)
        self.pre = glm.vec2(pos)

    def process(self):
        if CTM() > self.start + 50:
            self.ang = math.radians(glm.simplex(self.pos) * 360.0)
            self.start = CTM()
    
        self.rot = glm.vec2(
            glm.vec4(1) * glm.rotate(glm.mat4(), self.ang, [0, 0, 1])
        )
        self.pre = int(self.pos.x), int(self.pos.y)
        self.pos += self.rot * rl.GetFrameTime() * 64
        rl.DrawLine(
            int(self.pos.x), int(self.pos.y), *self.pre, self.clr
        )

        if self.pos.x < 0: self.pos.x = rl.GetScreenWidth() - 1
        if self.pos.y < 0: self.pos.y = rl.GetScreenHeight() - 1
        if self.pos.x >= rl.GetScreenWidth(): self.pos.x = 0
        if self.pos.y >= rl.GetScreenHeight(): self.pos.y = 0

        hlf = self.scl // 2
        self.mem = int(self.pos.x) - hlf, int(self.pos.y) - hlf
        rl.DrawRectangle(
            *self.mem,
            self.scl if not BEES else hlf,
            self.scl,
            self.clr
        )
        if BEES:
            rl.DrawRectangle(
                self.mem[0] + hlf, self.mem[1],
                hlf,
                self.scl,
                [0, 0, 0, 55]
            )

dims = rl.GetScreenWidth(), rl.GetScreenHeight()
ini = False
parts = [
    Particle(glm.vec2(random_point_in_circle(
        glm.vec3(
            rl.GetScreenWidth() / 2,
            rl.GetScreenHeight() / 2,
            0
        ),
        64
    )))
    for i in range(125)
]
while not rl.WindowShouldClose():
    if (rl.GetScreenWidth(), rl.GetScreenHeight()) != dims:
        canvas = rl.LoadRenderTexture(rl.GetScreenWidth(), rl.GetScreenHeight())
        rl.SetTextureWrap(canvas.texture, rl.WRAP_MIRROR_REPEAT)
        ini = False
        dims = rl.GetScreenWidth(), rl.GetScreenHeight()

    rl.BeginDrawing()

    rl.BeginTextureMode(canvas)
    if not ini:
        rl.ClearBackground([200, 200, 0, 255] if BEES else WHITE)
        if BEES:
            rl.DrawRectangle(
                0, 0,
                dims[0], dims[1] // 2,
                (0, 200, 255, 255)
            )
            rl.DrawCircle(
                dims[0] - 72, 72, 32, [255, 200, 0, 255]
            )
        else:
            ini = True

    for part in parts: part.process()

    rl.EndTextureMode()

    tex = canvas.texture
    rl.DrawTexturePro(
        tex, [0.0, 0.0, tex.width, -tex.height],
        [0, 0, tex.width, tex.height],
        [0, 0], 0.0, WHITE
    )

    rl.EndDrawing()

rl.CloseWindow()
