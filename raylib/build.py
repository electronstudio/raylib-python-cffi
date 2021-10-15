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
import subprocess

ffibuilder = FFI()


def get_the_include_path():
    return subprocess.run(['pkg-config', '--variable=includedir', 'raylib'], stdout=subprocess.PIPE).stdout.decode(
        'utf-8').strip()


def get_the_lib_path():
    return subprocess.run(['pkg-config', '--variable=libdir', 'raylib'], stdout=subprocess.PIPE).stdout.decode(
        'utf-8').strip()


ffi_includes = """
#include "raylib.h"
#define RAYGUI_IMPLEMENTATION
#define RAYGUI_SUPPORT_RICONS
#include "raygui.h"
#define PHYSAC_IMPLEMENTATION
#include "physac.h"
"""


def mangle(file):
    result = ""
    skip = False
    for line in open(file):
        line = line.strip().replace("va_list", "void *") + "\n"
        if skip:
            if line.startswith("#endif"):
                skip = False
            continue
        if line.startswith("#if defined(__cplusplus)"):
            skip = True
            continue
        if line.startswith("#endif // RAYGUI_H"):
            break
        if line.startswith("#"):
            continue
        if line.startswith("RLAPI"):
            line = line.replace('RLAPI ', '')
        if line.startswith("RAYGUIDEF"):
            line = line.replace('RAYGUIDEF ', '')
        if line.startswith("PHYSACDEF"):
            line = line.replace('PHYSACDEF ', '')
        result += line
        # print(line)
    return result


def build_linux():
    print("BUILDING FOR LINUX")
    ffibuilder.cdef(mangle(get_the_include_path() + "/raylib.h"))
    ffibuilder.cdef(open("raylib/raygui_modified.h").read().replace('RAYGUIDEF ', ''))
    ffibuilder.cdef(open("raylib/physac_modified.h").read().replace('PHYSACDEF ', ''))
    ffibuilder.set_source("raylib._raylib_cffi", ffi_includes,
                          extra_link_args=[get_the_lib_path() + '/libraylib.a', '-lm', '-lpthread', '-lGLU', '-lGL',
                                           '-lrt',
                                           '-lm', '-ldl', '-lX11', '-lpthread'],
                          libraries=['GL', 'm', 'pthread', 'dl', 'rt', 'X11'],
                          include_dirs=['raylib']
                          )
    if __name__ == "__main__":
        ffibuilder.compile(verbose=True)


def build_windows():
    print("BUILDING FOR WINDOWS")
    ffibuilder.cdef(mangle("raylib/raylib.h"))
    ffibuilder.cdef(open("raylib/raygui_modified.h").read().replace('RAYGUIDEF ', '').replace('bool', 'int'))
    ffibuilder.cdef(open("raylib/physac_modified.h").read().replace('PHYSACDEF ', '').replace('bool', 'int'))
    ffibuilder.set_source("raylib._raylib_cffi", ffi_includes,
                          extra_link_args=['/NODEFAULTLIB:MSVCRTD'],
                          libraries=['raylib', 'gdi32', 'shell32', 'user32', 'OpenGL32', 'winmm'],
                          include_dirs=['raylib'],
                          )
    if __name__ == "__main__":
        ffibuilder.compile(verbose=True)


def build_mac():
    print("BUILDING FOR MAC")
    ffibuilder.cdef(mangle(get_the_include_path() + "/raylib.h"))
    ffibuilder.cdef(open("raylib/raygui_modified.h").read().replace('RAYGUIDEF ', ''))
    ffibuilder.cdef(open("raylib/physac_modified.h").read().replace('PHYSACDEF ', ''))
    ffibuilder.set_source("raylib._raylib_cffi", ffi_includes,
                          extra_link_args=[get_the_lib_path() + '/libraylib.a', '-framework', 'OpenGL', '-framework', 'Cocoa',
                                           '-framework', 'IOKit', '-framework', 'CoreFoundation', '-framework',
                                           'CoreVideo'],
                          include_dirs=['raylib'],
                          )

    if __name__ == "__main__":
        ffibuilder.compile(verbose=True)


def build_rpi_nox():
    print("BUILDING FOR RASPBERRY PI")
    ffibuilder.cdef(mangle(get_the_include_path() + "/raylib.h"))
    ffibuilder.cdef(open("raylib/raygui_modified.h").read().replace('RAYGUIDEF ', ''))
    ffibuilder.cdef(open("raylib/physac_modified.h").read().replace('PHYSACDEF ', ''))
    ffibuilder.set_source("raylib._raylib_cffi", ffi_includes,
                          extra_link_args=[get_the_lib_path() + '/libraylib.a',
                                           '/opt/vc/lib/libEGL_static.a', '/opt/vc/lib/libGLESv2_static.a',
                                           '-L/opt/vc/lib', '-lvcos', '-lbcm_host', '-lbrcmEGL', '-lbrcmGLESv2',
                                           '-lm', '-lpthread', '-lrt'],
                          include_dirs=['raylib'],
                          )

    if __name__ == "__main__":
        ffibuilder.compile(verbose=True)


if platform.system() == "Darwin":
    build_mac()
elif platform.system() == "Linux":
    if "x86" in platform.machine():
        build_linux()
    elif "arm" in platform.machine():
        build_rpi_nox()
elif platform.system() == "Windows":
    build_windows()
else:
    print("WARNING: UKKNOWN PLATFORM - trying Linux build")
    build_linux()
