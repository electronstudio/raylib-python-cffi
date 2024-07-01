from pyray import *
init_window(800, 450, "Hello")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    font = load_font_ex("/usr/share/fonts/TTF/FiraSans-Ultra.ttf", 30, None, 0)
    draw_text_ex(font, "hellow font", (300, 300), 30, 0, BLACK)
    draw_text("Hello world", 190, 200, 20, VIOLET)
    end_drawing()
close_window()
