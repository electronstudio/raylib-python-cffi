raylib.dynamic
==============

CFFI ABI dynamic bindings exist in order to avoid the need to compile a C extension module.

Currently the github version may include bundled DLLs in ``raylib/dynamic`` but the pypi version requires a system installed Raylib.
You can put your own DLLs in ``raylib/dynamic`` if you prefer.

If your system already has the Raylib library installed, you can set the environment variable ``USE_EXTERNAL_RAYLIB`` and it will
always be used instead of the bundled DLLs.

See https://github.com/electronstudio/raylib-python-cffi/blob/master/test_static.py for how to use.

.. warning::

   There have been some weird failures with dynamic bindings and ctypes bindings before and often the
   failures are silent
   so you dont even know.  Also the static bindings should be faster.  Therefore I personally recommend the static ones.
   But the dynamic bindings have the big advantage that you don't need to compile anything to install.  You just need a Raylib DLL.

API is the same as raylib.static.