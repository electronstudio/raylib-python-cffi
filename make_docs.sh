#!/usr/bin/bash

python3 create_stub_pyray.py > raylib/pyray.pyi
python3 create_stub_static.py >raylib/static/__init__.pyi
cd docs-src
make clean ; make html ; cp -a _build/html/. ../docs/
