import pyray

pyray.init_window(800, 450, b"Hello Raylib [pyray]")

while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.clear_background(pyray.RAYWHITE)
    pyray.draw_text(b"Hello, world!", 190, 200, 20, pyray.DARKGRAY)
    pyray.end_drawing()

pyray.close_window()
