# Python Bindings for Raylib 2.5

New CFFI API static bindings.  Faster, fewer bugs and easier to maintain than ctypes.

# Install

**Windows 10 (64 bit): Python 3.6 - 3.7**

**MacOS: Python 3.5 - 3.7**

We distribute a statically linked Raylib library,  install from Pypi.

    pip3 install raylib

If you're using **Linux**, or a different version of Python, or maybe Windows/Mac with incompatible libraries
then you can either *use the dynamic binding only* or else you will have to build from source.  Download, compile
and install Raylib 2.5 then

    cd raylib/static
    python3 build_linux.py

# Use

## raylib.static

Goal is make usage as similar to the original C as CFFI will allow.  There are a few differences
you can see in the examples.  See test_static.py and examples/*.py for how to use.

```
from raylib.static import *

InitWindow(800, 450, b"Hello Raylib")
SetTargetFPS(60)

camera = ffi.new("struct Camera3D *", [[18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0])
SetCameraMode(camera[0], CAMERA_ORBITAL)

while not WindowShouldClose():
    UpdateCamera(camera)
    BeginDrawing()
    ClearBackground(RAYWHITE)
    DrawText(b"Hellow World", 190, 200, 20, VIOLET)
    EndDrawing()
CloseWindow()

```

## raylib.dynamic

In addition to the API static bindings we have CFFI ABI dynamic bindings in order to avoid the need to compile a C extension module.
There have been some weird failures with dynamic bindings and ctypes bindings before and often the failures are silent
so you dont even know.  Also the static bindings should be faster.  Therefore I recommend the static ones...

BUT the dynamic bindings have the big advantage that you don't need to compile anything to install.  You just need a Raylib DLL,
which we supply for Windows/Mac/Linux.

See test_dynamic.py for how to use.

## raylib.static.pyray

Wrapper around the static bindings.  Makes the names snakecase and converts strings to bytes automatically.  See test_pyray.py.


```
from raylib.static.pyray import pyray as prl
from raylib.colors import *

prl.init_window(800, 450, "Hello Pyray")
prl.set_target_fps(60)

camera = prl.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
image = prl.load_image("examples/models/resources/heightmap.png")
prl.set_camera_mode(camera, prl.CAMERA_ORBITAL)

while not prl.window_should_close():
    prl.update_camera(prl.pointer(camera))
    prl.begin_drawing()
    prl.clear_background(RAYWHITE)
    prl.draw_text("Hello world", 190, 200, 20, VIOLET)
    prl.end_drawing()
prl.close_window()

```

## raylib.richlib

A very easy to use library on top of static bindings, modelled after Pygame Zero.

# Platforms tested

 * MacOS 10.12.6 - Python 3.7
 * Ubuntu 18.04 LTS - Python 3.6
 * Windows 10 (64 bit) - Python 3.7

# HELP WANTED

 * converting more examples from C to python
 * testing and building on more platforms
 * sorting out binary wheel distribution for Mac/Win and compile-from-source distributtion for Linux
 
