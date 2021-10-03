#!/usr/bin/env bash

pip3 install sphinx-autoapi myst_parser sphinx_rtd_theme
python3 create_stub_pyray.py > raylib/pyray.pyi
python3 create_stub_static.py >raylib/__init__.pyi
cd docs-src
make clean ; make html ; cp -a _build/html/. ../docs/
