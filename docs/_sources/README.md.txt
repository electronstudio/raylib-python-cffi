# Python Bindings for Raylib 3.7

New CFFI API static bindings.  Automatically generated to be as close as possible to 
original Raylib.  Faster, fewer bugs and easier to maintain than ctypes.

[Full documentation](http://electronstudio.github.io/raylib-python-cffi)

# License (updated)

The bindings are now under the Eclipse Public License, so you are free to 
statically link and use in non-free / proprietary / commercial projects!

# Installation

We distribute a statically linked binary Raylib wheel:

    pip3 install raylib

Some platforms that _should_ be available:  Windows 10 x64, MacOS 10.15 x64, Linux Ubuntu1804 x64.

If yours isn't available then pip will attempt to build from source, so you will need to have Raylib development libs installed.

[If it doesn't work, build from source](BUILDING.md)



# How to use

There are three different ways of using this binding.  You only need to pick one method, but you
can combine two methods in one program if you want to.

### If you are familiar with C coding and the Raylib C library and you want to use an exact copy of the C API

Use [raylib.static](https://electronstudio.github.io/raylib-python-cffi/raylib.html).

### If you prefer a slightly more Pythonistic API and don't mind it might be slightly slower

Use [raylib.pyray](https://electronstudio.github.io/raylib-python-cffi/pyray.html).

### If you insist on dynamic bindings and don't care that they are slower and less safe

Use [raylib.dynamic](https://electronstudio.github.io/raylib-python-cffi/dynamic.html).



# RLZero

Work in progress:

[A simplified API for Raylib for use in education and to enable beginners to create 3d games](https://github.com/electronstudio/rlzero)

# Help wanted

 * converting more examples from C to python
 * testing and building on more platforms

# Performance

For fastest permformance use Pypy rather than standard python.

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