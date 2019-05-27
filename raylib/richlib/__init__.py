""" Richlib, simple access to Raylib
"""
__version__ = '0.1'

from ..static import ffi, rl
#from ..dynamic import ffi, raylib as rl
from ..colors import *

import sys

data_dir = ""

camera = ffi.new("struct Camera3D *")
camera.position = (0.0, 100, 100)
camera.target = (0.0, 0.0, 0.0)
camera.up = (0, 1, 0)
camera.fovy = 45
camera.type = rl.CAMERA_PERSPECTIVE

mod = sys.modules['__main__']


class Vector(list):
    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

    @property
    def z(self):
        return self[2]

    @z.setter
    def z(self, value):
        self[2] = value

    @property
    def w(self):
        return self[3]

    @w.setter
    def w(self, value):
        self[3] = value

class Color(list):
    def __init__(self, s):
        if isinstance(s, str):
            super().__init__(globals()[s.upper()])
        else:
            super().__init__(s)
        if len(self) == 3:
            self.append(255)

    @property
    def r(self):
        return self[0]

    @r.setter
    def r(self, value):
        self[0] = value

    @property
    def g(self):
        return self[1]

    @g.setter
    def g(self, value):
        self[1] = value

    @property
    def b(self):
        return self[2]

    @b.setter
    def b(self, value):
        self[2] = value

    @property
    def a(self):
        return self[3]

    @a.setter
    def a(self, value):
        self[3] = value


def clear(color=BLACK):
    rl.ClearBackground(Color(color))


class Shape:
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = Color(value)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = Vector(value)

    @property
    def wire_color(self):
        return self._wire_color

    @wire_color.setter
    def wire_color(self, value):
        self._wire_color =  Color(value)

    @property
    def x(self):
        return self.pos.x

    @x.setter
    def x(self, value):
        self.pos.x = value

    @property
    def y(self):
        return self.pos.y

    @y.setter
    def y(self, value):
        self.pos.y = value

    @property
    def z(self):
        return self.pos.z

    @z.setter
    def z(self, value):
        self.pos.z = value


class Box(Shape):
    def __init__(self, position, size, color=RED, wires=True, wire_color=DARKGRAY):
        self.pos = position
        self.size = size
        self.color = color
        self.wire_color = wire_color
        self.wires = wires

    # def __getattr__(self, item):
    #     return self.pos.item
    #
    # def __setattr__(self, key, value):
    #     self.pos.key = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        print("setting size ", value, type(value))
        self._size = Vector(value)

    def get_bounding_box(self):
        return (
            (
                self.pos.x - self.size.x / 2,
                self.pos.y - self.size.y / 2,
                self.pos.z - self.size.z / 2,
            ),
            (
                self.pos.x + self.size.x / 2,
                self.pos.y + self.size.y / 2,
                self.pos.z + self.size.z / 2,
            )
        )

    def draw(self):
        #print("draw color ",self.color)
        rl.DrawCubeV(self.pos, self.size, self.color)
        if self.wires:
            rl.DrawCubeWiresV(
                self.pos, self.size, self.wire_color
            )

    def check_collision(self, other):
        if isinstance(other, Sphere):
            r = rl.CheckCollisionBoxSphere(
                self.get_bounding_box(), other.pos, other.radius
            )
            return r
        elif isinstance(other, Box):
            return rl.CheckCollisionBoxes(self.get_bounding_box(), other.get_bounding_box())
        elif isinstance(other, Actor):
            return self.check_collision(other.collision_sphere)


class Sphere(Shape):
    def __init__(self, position, radius, color=RED, wires=True, wire_color=DARKGRAY):
        self.pos = position
        self.radius = radius
        self.color = color
        self.wire_color = wire_color
        self.wires = wires

    def draw(self):
        rl.DrawSphere(self.pos, self.radius, self.color)
        if self.wires:
            rl.DrawSphereWires(self.pos, self.radius, 32, 32, self.wire_color)

    def check_collision(self, other):
        if isinstance(other, Sphere):
            return rl.CheckCollisionSpheres(
                self.pos, self.radius, other.pos, other.radius
            )
        elif isinstance(other, Box):
            return rl.CheckCollisionBoxSphere(
                other.get_bounding_box(), self.pos, self.radius
            )
        elif isinstance(other, Actor):
            return self.check_collision(other.collision_sphere)


