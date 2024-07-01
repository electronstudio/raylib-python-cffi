#/*******************************************************************************************
#*
#*   raylib [shapes] example - draw rectangle rounded (with gui options)
#*
#*   This example has been created using raylib 2.5 (www.raylib.com)
#*   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#*
#*   Example contributed by Vlad Adrian (@demizdor) and reviewed by Ramon Santamaria (@raysan5)
#*
#*   Copyright (c) 2018 Vlad Adrian (@demizdor) and Ramon Santamaria (@raysan5)
#*
#********************************************************************************************/

import pyray
from raylib.colors import (
    RAYWHITE,
    LIGHTGRAY,
    DARKGRAY,
    GOLD,
    MAROON,
)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "raylib [shapes] example - draw rectangle rounded")



drawRect = False
drawRoundedRect = True
drawRoundedLines = False

pyray.set_target_fps(60)
width = pyray.ffi.new('float *', 200)
# these need to be changed to pointers for new raygui format
roundness = 0.2
height = 100
segments = 0
lineThick = 1
#// Main game loop
while not pyray.window_should_close():  #// Detect window close button or ESC key

    #// Update
    #//----------------------------------------------------------------------------------
    rec = pyray.Rectangle( (pyray.get_screen_width()-width[0]-250)/2, (pyray.get_screen_height()-height)/2, width[0], height )
    #//----------------------------------------------------------------------------------

    #// Draw
    #//----------------------------------------------------------------------------------
    pyray.begin_drawing()
    pyray.clear_background(RAYWHITE)

    pyray.draw_line(560,0,560,pyray.get_screen_height(),pyray.fade(LIGHTGRAY,0.6))
    pyray.draw_rectangle(560,0,pyray.get_screen_width()-500,pyray.get_screen_height(),pyray.fade(LIGHTGRAY,0.3))

    if drawRect:
        pyray.draw_rectangle_rec(rec,pyray.fade(GOLD,0.6))
    if drawRoundedRect:
        pyray.draw_rectangle_rounded(rec,roundness,segments,pyray.fade(MAROON,0.2))
    if drawRoundedLines:
        pyray.draw_rectangle_rounded_lines(rec,roundness,segments,lineThick,pyray.fade(MAROON,0.4))

    #// Draw GUI controls
    #//------------------------------------------------------------------------------

    pyray.gui_slider_bar(pyray.Rectangle(640,40,105,20),"Width","",width,0,pyray.get_screen_width()-300)

    # these need to be updated to new raygui format like above like

    # height = int( pyray.gui_slider_bar(pyray.Rectangle(640,70,105,20),"Height",0,height,0,pyray.get_screen_height()-50) )
    # roundness = pyray.gui_slider_bar(pyray.Rectangle(640,140,105,20),"Roundness",0,roundness,0,1)
    # lineThick = int( pyray.gui_slider_bar(pyray.Rectangle(640,170,105,20),"Thickness",0,lineThick,0,20) )
    # segments = int( pyray.gui_slider_bar(pyray.Rectangle(640,240,105,20),"Segments",0,segments,0,60) )
    #
    # drawRoundedRect = pyray.gui_check_box(pyray.Rectangle(640,320,20,20),"DrawRoundedRect",drawRoundedRect)
    # drawRoundedLines = pyray.gui_check_box(pyray.Rectangle(640,350,20,20),"DrawRoundedLines",drawRoundedLines)
    # drawRect = pyray.gui_check_box(pyray.Rectangle(640,380,20,20),"DrawRect",drawRect)
    #//------------------------------------------------------------------------------

    pyray.draw_text( "MANUAL" if segments >= 4 else "AUTO" , 640, 280, 10, MAROON if segments >= 4 else DARKGRAY)
    pyray.draw_fps(10,10)
    pyray.end_drawing()
    #//------------------------------------------------------------------------------

# De-Initialization
pyray.close_window()  # Close window and OpenGL context