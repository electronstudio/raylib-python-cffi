#!/usr/bin/env bash
rm *linux-gnu.so
pyenv global 3.8.1
pip3 install cffi
python build_linux.py
pyenv global 3.7.6
pip3 install cffi
python build_linux.py
pyenv global 3.6.10
pip3 install cffi
python build_linux.py
