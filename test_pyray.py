"""
This shows how to use the Pyray wrapper around the static binding.
"""

from raylib.pyray import PyRay
from raylib.colors import *

pyray = PyRay()

pyray.init_window(800, 450, "Raylib texture test")
pyray.set_target_fps(60)

camera = pyray.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
image = pyray.load_image("examples/models/resources/heightmap.png")
texture = pyray.load_texture_from_image(image)
mesh = pyray.gen_mesh_heightmap(image, (16, 8, 16))
model = pyray.load_model_from_mesh(mesh)
model.materials.maps[pyray.MAP_DIFFUSE].texture = texture

pyray.unload_image(image)
pyray.set_camera_mode(camera, pyray.CAMERA_ORBITAL)

while not pyray.window_should_close():
    pyray.update_camera(pyray.pointer(camera))
    pyray.begin_drawing()
    pyray.clear_background(RAYWHITE)
    pyray.begin_mode_3d(camera)
    pyray.draw_model(model, (-8.0, 0.0, -8.0), 1.0, RED)
    pyray.draw_grid(20, 1.0)
    pyray.end_mode_3d()
    pyray.draw_text("This mesh should be textured", 190, 200, 20, VIOLET)
    pyray.end_drawing()
pyray.close_window()
