raylib.static
=============

The goal of raylib.static is make usage as similar to the original C as CFFI will allow.  The `example programs <https://github.com/electronstudio/raylib-python-cffi/tree/master/examples>`_
are very, very similar to the C originals.

Example program:

.. code-block::

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

See also https://github.com/electronstudio/raylib-python-cffi/blob/master/test_static.py

Also useful to read whenever you need to convert stuff between C and Python: https://cffi.readthedocs.io

Your **primary reference** should always be `the official Raylib docs <https://www.raylib.com/cheatsheet/cheatsheet.html>`_

However, here is a list of available functions:

Functions API reference
-----------------------

.. autoapimodule:: raylib.static
    :members:
    :undoc-members:



