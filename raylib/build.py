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
import time

ffibuilder = FFI()

def check_raylib_installed():
    return subprocess.run(['pkg-config', '--exists', 'raylib'], text=True, stdout=subprocess.PIPE).returncode == 0

def get_the_include_path():
    return subprocess.run(['pkg-config', '--variable=includedir', 'raylib'], text=True, stdout=subprocess.PIPE).stdout.strip()


def get_the_lib_path():
    return subprocess.run(['pkg-config', '--variable=libdir', 'raylib'], text=True, stdout=subprocess.PIPE).stdout.strip()


def pre_process_header(filename):
    print("Pre-processing "+filename)
    file = open(filename, "r")
    filetext = "".join([ line for line in file if '#include' not in line])
    command =['gcc', '-CC', '-P' ,'-undef', '-nostdinc', '-DRLAPI=', '-DPHYSACDEF=', '-DRAYGUIDEF=',
               '-dDI', '-E', '-']
    filetext2 = subprocess.run(command, text=True, input=filetext, stdout=subprocess.PIPE).stdout
    filetext3 = filetext2.replace("va_list", "void *")
    filetext4 = "\n".join([ line for line in filetext3.splitlines() if not line.startswith("#")])
    #print(r)
    return filetext4

def check_header_exists(file):
    if not os.path.isfile(file):
        print("\n\n*************** WARNING ***************\n\n")
        print(file+" not found.  Build will not contain these extra functions.\n\nPlease copy file from src/extras to "+file+" if you want them.\n\n")
        print("**************************************\n\n")
        time.sleep(1)
        return False
    return True

def mangle(string):
    return string

if not check_raylib_installed():
    raise Exception("ERROR: raylib not found by pkg-config.  Please install pkg-config and Raylib.")

raylib_h = get_the_include_path() + "/raylib.h"

if not os.path.isfile(raylib_h):
    raise Exception("ERROR: "+raylib_h+" not found.  Please install Raylib.")




ffi_includes = """
#include "raylib.h"
"""

raygui_h = get_the_include_path() + "/raygui.h"
if check_header_exists(raygui_h):
    ffi_includes += """
    #define RAYGUI_IMPLEMENTATION
    #define RAYGUI_SUPPORT_RICONS
    #include "raygui.h"
    """


physac_h = get_the_include_path() + "/physac.h"
if check_header_exists(physac_h):
    ffi_includes += """
    #define PHYSAC_IMPLEMENTATION
    #include "physac.h"
    """







def build_linux():
    print("BUILDING FOR LINUX")
    ffibuilder.cdef(pre_process_header(raylib_h))
    if os.path.isfile(raygui_h):
        ffibuilder.cdef(pre_process_header(raygui_h))
    if os.path.isfile(physac_h):
        ffibuilder.cdef(pre_process_header(physac_h))
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
    ffibuilder.cdef(open("raylib/raygui_modified.h").read().replace('RAYGUIDEF ', ''))
    ffibuilder.cdef(open("raylib/physac_modified.h").read().replace('PHYSACDEF ', ''))
    ffibuilder.set_source("raylib._raylib_cffi", ffi_includes,
                          extra_link_args=['/NODEFAULTLIB:MSVCRTD'],
                          libraries=['raylib', 'gdi32', 'shell32', 'user32', 'OpenGL32', 'winmm'],
                          include_dirs=['raylib'],
                          )
    if __name__ == "__main__":
        ffibuilder.compile(verbose=True)


def build_mac():
    print("BUILDING FOR MAC")
    ffibuilder.cdef(pre_process_header(raylib_h))
    if os.path.isfile(raygui_h):
        ffibuilder.cdef(pre_process_header(raygui_h))
    if os.path.isfile(physac_h):
        ffibuilder.cdef(pre_process_header(physac_h))
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
    ffibuilder.cdef(pre_process_header(raylib_h))
    if os.path.isfile(raygui_h):
        ffibuilder.cdef(pre_process_header(raygui_h))
    if os.path.isfile(physac_h):
        ffibuilder.cdef(pre_process_header(physac_h))
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
