#!/usr/bin/bash

python3 create_stub.py > raylib/pyray.pyi
cd docs-src
make clean ; make html ; cp -a _build/html/. ../docs/
