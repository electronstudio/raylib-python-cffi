# Python Bindings for Raylib 5.5
## Libraries: raymath, raygui, rlgl, physac and GLFW
## Backends: Desktop, SDL, DRM, Web

Chatroom: [Discord](https://discord.gg/fKDwt85aX6) or [Matrix](https://matrix.to/#/#raylib-python-cffi:matrix.org)

New CFFI API static bindings.
* Automatically generated to be as close as possible to 
original Raylib.
* Faster, fewer bugs and easier to maintain than ctypes.
* Commercial-friendly license.
* Docstrings and auto-completion.


[Full documentation](http://electronstudio.github.io/raylib-python-cffi)

# Quickstart

`pip3 install raylib==5.0.0.4`
```python
from pyray import *
init_window(800, 450, "Hello")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text("Hello world", 190, 200, 20, VIOLET)
    end_drawing()
close_window()
```

# Installation

First make sure you have the latest pip installed:

    python3 -m pip install --upgrade pip

Then install

    python3 -m pip install setuptools
    python3 -m pip install raylib==5.0.0.4

On most platforms it should install a binary wheel.  If yours isn't available then pip will attempt to build from source, in which case you will need to have Raylib development libs installed, e.g. 
using homebrew, apt, etc.

## Windows

Binaries require x64 Windows 10 or newer.  (For x86 or older Windows you will have to build from source.)

Use an [official Windows Python release](https://www.python.org/downloads/windows/) rather than WSL, MSYS, etc.

## MacOS

Binaries require arm64 MacOS 13 or x64 MacOS 12 or newer.

Older MacOS requires building from source but this is usually simple:

    brew install pkg-config
    brew install raylib
    python3 -m pip install raylib==5.0.0.4

## Linux

Binaries require OS newer than Ubuntu 2020, x64 or arm64.   Otherwise build from source.
(Pip should attempt automatically but will need Raylib itself installed and also pkg-config.)

The arm64 builds are built on Raspberry Pi arm64 Bullseye
so may not work on other boards.

## Raspberry Pi

[Using on Rasperry Pi](RPI.rst)

## Dynamic binding version

There is now a separate dynamic version of this binding:

    python3 -m pip install raylib_dynamic

It works on some systems where the static version doesn't, [but be sure to read these caveats before using it](https://electronstudio.github.io/raylib-python-cffi/dynamic.html)

## SDL backend

This is not well tested but has better support for controllers:

    python3 -m pip uninstall raylib
    python3 -m pip install raylib_sdl

You can't have multiple backends installed at once.

## DRM backend

This uses the Linux framebuffer for devices that don't run X11/Wayland:

    python3 -m pip uninstall raylib
    python3 -m pip install raylib_drm

You can't have multiple backends installed at once.

## Problems?

If it doesn't work, [try to build manually.](BUILDING.rst).  If that works then [submit an issue](https://github.com/electronstudio/raylib-python-cffi/issues)
to let us know what you did.

If you need help you can try asking [on Discord](https://discord.gg/raylib).

If it still doesn't work, [submit an issue](https://github.com/electronstudio/raylib-python-cffi/issues).


# How to use

There are two APIs, you can use either or both:

### If you are familiar with C coding and the Raylib C library and you want to use an exact copy of the C API

Use [the C API](https://electronstudio.github.io/raylib-python-cffi/raylib.html).

### If you prefer a slightly more Pythonistic API and don't mind it might be slightly slower

Use [the Python API](https://electronstudio.github.io/raylib-python-cffi/pyray.html).

# Running in a web browser

[Pygbag](https://pypi.org/project/pygbag/) >=0.8.7 supports running in a web browser.

Make a folder `my_project` with a file `main.py`:

    # /// script
    # dependencies = [
    #     "cffi",
    #     "raylib"
    # ]
    # ///
    import asyncio
    import platform
    from pyray import *

    async def main():   # You must have an async main function
        init_window(500, 500, "Hello")
        platform.window.window_resize()  # You must add this line
        while not window_should_close():
            begin_drawing()
            clear_background(WHITE)
            draw_text("Hello world", 190, 200, 20, VIOLET)
            end_drawing()
            await asyncio.sleep(0) # You must call this in your main loop
        close_window()

    asyncio.run(main())

Then to create the web files and launch a web server:

    python3.12 -m pip install --user --upgrade pygbag
    python3.12 -m pygbag --PYBUILD 3.12 --ume_block 0 --template noctx.tmpl my_project

Point your browser to http://localhost:8000

This is all done by Pygbag rather than by me, so you should probably contact them with any issues.
Carefully read all their [documentation](https://pygame-web.github.io/).

It does work for most of [these examples](https://electronstudio.github.io/raylib-python-cffi-pygbag-examples/)

# App showcase

[Tanki](https://github.com/pkulev/tanki)

[Alloy Bloxel Editor](https://pebaz.itch.io/alloy-bloxel-editor)

Add your app here!

# RLZero

A related library (that is a work in progress!):

[A simplified API for Raylib for use in education and to enable beginners to create 3d games](https://github.com/electronstudio/rlzero)

# Help wanted

 * Converting more examples from C to Python
 * Testing on more platforms

# License

Eclipse Public License, so you are free to
statically link and use in non-free / proprietary / commercial projects!

# Performance

If you need more performance, do in this order:

1. Use Pypy rather than standard CPython.  It is much, much faster and will make more difference than any other optimisations you might do.

2. Every call to C is costly, so it's slightly faster if you use Python data structures and functions when calculating
in your update loop
and then only convert them to C data structures when you have to call the C functions for drawing.

3. The raylib.* functions are potentially *slightly* faster than the pyray.* equivalents, so if you need a tiny bit more performance
you can switch your inner loop functions to these.

4. There is a version of Python that is faster than Pypy: GraalPy.  However it's not fully compatible with all Python
packages.  It doesn't work with CFFI and so doesn't work with this binding.  But it *is* compatible with the
*Java* binding, Jaylib!  There is an example of this here: https://github.com/electronstudio/megabunny/tree/master/raylib-python-jaylib

## Bunnymark


| Library                        | Implementation    | Bunnies (60 FPS) | Percentage |
|--------------------------------|-------------------|------------------|------------|
| Raylib 5.0                     | C                 | 180000           | 100%       |
| Raylib Python CFFI 5.0.0.2     | Python 3.12       | 10500            | 5.8%       |
| Raylib Python CFFI 5.0.0.2     | Pypy 3.10         | 95000            | 53%        |
| Raylib 3.7                     | C                 | 168100           | 100%       |
| Raylib Python CFFI 3.7         | Pypy 3.7          | 33800            | 20%        |
| Raylib Python CFFI 3.7         | Python 3.9        | 7700             | 4.5%       |
| Raylib Python CFFI 3.7         | Python 3.9 Nuitka | 8600             | 5.1%       |
| Raylib Python CFFI 3.7 Dynamic | Python 3.9        | 6300             | 3.7%       |

See also https://github.com/electronstudio/megabunny/

# Packaging your app

You can create a standalone binary using the Nuitka compiler.  For example, here is how to package Bunnymark:

    pip3 install nuitka
    cd examples/textures
    python3 -m nuitka --onefile --linux-onefile-icon resources/wabbit_alpha.png textures_bunnymark.py

# Advert

[RetroWar: 8-bit Party Battle](https://store.steampowered.com/app/664240/RetroWar_8bit_Party_Battle/?git) is out now.  Defeat up to 15 of your friends in a tournament of 80s-inspired retro mini games.

[Coding Games With Pygame Zero & Python](https://github.com/electronstudio/pygame-zero-book) is 
a book for Python beginners.
