"""
This shows how to use the Pyray wrapper around the static binding.
"""

from pyray import *

init_window(800, 450, "Raylib texture test")
set_target_fps(60)

image = gen_image_color(800, 400, (0,0,0,255) )
texture = load_texture_from_image(image)
update_texture(texture, image.data)

camera = Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
image = load_image("examples/models/resources/heightmap.png")
texture = load_texture_from_image(image)
mesh = gen_mesh_heightmap(image, (16, 8, 16))
model = load_model_from_mesh(mesh)
model.materials.maps[MATERIAL_MAP_ALBEDO].texture = texture

unload_image(image)
set_camera_mode(camera, CAMERA_ORBITAL)

pos = get_mouse_position()
ray = get_mouse_ray(pos, camera)
#rayhit = get_ray_collision_ground(ray, 0)
#print(str(rayhit.position.x))

while not window_should_close():
    update_camera(camera)
    begin_drawing()
    clear_background(RAYWHITE)
    begin_mode_3d(camera)
    draw_model(model, (-8.0, 0.0, -8.0), 1.0, RED)
    draw_grid(20, 1.0)
    end_mode_3d()
    draw_text("This mesh should be textured", 190, 200, 20, VIOLET)
    end_drawing()

    pos = get_mouse_position()
    ray = get_mouse_ray(pos, camera)
    #rayhit = get_ray_collision_ground(ray, 0)
    #print(str(rayhit.position.x))

close_window()
