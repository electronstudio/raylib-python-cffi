#!/usr/bin/env bash
cd raygui-c
cp src/raygui.h src/raygui.c
gcc -c -o raygui.o src/raygui.c -fpic -DRAYGUI_IMPLEMENTATION -DRAYGUI_SUPPORT_ICONS -lraylib -lGL -lm -lpthread -ldl -lrt -lX11
ar rcs raygui.a raygui.o
