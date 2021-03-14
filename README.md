# Python Bindings for Raylib 3.5

New CFFI API static bindings.  Faster, fewer bugs and easier to maintain than ctypes.

### Advert

[RetroWar: 8-bit Party Battle](https://store.steampowered.com/app/664240/RetroWar_8bit_Party_Battle/?git) is out now.  Defeat up to 15 of your friends in a tournament of 80s-inspired retro mini games.

# Install

## Option 1: Install from Pypi (easiest but currently out of date, Raylib 2.6 and Python 3.6 - 3.8)

**Windows 10 (64 bit): Python 3.6 - 3.8**

**MacOS: Python 3.6 - 3.8**

**Linux (Ubuntu 16.04+): Python 3.6 - 3.8**

We distribute a statically linked Raylib library,  install from Pypi.

    pip3 install raylib

## Option 2: Install from github (Raylib 3.5, Python 3.6 - 3.9, Linux, awaiting builds for other platforms)
    
The version on Pypi may not always be up to date.  If you want to test the latest version,
clone the git repo and make a symlink to the `raylib` directory in your current project directory.

## Option 3: Build from source (Raylib 3.5, all platforms)

If you're using a platform we dont have binary builds for yet
then you can either *use the dynamic binding with your own dll* or else you will have to build from source.
If you do build on a new platform please
submit your binaries as a PR.

These instructions have been tested on Ubuntu 20.10 and 16.04.  Mac should be very similar.  Windows is probably different.

Clone this repo including submodules so you get correct version of Raylib.

    git clone --recurse-submodules https://github.com/electronstudio/raylib-python-cffi

Build and install Raylib from the raylib-c directory.

    cd raylib-python-cffi/raylib-c
    mkdir build
    cd build
    cmake -DWITH_PIC=on -DSTATIC=on -DSHARED=on ..
    sudo make install

Make a patched version of raylib header.

    cd ../../raylib
    cp raylib.h raylib_modified.h
    patch  -p0 <raylib_modified.h.patch

Build 

    cd static
    pip3 install cffi
    python3 build_linux.py
    
To build a complete set of libs for Python 3.6, 3.7, 3.8 and 3.9:

    ./build_linux_multi.sh
    
To update the Linux dynamic libs (names will be different on other platfroms):

    cd ../..
    rm raylib/dynamic/*.so*
    cp -P /usr/local/lib/libraylib.so* raylib/dynamic/

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
    BeginMode3D(camera[0])
    DrawGrid(20, 1.0)
    EndMode3D()
    DrawText(b"Hellow World", 190, 200, 20, VIOLET)
    EndDrawing()
CloseWindow()

```

## raylib.pyray

Wrapper around the static bindings.  Makes the names snakecase and converts strings to bytes automatically.  See test_pyray.py.


```
from raylib.pyray import PyRay
from raylib.colors import *

pyray = PyRay()

pyray.init_window(800, 450, "Hello Pyray")
pyray.set_target_fps(60)

camera = pyray.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
pyray.set_camera_mode(camera, pyray.CAMERA_ORBITAL)

while not pyray.window_should_close():
    pyray.update_camera(camera)
    pyray.begin_drawing()
    pyray.clear_background(RAYWHITE)
    pyray.begin_mode_3d(camera)
    pyray.draw_grid(20, 1.0)
    pyray.end_mode_3d()
    pyray.draw_text("Hello world", 190, 200, 20, VIOLET)
    pyray.end_drawing()
pyray.close_window()

```

## raylib.dynamic

In addition to the API static bindings we have CFFI ABI dynamic bindings in order to avoid the need to compile a C extension module.
There have been some weird failures with dynamic bindings and ctypes bindings before and often the failures are silent
so you dont even know.  Also the static bindings should be faster.  Therefore I recommend the static ones...

BUT the dynamic bindings have the big advantage that you don't need to compile anything to install.  You just need a Raylib DLL,
which we supply for Windows/Mac/Linux.

See test_dynamic.py for how to use.

## richlib

[A simplified API for Raylib for use in education and to enable beginners to create 3d games](https://github.com/electronstudio/richlib)

# HELP WANTED

 * converting more examples from C to python
 * testing and building on more platforms
 * sorting out binary wheel distribution for Mac/Win and compile-from-source distributtion for Linux
 
