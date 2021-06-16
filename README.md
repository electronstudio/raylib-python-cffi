# Python Bindings for Raylib 3.7

New CFFI API static bindings.  Faster, fewer bugs and easier to maintain than ctypes.

### Advert

[RetroWar: 8-bit Party Battle](https://store.steampowered.com/app/664240/RetroWar_8bit_Party_Battle/?git) is out now.  Defeat up to 15 of your friends in a tournament of 80s-inspired retro mini games.

# Install

## Option 1: Install from Pypi (easiest but may not be up to date or be available for your platform)

We distribute a statically linked binary Raylib library,  install from Pypi.

    pip3 install raylib

Or to force latest version:

    pip3 install raylib==3.7.0

Some platforms that should be available:

**Windows 10 (64 bit): Python 3.7 - 3.9**

**Linux (Ubuntu 16.04+): Python 3.6 - 3.9**

If yours isn't available then pip should attempt to build from source, so you will need to have raylib development libs installed.

## Option 2: Build from source

If you're using a platform we don't have binary builds for yet
then you can either *use the dynamic binding with your own dll* or else you will have to build from source.
If you do build on a new platform please
submit your binaries as a PR.

These instructions have been tested on Ubuntu 20.10 and 16.04.  Mac should be very similar.  Windows is probably different.

Clone this repo including submodules so you get correct version of Raylib.

    git clone --recurse-submodules https://github.com/electronstudio/raylib-python-cffi

### Windows

Open Visual C++ command shell.

Fix the symlink that doesnt work on Windows

    cd raylib-python-cffi
    copy raylib-c\src\raylib.h raylib\raylib.h

Build and install Raylib from the raylib-c directory.

    cd raylib-python-cffi/raylib-c
    mkdir build
    cd build
    cmake -DWITH_PIC=on -DCMAKE_BUILD_TYPE=Release ..
    msbuild ALL_BUILD.vxcproj
    copy raylib\Debug\raylib.lib ..\..
    cd ..\..

To update the dynamic libs, download the official release, e.g. https://github.com/raysan5/raylib/releases/download/3.7.0/raylib-3.7.0_win64_msvc16.zip and extract `raylib.dll`
into `raylib/dynamic`.  Delete the files for other platforms, unless you want them in your distribution. 

To build a binary wheel distribution:

    rmdir /Q /S build
    pip3 install cffi
    pip3 install wheel
    python setup.py bdist_wheel

and install it:

    pip3 install dist\raylib-3.5.0-cp37-cp37m-win_amd64.whl

### Linux etc

Build and install Raylib from the raylib-c directory.

    sudo apt install libasound2-dev mesa-common-dev libx11-dev libxrandr-dev libxi-dev xorg-dev libgl1-mesa-dev libglu1-mesa-dev
    cd raylib-python-cffi/raylib-c
    mkdir build
    cd build
    cmake -DWITH_PIC=on -DCMAKE_BUILD_TYPE=Release ..
    sudo make install

Optional: Build the Raylib shared libs, if you plan to use `raylib.dynamic` binding.

    rm -rf *
    cmake -DWITH_PIC=on -DBUILD_SHARED_LIBS=on -DCMAKE_BUILD_TYPE=Release ..
    sudo make install

Optional: Make a patched version of raylib header.  (Not necessary if you've already got raylib_modifed.h from repo and haven't changed anything.)

    cd ../../raylib
    cp raylib.h raylib_modified.h
    patch  -p0 <raylib_modified.h.patch


Build 

    pip3 install cffi
    cd ..
    rm -rf build raylib/static/_raylib_cffi.*
    python3 raylib/static/build.py
    

To update the Linux dynamic libs (names will be different on other platfroms):

    rm raylib/dynamic/*.so*
    cp -P /usr/local/lib/libraylib.so* raylib/dynamic/

To build a binary wheel distribution:

    pip3 install wheel
    python3 setup.py bdist_wheel

and install it:

    pip3 install dist/raylib*.whl

To build a complete set of libs for Python 3.6, 3.7, 3.8 and 3.9:

    ./raylib/static/build_multi.sh

(NOTE pypi wont accept Linux packages unless they are built `--plat-name manylinux2014_x86_64` so on linux
please run `./raylib/static/build_multi_linux.sh` )

(TODO move the dynamic libs into a separate package rather than include them with every one.)

### Raspberry Pi

The integrated GPU hardware in a Raspberry Pi ("VideoCore") is rather
idiosyncratic, resulting in a complex set of software options. Probably the
most interesting two options for Raylib applications are:

 1. Use the Broadcom proprietary Open GL ES 2.0 drivers, installed by Raspbian
    into `/opt/vc`. These are 32-bit only, and currently X11 doesn't use these
    for its acceleration, so this is most suitable for driving the entire HDMI
    output from one application with minimal overhead (no X11).

 2. Use the more recent open-source `vc4-fkms-v3d` kernel driver. This can run
    in either 32-bit or 64-bit, and X11 can use these, so using X11 is probably
    the more common choice here.

With option 2, the regular linux install instructions above should probably
work as-is.

For option 1, then also follow the above instructions, but with these
modifications:

 - With `cmake`, use `cmake -DWITH_PIC=on -DSTATIC=on -DSHARED=on -DPLATFORM='Raspberry Pi' ..`

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

Currently the DLL is being removed from the pypi packages but still available in the git repo.  Could split into its own pypi package if anyone wants it.

See test_dynamic.py for how to use.

## richlib

[A simplified API for Raylib for use in education and to enable beginners to create 3d games](https://github.com/electronstudio/richlib)

# HELP WANTED

 * converting more examples from C to python
 * testing and building on more platforms

# Performance

For fastest permformance use Pypy rather than standard python.

Every call to C is costly, so it's slightly faster if you use Python data structures and functions when calculating
in your update loop
and then only convert them to C data structures when you have to call the C functions for drawing.

## Bunnymark


| Library                | Implementation | Bunnies (60 FPS) | Percentage    |
| -------------          | -------------  | -------------    | ------------- |
| Raylib 3.7             | C              | 168100           | 100%          |
| Raylib Python CFFI 3.7 | Pypy 3.7     | 33800              | 20%           |
| Raylib Python CFFI 3.7 | Python 3.9     | 6800             | 4%            |

