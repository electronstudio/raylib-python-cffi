# Python Bindings for Raylib

This uses CFFI API static bindings rather than ctypes.  Hopefully this will be faster, the static type knowledge from the C
headers will result in fewer bugs, and using the original headers will make it easier to maintain.

Currently the goal is make usage as similar to the original C as CFFI will allow.  There are a few differences
you can see in the examples.  Making a 'Pythonic' library would be an additional layer on top which hasn't been
done yet.

See test_static.py and examples/*.py for how to use.

# Installing

**MacOS: Python 3.7**: we distribute a statically linked Raylib library, so in theory the only thing you need to do is install
us from Pypi.

    pip3 install raylib

**Linux: Python 3.6**: we dont distribute Raylib, so you must have Raylib 2.5dev already installed on your system.  Currently we are building from the github version, specifically https://github.com/raysan5/raylib/commit/f325978b26ea934095f74ac628e6578ebbc2b7a0 although I guess any 2.5 build should work. First follow the instructions here: https://github.com/raysan5/raylib/wiki/Working-on-GNU-Linux Then do:

    pip3 install raylib
    
**Windows 10 (64 bit): Python 3.7**: we distribute a statically linked Raylib library, thanks to https://github.com/Pebaz, so in theory the only thing you need to do is install us from Pypi.
                                     
    pip3 install raylib

If you're using a different version of Python, or maybe a Linux/Mac with incompatible libraries
you will have to build.  The specific version we built against is https://github.com/raysan5/raylib/commit/f325978b26ea934095f74ac628e6578ebbc2b7a0 but we should soon try to synchronize with a proper released version of Raylib.

    cd raylib
    python3 build_linux.py
    python3 build_mac.py

# Platforms tested

 * MacOS 10.12.6 - Python 3.7
 * Ubuntu 18.04 LTS - Python 3.6
 * Windows 10 (64 bit) - Python 3.7

# HELP WANTED

 * converting more examples from C to python
 * testing and building on more platforms
 
### Dynamic bindings

In addition to the API static bindings I have attempted to do CFFI ABI dynamic bindings in order to avoid the need to compile a C extension module.
There have been some weird failures with dynamic bindings and ctypes bindings before and often the failures are silent
so you dont even know.  Also the static bindings should be faster.  Therefore I recommend the static ones...

BUT the dynamic bindings have the big advantage that you don't need to compile anything to install.

See test_dynamic.py for how to use them.