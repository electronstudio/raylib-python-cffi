import pyray as pr

screenWidth = 800
screenHeight = 600

pr.set_config_flags(pr.FLAG_WINDOW_UNDECORATED)

pr.init_window(screenWidth, screenHeight, "raygui - portable window")


mousePosition = pr.Vector2(0, 0)
windowPosition = pr.Vector2(500, 200 )
panOffset = mousePosition
dragWindow = False

pr.set_window_position(int(windowPosition.x), int(windowPosition.y))

exitWindow = False

pr.set_target_fps(60)


while not exitWindow and not pr.window_should_close():

    mousePosition = pr.get_mouse_position()

    if pr.is_mouse_button_pressed(pr.MOUSE_BUTTON_LEFT):
        if pr.check_collision_point_rec(mousePosition,  pr.Rectangle(0, 0, screenWidth, 20)):
            dragWindow = True
            panOffset = mousePosition

    if dragWindow:
        windowPosition.x += (mousePosition.x - panOffset.x)
        windowPosition.y += (mousePosition.y - panOffset.y)
        if pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):
            dragWindow = False

        pr.set_window_position(int(windowPosition.x), int(windowPosition.y))

    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    exitWindow = pr.gui_window_box(pr.Rectangle(0, 0, screenWidth, screenHeight), "#198# PORTABLE WINDOW")
    pr.draw_text(f"Mouse Position: {mousePosition.x} {mousePosition.y}", 10, 40, 10, pr.DARKGRAY)
    pr.end_drawing()

pr.close_window()