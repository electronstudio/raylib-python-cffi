from pyray import *

init_window(800, 450, "Raylib test")
camera = Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
while not window_should_close():
    update_camera(camera, CameraMode.CAMERA_ORBITAL)
    begin_drawing()
    clear_background(WHITE)
    begin_mode_3d(camera)
    draw_grid(20, 1.0)
    end_mode_3d()
    draw_text("Raylib is working", 190, 200, 20, VIOLET)
    draw_fps(20, 20)
    end_drawing()
close_window()
