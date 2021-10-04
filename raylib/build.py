#  Copyright (c) 2021 Richard Smith and others
#
#  This program and the accompanying materials are made available under the
#  terms of the Eclipse Public License 2.0 which is available at
#  http://www.eclipse.org/legal/epl-2.0.
#
#  This Source Code may also be made available under the following Secondary
#  licenses when the conditions for such availability set forth in the Eclipse
#  Public License, v. 2.0 are satisfied: GNU General Public License, version 2
#  with the GNU Classpath Exception which is
#  available at https://www.gnu.org/software/classpath/license.html.
#
#  SPDX-License-Identifier: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0

# Assumes raylib, GL, etc are all already installed as system libraries.  We dont distribute them.
# Raylib must be installed and compiled with:  cmake -DWITH_PIC=ON -DSHARED=ON -DSTATIC=ON ..

# We use /usr/local/lib/libraylib.a to ensure we link to static version

from cffi import FFI
import os
import platform
import sys

ffibuilder = FFI()

def build_linux():
    print("BUILDING FOR LINUX")
    ffibuilder.cdef(open("raylib/raylib_modified.h").read().replace('RLAPI ', ''))
    ffibuilder.set_source("raylib._raylib_cffi",
                          """
                               #include "raylib.h"
                          """,
                          extra_link_args=['/usr/local/lib/libraylib.a','-lm', '-lpthread', '-lGLU', '-lGL',  '-lrt', '-lm', '-ldl', '-lX11', '-lpthread'],
                          libraries=['GL','m','pthread', 'dl', 'rt', 'X11']
                          )
    if __name__ == "__main__":
        ffibuilder.compile(verbose=True)

def build_windows():
    print("BUILDING FOR WINDOWS")
    ffibuilder.cdef(open("raylib/raylib_modified.h").read().replace('RLAPI ', '').replace('bool','int'))
    ffibuilder.set_source("raylib._raylib_cffi",
                          """
                          #include "../../../raylib/raylib.h"   
                          """,
                          extra_link_args=['/NODEFAULTLIB:MSVCRTD'],
                          libraries=['raylib', 'gdi32', 'shell32', 'user32','OpenGL32', 'winmm'],
                          )
    if __name__ == "__main__":
        ffibuilder.compile(verbose=True)

def build_mac():
    print("BUILDING FOR MAC")
    ffibuilder.cdef(open("raylib/raylib_modified.h").read().replace('RLAPI ', ''))
    ffibuilder.set_source("raylib._raylib_cffi",
                          """
                               #include "../../raylib/raylib.h"   // the C header of the library, supplied by us here
                          """,
                          extra_link_args=['/usr/local/lib/libraylib.a', '-framework', 'OpenGL', '-framework', 'Cocoa', '-framework', 'IOKit', '-framework', 'CoreFoundation', '-framework', 'CoreVideo'],
                          )

    if __name__ == "__main__":
        ffibuilder.compile(verbose=True)


def build_rpi_nox():
    print("BUILDING FOR RASPBERRY PI")
    ffibuilder.cdef(open("raylib/raylib_modified.h").read().replace('RLAPI ', ''))
    ffibuilder.set_source("raylib._raylib_cffi",
                          """
                               #include "../../raylib/raylib.h"
                          """,
                          extra_link_args=['/usr/local/lib/libraylib.a',
                                           '/opt/vc/lib/libEGL_static.a', '/opt/vc/lib/libGLESv2_static.a',
                                           '-L/opt/vc/lib', '-lvcos', '-lbcm_host', '-lbrcmEGL', '-lbrcmGLESv2',
                                           '-lm', '-lpthread', '-lrt'],
                          )


    if __name__ == "__main__":
        ffibuilder.compile(verbose=True)



if platform.system()=="Darwin":
    build_mac()
elif platform.system()=="Linux":
    if "x86" in platform.machine():
        build_linux()
    elif "arm" in platform.machine():
        build_rpi_nox()
elif platform.system()=="Windows":
    build_windows()
else:
    print("WARNING: UKKNOWN PLATFORM - trying Linux build")
    build_linux()