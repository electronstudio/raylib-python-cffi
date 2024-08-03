Raspberry Pi
====================

Please use Raspberry Pi OS Bookworm.  Bullseye should also work.  Older OSes are not tested.

Option 1: Binary wheel
----------------------

We have published binary wheels compiled for 64-bit Raspberry OS Bullseye in X11 mode.

::

    python -m pip install --break-system-packages raylib

If it doesn't work, or you're not on Bullseye, or you're 32 bit, or if you want to use Raylib in ``PLATFORM_DRM`` mode, you will need to compile your own raylib.  See below.
For full instructions on this, see https://github.com/raysan5/raylib/wiki/Working-on-Raspberry-Pi .  If you need help with this ask Raylib.

Option 2: Compile Raylib from source X11 mode
---------------------------------------------

This should work for everyone.

::

    sudo apt update
    sudo apt install python3-pip cmake libegl1-mesa-dev libgbm-dev libgles2-mesa-dev libdrm-dev libglfw3-dev
    git clone https://github.com/raysan5/raylib.git --branch 5.0 --single-branch
    cd raylib
    mkdir build
    rm -rf build/*
    cd build
    cmake -DPLATFORM="Desktop" -DOPENGL_VERSION=2.1 -DBUILD_EXAMPLES=OFF -DCUSTOMIZE_BUILD=ON -DSUPPORT_FILEFORMAT_JPG=ON -DSUPPORT_FILEFORMAT_FLAC=ON -DWITH_PIC=ON -DCMAKE_BUILD_TYPE=Release ..
    make
    sudo make install
    sudo cp -r ../src/external/glfw/include/GLFW /usr/local/include/

Then have pip compile and install the wheel:

::

    python3 -m pip install --break-system-packages setuptools
    python3 -m pip install --no-cache-dir --no-binary raylib --upgrade --force-reinstall --break-system-packages raylib==5.0.0.3

Option 3: Compile Raylib from source DRM mode
---------------------------------------------

This seems to work on Raspberry Pi 4.  Note you must not be running X11 when you run your programs.

If you have ever installed Raylib or raylib-python-cffi before, remove all traces of it:

::

    sudo apt remove raylib raylib-dev libraylib libraylib-dev
    sudo rm /usr/local/lib/pkgconfig/raylib.pc
    sudo rm -rf /usr/local/lib/libraylib.* /usr/lib/libraylib.*

Remove all GLFW:

::

    sudo apt remove libglfw3-dev libglfw3
    sudo rm -rf /usr/local/include/GLFW

Build a shared lib version of Raylib in DRM mode and install to /usr:

::

    sudo apt update
    sudo apt install python3-pip cmake libegl1-mesa-dev libgbm-dev libgles2-mesa-dev libdrm-dev
    git clone https://github.com/raysan5/raylib.git --branch 5.0 --single-branch
    cd raylib
    mkdir build
    rm rf build/*
    cd build
    cmake -DPLATFORM="DRM" -DBUILD_EXAMPLES=OFF -DCUSTOMIZE_BUILD=ON -DSUPPORT_FILEFORMAT_JPG=ON -DSUPPORT_FILEFORMAT_FLAC=ON -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
    make
    sudo make install

    
Then have pip compile and install the wheel:

::

    python3 -m pip install --break-system-packages setuptools
    python3 -m pip install --no-cache-dir --no-binary raylib --upgrade --force-reinstall --break-system-packages raylib==5.0.0.3




.. attention::

    If you intend to use the Broadcom proprietary Open GL ES 2.0 drivers (the ones installed by Raspbian into ``/opt/vc`` and compiled in Raylib
    with ``PLATFORM_RPI``) be aware they not work with Bullseye and have not been tested with the bindings.  They will probably
    require additional linker arguments to be added to ``build.py``.  Suggest you try ``PLATFORM_DRM`` instead.
