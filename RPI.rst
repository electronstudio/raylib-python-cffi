Raspberry Pi
====================

Please use Raspberry Pi OS Bullseye.  Older OSes are not tested.

We have published a binary wheel using Raylib in X11 mode.  This *should* install and work on Bullseye
with

::

    python3.9 -m pip install raylib==4.2.1.2

If it doesn't work, or we haven't published a binary wheel for the latest version,
or if you want to use Raylib in ``PLATFORM_DRM`` mode, you will need to compile your own raylib.
For full instructins on this, see https://github.com/raysan5/raylib/wiki/Working-on-Raspberry-Pi .  If you need help with this ask Raylib.

This 'worked for me':

::

    git clone https://github.com/raysan5/raylib.git --branch 4.2.0 --single-branch
    cd raylib
    mkdir build
    cd build
    cmake -DPLATFORM="DRM" -DINCLUDE_EVERYTHING=on -DSUPPORT_FILEFORMAT_JPG=on -DWITH_PIC=on -DCMAKE_BUILD_TYPE=Release ..
    make
    sudo make install
    
Then have pip compile the wheel:

::

    pip3 install setuptools
    pip3 install --no-cache-dir --no-binary raylib --upgrade --force-reinstall raylib==4.2.1.2

(or newer version)

.. attention::

    The Broadcom proprietary Open GL ES 2.0 drivers (installed by Raspbian into ``/opt/vc`` and compiled in Raylib
    with ``PLATFORM_RPI``) do not work with Bullseye and have not been tested with the bindings.  They will probably
    require additional linker arguments to be added to ``build.py``.  Suggest you use ``PLATFORM_DRM`` instead.
