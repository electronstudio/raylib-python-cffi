#!/usr/bin/env bash
if ! command -v pyenv &> /dev/null
then
    echo "Pyenv required: https://github.com/pyenv/pyenv-installer"
    exit
fi

pyenv update

function build() {
    echo "Building for Python $1"
    pyenv install -s $1
    pyenv global $1
    pip3 install cffi
    pip3 install wheel
    rm -rf raylib/_raylib_cffi.* build
    python setup.py bdist_wheel --plat-name manylinux2014_armv7l
}

build 3.9.5
build 3.8.10
build 3.7.10
build 3.6.13

