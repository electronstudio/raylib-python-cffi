from pyray import *

init_window(400, 200, "raygui - controls test suite")
set_target_fps(60)


while not window_should_close():
    # Draw
    #----------------------------------------------------------------------------------
    begin_drawing()
    clear_background(get_color(abs(gui_get_style(DEFAULT, BACKGROUND_COLOR))));
    
    gui_button(Rectangle(24, 24, 320, 30), "#191#Background should be white")

    

    end_drawing()


close_window()
