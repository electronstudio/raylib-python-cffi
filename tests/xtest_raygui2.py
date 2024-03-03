import pyray
from pyray import *
import pytest

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raygui")
    set_exit_key(KeyboardKey.KEY_ESCAPE)
    set_target_fps(30)

    _bool_pointer = pyray.ffi.new("bool *", True)
    _bool = True
    _float = 5.5
    _float_pointer = pyray.ffi.new("float *", 5.2)
    color = RED
    color_pointer = Color()
    _int=0
    _int_pointer = pyray.ffi.new("int *", 0)
    _string ="cant edit this string"
    _string_pointer = pyray.ffi.new("char []", b"0123456789")

    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)

        gui_check_box((40, 40, 30, 30), "checkbox", _bool_pointer)
        with pytest.raises(TypeError):
            gui_check_box(Rectangle(40, 40, 100, 100), "checkbox", _bool)

        gui_color_bar_alpha((40, 80, 100, 20), "bar", _float_pointer)
        with pytest.raises(TypeError):
            gui_color_bar_alpha((40, 80, 100, 20), "bar", _float)

        gui_color_picker((40,120, 100, 100), "color", color_pointer)
        with pytest.raises(TypeError):
            gui_color_picker((40,120, 100, 100), "color", color)

        gui_text_box((40,230, 100, 30), _string_pointer, 10, True)
        gui_text_box((200,230, 100, 30), _string, 10, True)

        gui_tab_bar((40,300, 100, 30), ["foo", "boo"], 2, _int_pointer)
        with pytest.raises(TypeError):
            gui_tab_bar((40,300, 100, 30), ["foo", "boo"], 2, _int)

        end_drawing()
main()