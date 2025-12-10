from pyray import *
import raylib

screenWidth = 800
screenHeight = 480

init_window(screenWidth, screenHeight, "raygui - styles selector")
set_exit_key(0)

# TODO? fonts
# font = LoadFontEx("fonts/custom_font.ttf", 12, 0, 0);
# GuiSetFont(font)

exitWindow = False
showMessageBox = False

# TODO? the styles that come with raggui
# GuiLoadStyleBluish();
visualStyleActive = ffi.new('int *', 0)
prevVisualStyleActive = ffi.new('int *', 1)

set_target_fps(60)

while not exitWindow:
    exitWindow = window_should_close()

    if is_key_pressed(KeyboardKey.KEY_ESCAPE):
        showMessageBox = not showMessageBox

    if is_file_dropped():
        droppedFiles = load_dropped_files()

        if (droppedFiles.count > 0) and is_file_extension(droppedFiles.paths[0], ".rgs"):
            gui_load_style(droppedFiles.paths[0])

        unload_dropped_files(droppedFiles)


    if visualStyleActive[0] != prevVisualStyleActive[0]:
        gui_load_style_default()
        match visualStyleActive[0]:
            case 0:
                gui_set_style(GuiControl.DEFAULT, GuiDefaultProperty.BACKGROUND_COLOR,  0x000000FF) # black
                gui_set_style(GuiControl.DEFAULT, GuiDefaultProperty.LINE_COLOR,  color_to_int(GREEN))
            case 1:
                gui_set_style(GuiControl.DEFAULT, GuiDefaultProperty.BACKGROUND_COLOR, 0xF5F5F5FF) # white
                gui_set_style(GuiControl.DEFAULT, GuiDefaultProperty.LINE_COLOR,  color_to_int(RED)) # red
            case 2:
                gui_set_style(GuiControl.DEFAULT, GuiDefaultProperty.BACKGROUND_COLOR,  0xFF0000FF) # red
                gui_set_style(GuiControl.DEFAULT, GuiDefaultProperty.LINE_COLOR,  color_to_int(BLUE)) # blue

        prevVisualStyleActive[0] = visualStyleActive[0]

    begin_drawing()

    style = gui_get_style(GuiControl.DEFAULT, GuiDefaultProperty.BACKGROUND_COLOR)
    clear_background(get_color(style))

    gui_label((10, 10, 60, 24 ), "Style:")
    gui_label((200, 10, 160, 24 ), f"hex code: {hex(style)}")
    gui_combo_box((60,10, 120, 24 ), "black;whitish;red", visualStyleActive)

    draw_rectangle(10, 44, gui_get_font().texture.width, gui_get_font().texture.height, BLACK)
    draw_texture(gui_get_font().texture, 10, 44, WHITE)
    draw_rectangle_lines(10, 44, gui_get_font().texture.width, gui_get_font().texture.height,
        get_color(gui_get_style(GuiControl.DEFAULT, GuiDefaultProperty.LINE_COLOR)))


    end_drawing()
close_window()