#!/usr/bin/env bash
if ! command -v pyenv &> /dev/null
then
    echo "Pyenv required: https://github.com/pyenv/pyenv-installer"
    exit
fi
rm *arm-linux-gnueabihf.so
pyenv install -s 3.9.1
pyenv global 3.9.1
pip3 install cffi
python3 build_rpi_nox.py
pyenv install -s 3.8.7
pyenv global 3.8.7
pip3 install cffi
python3 build_rpi_nox.py
pyenv install -s 3.7.9
pyenv global 3.7.9
pip3 install cffi
python3 build_rpi_nox.py
pyenv install -s 3.6.12
pyenv global 3.6.12
pip3 install cffi
python3 build_rpi_nox.py
