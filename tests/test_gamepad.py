import pyray as pr
pr.set_config_flags(pr.FLAG_MSAA_4X_HINT)
pr.init_window(800, 600, 'Test gamepad')
pr.set_target_fps(60)
while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    if pr.is_gamepad_available(0):
        pr.draw_text(f'GP0: {pr.get_gamepad_name(0)}', 5, 5, 20, pr.RAYWHITE)
        pr.draw_text(f'Axis: {pr.get_gamepad_axis_count(0)}', 5, 30, 20, pr.RAYWHITE)
        pr.draw_text(f'Button: {pr.get_gamepad_button_pressed()}', 5, 55, 20, pr.RAYWHITE)
        _hy_anon_var_1 = pr.draw_text(
            f'Axis 0: {pr.get_gamepad_axis_movement(0, 0)}', 5, 85, 20, pr.RAYWHITE)
    else:
        _hy_anon_var_1 = None
    pr.end_drawing()
pr.close_window()