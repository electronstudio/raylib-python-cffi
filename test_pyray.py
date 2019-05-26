"""
This shows how to use the Pyray wrapper around the static binding.
"""
from raylib.static.pyray import pyray as prl
from raylib.colors import *

prl.init_window(800, 450, "Raylib texture test")
prl.set_target_fps(60)

camera = prl.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
image = prl.load_image("examples/models/resources/heightmap.png")
texture = prl.load_texture_from_image(image)
mesh = prl.gen_mesh_heightmap(image, (16, 8, 16))
model = prl.load_model_from_mesh(mesh)
model.materials.maps[prl.MAP_DIFFUSE].texture = texture

prl.unload_image(image)
prl.set_camera_mode(camera, prl.CAMERA_ORBITAL)

while not prl.window_should_close():
    prl.update_camera(prl.pointer(camera))
    prl.begin_drawing()
    prl.clear_background(RAYWHITE)
    prl.begin_mode_3d(camera)
    prl.draw_model(model, (-8.0, 0.0, -8.0), 1.0, RED)
    prl.draw_grid(20, 1.0)
    prl.end_mode_3d()
    prl.draw_text("This mesh should be textured", 190, 200, 20, VIOLET)
    prl.end_drawing()
prl.close_window()
