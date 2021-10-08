"""
This shows how to use the Pyray wrapper around the static binding.
"""

import pyray as pr

pr.init_window(800, 450, "Raylib texture test")
pr.set_target_fps(60)

image = pr.gen_image_color(800, 400, (0,0,0,255) )
texture = pr.load_texture_from_image(image)
pr.update_texture(texture, image.data)

camera = pr.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
image = pr.load_image("examples/models/resources/heightmap.png")
texture = pr.load_texture_from_image(image)
mesh = pr.gen_mesh_heightmap(image, (16, 8, 16))
model = pr.load_model_from_mesh(mesh)
model.materials.maps[pr.MATERIAL_MAP_DIFFUSE].texture = texture

pr.unload_image(image)
pr.set_camera_mode(camera, pr.CAMERA_ORBITAL)

pos = pr.get_mouse_position()
ray = pr.get_mouse_ray(pos, camera)
rayhit = pr.get_collision_ray_ground(ray, 0)
print(str(rayhit.position.x))

while not pr.window_should_close():
    pr.update_camera(camera)
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    pr.begin_mode_3d(camera)
    pr.draw_model(model, (-8.0, 0.0, -8.0), 1.0, pr.RED)
    pr.draw_grid(20, 1.0)
    pr.end_mode_3d()
    pr.draw_text("This mesh should be textured", 190, 200, 20, pr.VIOLET)
    pr.end_drawing()

    pos = pr.get_mouse_position()
    ray = pr.get_mouse_ray(pos, camera)
    rayhit = pr.get_collision_ray_ground(ray, 0)
    #print(str(rayhit.position.x))

pr.close_window()
