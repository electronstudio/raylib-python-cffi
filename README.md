# Python Bindings for Raylib 3.7

New CFFI API static bindings.  Automatically generated to be as close as possible to 
original Raylib.  Faster, fewer bugs and easier to maintain than ctypes.  Commercial-friendly license.
Docstrings and auto-completion.

[Full documentation](http://electronstudio.github.io/raylib-python-cffi)

# Quickstart

`pip3 install raylib`

    from pyray import *
    init_window(800, 450, "Hello")
    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)
        draw_text("Hello world", 190, 200, 20, VIOLET)
        end_drawing()
    close_window()


# Installation

First make sure you have latest pip installed:

    python3 -m pip install --upgrade pip

Then install

    python3 -m pip install raylib

On most platforms it should install a binary wheel (Windows 10 x64, MacOS 10.15 x64, Linux Ubuntu1804 x64).

If yours isn't available then pip will attempt to build from source, in which case you will need to have Raylib development libs installed, e.g. 
using homebrew, apt, etc.

[If it doesn't work, you can build manually.](BUILDING.rst)

## Dynamic binding version

There is now a separate dynamic version of this binding:

    python3 -m pip install raylib_dynamic

[Read this before using raylib_dynamic](https://electronstudio.github.io/raylib-python-cffi/dynamic.html)

## Beta testing

You can install an alpha or beta version by specifying the version number like this:

    python3 -m pip install raylib==4.0a3


# How to use

There are two APIs, you can use either or both:

### If you are familiar with C coding and the Raylib C library and you want to use an exact copy of the C API

Use [the C API](https://electronstudio.github.io/raylib-python-cffi/raylib.html).

### If you prefer a slightly more Pythonistic API and don't mind it might be slightly slower

Use [the Python API](https://electronstudio.github.io/raylib-python-cffi/pyray.html).




# RLZero

A related library (that is a work in progress!):

[A simplified API for Raylib for use in education and to enable beginners to create 3d games](https://github.com/electronstudio/rlzero)

# Help wanted

 * Converting more examples from C to Python
 * Testing on more platforms

# License (updated)

The bindings are now under the Eclipse Public License, so you are free to
statically link and use in non-free / proprietary / commercial projects!

# Performance

For fastest performance use Pypy rather than standard Python.

Every call to C is costly, so it's slightly faster if you use Python data structures and functions when calculating
in your update loop
and then only convert them to C data structures when you have to call the C functions for drawing.

## Bunnymark


| Library                | Implementation    | Bunnies (60 FPS) | Percentage    |
| -------------          | -------------     | -------------    | ------------- |
| Raylib 3.7             | C                 | 168100           | 100%          |
| Raylib Python CFFI 3.7 | Pypy 3.7          | 33800            | 20%           |
| Raylib Python CFFI 3.7 | Python 3.9        | 7700             |  4.5%         |
| Raylib Python CFFI 3.7 | Python 3.9 Nuitka | 8600             |  5.1%         |
| Raylib Python CFFI 3.7 Dynamic | Python 3.9 | 6300             |  3.7%         |

# Packaging your app

You can create a standalone binary using the Nuitka compiler.  For example, here is how to package Bunnymark:

    pip3 install nuitka
    cd examples/textures
    python3 -m nuitka --onefile --linux-onefile-icon resources/wabbit_alpha.png textures_bunnymark.py

# Advert

[RetroWar: 8-bit Party Battle](https://store.steampowered.com/app/664240/RetroWar_8bit_Party_Battle/?git) is out now.  Defeat up to 15 of your friends in a tournament of 80s-inspired retro mini games.

[Coding Games With Pygame Zero & Python](https://github.com/electronstudio/pygame-zero-book) is 
a book for Python beginners.