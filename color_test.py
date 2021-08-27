from raylib.pyray import PyRay
pyray = PyRay()
pyray.init_window(800, 400, 'demo')


white = pyray.get_color(0xFFFFFFFF)
red = pyray.get_color(0xFF0000FF)
green = pyray.get_color(0x00FF00FF)
blue = pyray.get_color(0x0000FFFF)

while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.clear_background(white)
    pyray.draw_rectangle(0, 0, 100, 100, red)
    pyray.draw_rectangle(100, 100, 100, 100, green)
    pyray.draw_rectangle(200, 200, 100, 100, blue)
    pyray.end_drawing()
pyray.close_window()
