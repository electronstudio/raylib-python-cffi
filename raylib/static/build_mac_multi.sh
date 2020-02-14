#!/usr/bin/env bash
rm *darwin.so
pyenv global 3.8.1
pip3 install cffi
python build_mac.py
pyenv global 3.7.5
pip3 install cffi
python build_mac.py
pyenv global 3.6.9
pip3 install cffi
python build_mac.py
