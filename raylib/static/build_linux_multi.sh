#!/usr/bin/env bash
rm *linux-gnu.so
pyenv install -s 3.9.0
pyenv global 3.9.0
pip3 install cffi
python build_linux.py
pyenv install -s 3.8.6
pyenv global 3.8.6
pip3 install cffi
python build_linux.py
pyenv install -s 3.7.9
pyenv global 3.7.9
pip3 install cffi
python build_linux.py
pyenv install -s 3.6.12
pyenv global 3.6.12
pip3 install cffi
python build_linux.py
