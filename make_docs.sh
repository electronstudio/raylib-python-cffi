#!/usr/bin/env bash

gcc raylib-c/parser/raylib_parser.c
./a.out -i raygui/src/raygui.h -d RAYGUIAPI -o raygui.json -f JSON
./a.out -i physac/src/physac.h -d PHYSACDEF -o physac.json -f JSON
./a.out -i raylib-c/src/raylib.h -o raylib.json -f JSON
./a.out -i raylib-c/src/rlgl.h -o rlgl.json -f JSON
./a.out -i raylib-c/src/raymath.h -d RMAPI -o raymath.json -f JSON
./a.out -i raylib-c/src/external/glfw/include/GLFW/glfw3.h -d GLFWAPI -o glfw3.json -f JSON
sed -i "s|\/\*.*,$|,|g" glfw3.json

python3 raylib/build.py

python3 create_enums.py > raylib/enums.py
python3 create_enums.py > dynamic/raylib/enums.py
python3 create_define_consts.py > raylib/defines.py
python3 create_define_consts.py > dynamic/raylib/defines.py

pip3 install sphinx-autoapi myst_parser sphinx_rtd_theme
python3 create_stub_pyray.py > pyray/__init__.pyi
python3 create_enums.py >> pyray/__init__.pyi
cat raylib/colors.py >> pyray/__init__.pyi
python3 create_stub_static.py >raylib/__init__.pyi
cat raylib/colors.py >> raylib/__init__.pyi
rm -r docs
cd docs-src
make clean ; make html ; mv _build/html/ ../docs/
touch ../docs/.nojekyll