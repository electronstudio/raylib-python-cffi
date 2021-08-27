## Have Pip build from source

Useful if the binaries don't work on your system.

Make sure Raylib is installed and then:

    pip3 install --no-binary raylib --upgrade --force-reinstall raylib

## Build from source manually

Useful if the Pip build doesn't work, or you want to contribute to the project, or you want to skip building the
static lib and just *use the dynamic binding with your own dll*.

If you do build on a new platform please
submit your binaries as a PR.



### Windows manual build

Clone this repo including submodules so you get correct version of Raylib.

    git clone --recurse-submodules https://github.com/electronstudio/raylib-python-cffi

Open Visual C++ command shell.

Fix the symlink that doesnt work on Windows

    cd raylib-python-cffi
    copy raylib-c\src\raylib.h raylib\raylib.h

Build and install Raylib from the raylib-c directory.

    cd raylib-python-cffi/raylib-c
    mkdir build
    cd build
    cmake -DWITH_PIC=on -DCMAKE_BUILD_TYPE=Release ..
    msbuild raylib.sln /target:raylib /property:Configuration=Release
    copy raylib\Release\raylib.lib ..\..
    cd ..\..

To update the dynamic libs, download the official release, e.g. https://github.com/raysan5/raylib/releases/download/3.7.0/raylib-3.7.0_win64_msvc16.zip and extract `raylib.dll`
into `raylib/dynamic`.  Delete the files for other platforms, unless you want them in your distribution.

To build a binary wheel distribution:

    rmdir /Q /S build
    pip3 install cffi
    pip3 install wheel
    python setup.py bdist_wheel

and install it:

    pip3 install dist\raylib-3.7.0-cp37-cp37m-win_amd64.whl

(Note: your wheel's filename will probably be different than the one here.)

### Linux etc manual build

These instructions have been tested on Ubuntu 20.10 and 16.04.  Mac should be very similar.

Clone this repo including submodules so you get correct version of Raylib.

    git clone --recurse-submodules https://github.com/electronstudio/raylib-python-cffi

Build and install Raylib from the raylib-c directory.

    sudo apt install libasound2-dev mesa-common-dev libx11-dev libxrandr-dev libxi-dev xorg-dev libgl1-mesa-dev libglu1-mesa-dev
    cd raylib-python-cffi/raylib-c
    mkdir build
    cd build
    cmake -DWITH_PIC=on -DCMAKE_BUILD_TYPE=Release ..
    sudo make install

Optional: Build the Raylib shared libs, if you plan to use `raylib.dynamic` binding.

    rm -rf *
    cmake -DWITH_PIC=on -DBUILD_SHARED_LIBS=on -DCMAKE_BUILD_TYPE=Release ..
    sudo make install

Optional: Make a patched version of raylib header.  (**Not necessary** if you've already got 
raylib_modifed.h from repo and haven't changed anything.)

    cd ../../raylib
    cp raylib.h raylib_modified.h
    patch  -p0 <raylib_modified.h.patch


Build

    pip3 install cffi
    cd ..
    rm -rf build raylib/static/_raylib_cffi.*
    python3 raylib/static/build.py


To update the Linux dynamic libs (names will be different on other platfroms):

    rm raylib/dynamic/*.so*
    cp -P /usr/local/lib/libraylib.so* raylib/dynamic/

To build a binary wheel distribution:

    pip3 install wheel
    python3 setup.py bdist_wheel

and install it:

    pip3 install dist/raylib*.whl

To build a complete set of libs for Python 3.6, 3.7, 3.8 and 3.9:

    ./raylib/static/build_multi.sh

(NOTE pypi wont accept Linux packages unless they are built `--plat-name manylinux2014_x86_64` so on linux
please run `./raylib/static/build_multi_linux.sh` )

(TODO move the dynamic libs into a separate package rather than include them with every one.)

### Raspberry Pi

The integrated GPU hardware in a Raspberry Pi ("VideoCore") is rather
idiosyncratic, resulting in a complex set of software options. Probably the
most interesting two options for Raylib applications are:

1. Use the Broadcom proprietary Open GL ES 2.0 drivers, installed by Raspbian
   into `/opt/vc`. These are 32-bit only, and currently X11 doesn't use these
   for its acceleration, so this is most suitable for driving the entire HDMI
   output from one application with minimal overhead (no X11).

2. Use the more recent open-source `vc4-fkms-v3d` kernel driver. This can run
   in either 32-bit or 64-bit, and X11 can use these, so using X11 is probably
   the more common choice here.

With option 2, the regular linux install instructions above should probably
work as-is.

For option 1, then also follow the above instructions, but with these
modifications:

- With `cmake`, use `cmake -DWITH_PIC=on -DSTATIC=on -DSHARED=on -DPLATFORM='Raspberry Pi' ..`

(See [here](https://github.com/electronstudio/raylib-python-cffi/issues/31#issuecomment-862078330) for a Raspberry Pi wheel)