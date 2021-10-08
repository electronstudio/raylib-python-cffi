#!/usr/bin/env bash

python3 raylib/build.py
pip3 install sphinx-autoapi myst_parser sphinx_rtd_theme
python3 create_stub_pyray.py > pyray/__init__.pyi
python3 create_stub_static.py >raylib/__init__.pyi
rm -r docs
cd docs-src
make clean ; make html ; mv _build/html/ ../docs/
touch ../docs/.nojekyll