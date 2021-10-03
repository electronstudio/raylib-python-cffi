raylib.dynamic
==============

CFFI ABI dynamic bindings avoid the need to compile a C extension module.  They now been moved to a separate module::

   python3 -m pip install raylib_dynamic

.. warning::

   There have been some weird failures with dynamic bindings and ctypes bindings before and often the
   failures are silent
   so you dont even know.  Also the static bindings are faster.  Therefore I personally recommend the static ones.
   But the dynamic bindings have the advantage that you don't need to compile anything to install.  You just need a Raylib DLL.

API is exactly the same as the static one documented here.  (Therefore you can't have both modules installed at once.)  The only difference is you can't do::

    from raylib import *

Instead you have to do::

    from raylib import raylib as rl

Then you access the functions with ``rl.`` prefix.  See

See https://github.com/electronstudio/raylib-python-cffi/blob/master/dynamic/test_dynamic.py for an example.



.. important::

   If your system already has the Raylib library installed, you can set the environment variable ``USE_EXTERNAL_RAYLIB`` and it will
   always be used instead of the bundled DLLs.



.. note::

   If you write a program using the ``rl.`` prefix on all the functions and then you decide you want to use
   that same program with the static binding instead of the dynamic, you don't have to remove the ``rl``,
   you can just do::

       import raylib as rl
