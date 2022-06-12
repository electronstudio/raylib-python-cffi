Python API
==============

This is a wrapper around the C API with some syntactic sugar.

The API is *still the same as Raylib*, so you should still reply on `the official Raylib docs <https://www.raylib.com/cheatsheet/cheatsheet.html>`_, except:

* the function names are in **snake_case**.

* Some string and pointer conversions are handled automatically.

* There are some helper functions to create structures.

Example program:

..  code-block::

    import pyray as pr

    pr.init_window(800, 450, "Hello Pyray")
    pr.set_target_fps(60)

    camera = pr.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
    pr.set_camera_mode(camera, pr.CAMERA_ORBITAL)

    while not pr.window_should_close():
        pr.update_camera(camera)
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)
        pr.begin_mode_3d(camera)
        pr.draw_grid(20, 1.0)
        pr.end_mode_3d()
        pr.draw_text("Hello world", 190, 200, 20, pr.VIOLET)
        pr.end_drawing()
    pr.close_window()

..  tip:: New in 3.7.0.post9:

    You can also now import the functions with no prefix:

    ..  code-block::

        from pyray import *

        init_window(800, 450, "Raylib texture test")
        ...

    You don't need to use the PyRay() class anymore.

See also https://github.com/electronstudio/raylib-python-cffi/blob/master/tests/test_pyray.py

API reference
-------------

.. autoapimodule:: pyray
    :members:
    :undoc-members:
