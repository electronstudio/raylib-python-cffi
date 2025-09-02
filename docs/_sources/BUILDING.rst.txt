Building from source
====================

Have Pip build from source
--------------------------

This is useful if the binaries don’t work on your system, or you want to use a newer version of Raylib, or compile
Raylib with a different version of OpenGL than the default.  (e.g. on old hardware use cmake option ``-DOPENGL_VERSION=1.1``)

First make sure Raylib is installed.  On Linux/Mac it must include the pkg-config files.  Best way to ensure this
is to compile and install Raylib using CMake: https://github.com/raysan5/raylib/wiki/Working-on-GNU-Linux#build-raylib-using-cmake

Requirements for build: cmake, pkg-config.

::

        wget https://github.com/raysan5/raylib/archive/refs/tags/5.5.zip
        unzip 5.5.zip
        cd raylib-5.5
        mkdir build
        cd build
        cmake  -DCUSTOMIZE_BUILD=ON -DSUPPORT_FILEFORMAT_JPG=ON -DSUPPORT_FILEFORMAT_FLAC=ON -DWITH_PIC=ON -DCMAKE_BUILD_TYPE=Release ..
        make
        sudo make install
        export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

Then ask Pip to build from source:

::

   pip3 install --no-cache-dir --no-binary raylib --upgrade --force-reinstall raylib

Environment variables (new in 5.5.0.3)
--------------------------------------

If pkg-config doesn't work you can manually set these environment variables:

``RAYLIB_PLATFORM``: Any one of: ``Desktop``, ``SDL``, ``DRM``, ``PLATFORM_COMMA``

``RAYLIB_LINK_ARGS``: Arguments to pass to the linker rather than getting them from pkg-config.
e.g.: ``"-L/usr/local/lib -lraylib"``

``RAYLIB_INCLUDE_PATH``: Directory to find raylib.h rather than getting from pkg-config.
e.g.: ``/usr/local/include``

``RAYGUI_INCLUDE_PATH``: Directory to find raygui.h
e.g.: ``/usr/local/include``

``GLFW_INCLUDE_PATH``: Directory to find glfw3.h
e.g.: ``/usr/local/include/GLFW``

``PHYSAC_INCLUDE_PATH``: Directory to find physac.h
e.g.: ``/usr/local/include``

``LIBFFI_INCLUDE_PATH``:
e.g.: ``/usr/local/include``

You can also override which package names pkg-config will search for:

``PKG_CONFIG_LIB_raylib``: the package to request from pkg-config for raylib include files, default ``raylib``

``PKG_CONFIG_LIB_raygui``: the package to request from pkg-config for raygui include files
set to ``raygui``` if you have a separate raygui package, else unset for default ``raylib``

``PKG_CONFIG_LIB_physac``: the package to request from pkg-config for physac include files
set to ``physac``` if you have a separate physac package, else unset for default ``raylib``

``PKG_CONFIG_LIB_glfw3``: the package to request from pkg-config for glfw3 include files
set to ``glfw3`` if you have a separate glfw3 package, else unset for default ``raylib``

``PKG_CONFIG_LIB_libffi``: the package to request from pkg-config for libffi include files


Or, Build from source manually
------------------------------

Useful if the Pip build doesn’t work and you want to debug it, or you want to contribute to the
project.

.. attention::
   If the Pip build doesn’t work, please submit a bug. (And if you have
   fixed it, a PR.)

Manual instructions follow, but are probably outdated, so see instead how we actually build the wheels
at https://github.com/electronstudio/raylib-python-cffi/blob/master/.github/workflows/build.yml

Windows manual build
~~~~~~~~~~~~~~~~~~~~

Clone this repo including submodules so you get correct version of
Raylib.

::

   git clone --recurse-submodules https://github.com/electronstudio/raylib-python-cffi

Open Visual C++ command shell.

Fix the symlink that doesnt work on Windows

::

   cd raylib-python-cffi
   copy raylib-c\src\raylib.h raylib\raylib.h

Build and install Raylib from the raylib-c directory.

::

   cd raylib-python-cffi/raylib-c
   mkdir build
   cd build
   cmake -DWITH_PIC=on -DCMAKE_BUILD_TYPE=Release ..
   msbuild raylib.sln /target:raylib /property:Configuration=Release
   copy raylib\Release\raylib.lib ..\..
   cd ..\..



To build a binary wheel distribution:

::

   rmdir /Q /S build
   pip3 install cffi
   pip3 install wheel
   python setup.py bdist_wheel

Then install it:

::

   pip3 install dist\raylib-3.7.0-cp37-cp37m-win_amd64.whl

(Note: your wheel’s filename will probably be different than the one
here.)

Linux manual build
~~~~~~~~~~~~~~~~~~~~~~

Clone this repo including submodules so you get correct version of
Raylib.

::

   git clone --recurse-submodules https://github.com/electronstudio/raylib-python-cffi

Build and install Raylib from the raylib-c directory.

.. note::
   You can instead use a different version of Raylib you installed from elsewhere, and it should still
   work!

::

   sudo apt install cmake libasound2-dev mesa-common-dev libx11-dev libxrandr-dev libxi-dev xorg-dev libgl1-mesa-dev libglu1-mesa-dev pkg-config cmake
   cd raylib-python-cffi/raylib-c
   mkdir build
   cd build
   cmake -DCUSTOMIZE_BUILD=ON -DSUPPORT_FILEFORMAT_JPG=ON -DSUPPORT_FILEFORMAT_FLAC=ON -DWITH_PIC=ON -DCMAKE_BUILD_TYPE=Release ..
   sudo make install
   export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

.. note:: Optional: Build the Raylib shared libs, if you plan to use
   ``raylib_dynamic`` binding.

   ::

      rm -rf *
      cmake -DWITH_PIC=on -DBUILD_SHARED_LIBS=on -DCMAKE_BUILD_TYPE=Release ..
      make
      sudo make install

::

   cd ../..


Build the Python library:

::

   pip3 install cffi
   rm -rf build raylib/_raylib_cffi.*
   python3 raylib/build.py

..  note:: (Optional) To update the Linux dynamic libs (names will be different on other platforms):

    ::

       rm dynamic/raylib/*.so*
       cp -P /usr/local/lib/libraylib.so* dynamic/raylib/

To build a binary wheel distribution:

::

   pip3 install wheel
   python3 setup.py bdist_wheel


Then install it:

::

   pip3 install dist/raylib*.whl

To build a complete set of libs for Python 3.6, 3.7, 3.8 and 3.9:

::

   ./raylib/build_multi.sh

.. warning::
   pypi wont accept Linux packages unless they are built
   ``--plat-name manylinux2014_x86_64`` so on linux please run
   ``./raylib/build_multi_linux.sh`` )

.. TODO::
   Separate the instructions for preparing the dynamic module
   from the instructions for building the static module!



Macos manual build
~~~~~~~~~~~~~~~~~~~~~~

These instructions have been tested on Macos 10.14.

Clone this repo including submodules so you get correct version of
Raylib.

::

   git clone --recurse-submodules https://github.com/electronstudio/raylib-python-cffi

Build and install Raylib from the raylib-c directory.

::

    cd raylib-python-cffi/raylib-c/
    mkdir build
    cd build
    cmake -DWITH_PIC=on -DCMAKE_BUILD_TYPE=Release ..
    make
    sudo make install
    cd ../..


Build and install module.

::

   pip3 install cffi
   rm -rf build raylib/_raylib_cffi.*
   python3 raylib/build.py
   pip3 install wheel
   python3 setup.py install


