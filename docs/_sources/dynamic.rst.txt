Dynamic Bindings
================

CFFI ABI dynamic bindings avoid the need to compile a C extension module.  They now been moved to a separate module::

   python3 -m pip install raylib_dynamic

.. warning::

   There have been some weird failures with dynamic bindings and ctypes bindings before and often the
   failures are silent
   so you don't even know something has gone wrong and you don't get proper stacktraces.  Also the static bindings are faster.
   Therefore I personally recommend the static ones.
   But the dynamic bindings have the advantage that you don't need to compile anything to install.  You just need a Raylib DLL.

API is exactly the same as the static one documented here.  (Therefore you can't have both modules installed at once.)  The only difference is you can't do::

    from raylib import *

Instead you have to do::

    from raylib import rl

Then you access the functions with ``rl.`` prefix.

See https://github.com/electronstudio/raylib-python-cffi/blob/master/dynamic/test_dynamic.py for an example.

If you use the ``rl.`` prefix then code will work on both static and dynamic bindings.

.. tip::

   If you access functions via ``import pyray`` then there is no difference at all, but be warned this hasn't been tested much.


.. important::

   If your system already has the Raylib library installed, you can set the environment variable ``USE_EXTERNAL_RAYLIB`` and it will
   always be used instead of the bundled DLLs.