class Actor(Shape):
    def __init__(self, model_file, position=Vector([0, 0, 0]), collision_radius=1, texture_file="",
                 rotation_axis=Vector([0, 1, 0]), rotation_angle=0, scale=Vector([1, 1, 1]), color=WHITE, wires=False,
                 wire_color=DARKGRAY):
        #super().__init__(position, collision_radius, color, wires, wire_color)

        self.pos = position
        self.color = color
        self.wire_color = wire_color
        self.wires = wires

        self.model_file = model_file
        if texture_file == "":
            texture_file = model_file + "_diffuse"
        self.texture_file = texture_file
        self.scale = scale
        self.rotation_axis = rotation_axis
        self.rotation_angle = rotation_angle
        self.collision_radius = collision_radius
        self.collision_sphere = Sphere(position, collision_radius, RED)

        self.loaded = False

    def load_data(self):
        self.loaded = True
        print("*** DATA_DIR=", data_dir)
        self.model = rl.LoadModel((data_dir + self.model_file + '.obj').encode('utf-8'))
        texture = rl.LoadTexture((data_dir + self.texture_file + '.png').encode('utf-8'))
        self.model.materials[0].maps[rl.MAP_DIFFUSE].texture = texture

    def calc_bounding_box(self):
        bb = rl.MeshBoundingBox(self.model.meshes[0])

        bb.min.x *= self.scale.x
        bb.min.y *= self.scale.y
        bb.min.z *= self.scale.z
        bb.max.x *= self.scale.x
        bb.max.y *= self.scale.y
        bb.max.z *= self.scale.z

        bb.min.x += self.pos.x
        bb.min.y += self.pos.y
        bb.min.z += self.pos.z
        bb.max.x += self.pos.x
        bb.max.y += self.pos.y
        bb.max.z += self.pos.z
        return bb

    def calc_collision_sphere(self):
        centre_x = (self.bounding_box.max.x + self.bounding_box.min.x)/2
        centre_y = (self.bounding_box.max.y + self.bounding_box.min.y)/2
        centre_z = (self.bounding_box.max.z + self.bounding_box.min.z)/2
        sphere = Sphere((centre_x, centre_y, centre_z), self.collision_radius, RED)
        return sphere

    def draw(self):
        if not self.loaded:
            self.load_data()
        self.bounding_box = self.calc_bounding_box()
        self.collision_sphere = self.calc_collision_sphere()
        rl.DrawModelEx(self.model, self.pos, self.rotation_axis, self.rotation_angle, self.scale, self.color)
        if self.wires:
            rl.DrawBoundingBox(self.bounding_box, self.wire_color)
            self.collision_sphere.draw()

    def check_collision(self, other):
        return self.collision_sphere.check_collision(other)

def run():
    screen_width = 800
    screen_height = 450
    title = "RayLibPyZero"

    if hasattr(mod, "WIDTH"):
        screen_width = mod.WIDTH

    if hasattr(mod, "HEIGHT"):
        screen_height = mod.HEIGHT

    if hasattr(mod, "TITLE"):
        title = mod.TITLE

    if hasattr(mod, "DATA_DIR"):
        global data_dir
        data_dir = mod.DATA_DIR

    rl.SetConfigFlags(rl.FLAG_VSYNC_HINT + rl.FLAG_MSAA_4X_HINT)

    rl.InitWindow(screen_width, screen_height, title.encode('utf-8'))

    rl.SetTargetFPS(60)

    if hasattr(mod, "CAMERA"):
        rl.SetCameraMode(camera[0], mod.CAMERA)

    if hasattr(mod, "init"):
        mod.init()

    while not rl.WindowShouldClose():
        if hasattr(mod, "update"):
            mod.update()
        rl.UpdateCamera(camera)
        if rl.IsKeyPressed(rl.KEY_F):
            rl.ToggleFullscreen()
        if rl.IsKeyPressed(rl.KEY_ESCAPE):
            rl.Exit()
        rl.BeginDrawing()
        if hasattr(mod, "draw2dbackground"):
            mod.draw2dbackground()
        rl.BeginMode3D(camera[0])
        if hasattr(mod, "draw3d"):
            mod.draw3d()
        rl.EndMode3D()
        if hasattr(mod, "draw2d"):
            mod.draw2d()
        if hasattr(mod, "draw"):
            mod.draw()
        rl.EndDrawing()
    rl.CloseWindow()


class Keyboard:
    def __getattr__(self, kname):
        # return is a reserved word, so alias enter to return
        if kname == 'enter':
            kname = 'return'
        kname = kname.upper()
        if not kname.startswith("KEY_"):
            kname = "KEY_" + kname

        return rl.IsKeyDown(getattr(rl, kname))


keyboard = Keyboard()
