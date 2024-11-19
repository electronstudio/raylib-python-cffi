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
import re

from cffi import FFI
import os
import platform
import sys
import subprocess
import time

RAYLIB_PLATFORM = os.getenv("RAYLIB_PLATFORM", "Desktop")

def check_raylib_installed():
    return subprocess.run(['pkg-config', '--exists', 'raylib'], text=True, stdout=subprocess.PIPE).returncode == 0

def check_SDL_installed():
    return subprocess.run(['pkg-config', '--exists', 'sdl2'], text=True, stdout=subprocess.PIPE).returncode == 0

def get_the_include_path():
    return subprocess.run(['pkg-config', '--variable=includedir', 'raylib'], text=True,
                          stdout=subprocess.PIPE).stdout.strip()


def get_the_lib_path():
    return subprocess.run(['pkg-config', '--variable=libdir', 'raylib'], text=True,
                          stdout=subprocess.PIPE).stdout.strip()

def get_lib_flags():
    return subprocess.run(['pkg-config', '--libs', 'raylib'], text=True,
                          stdout=subprocess.PIPE).stdout.strip().split()

def pre_process_header(filename, remove_function_bodies=False):
    print("Pre-processing " + filename)
    file = open(filename, "r")
    filetext = "".join([line for line in file if '#include' not in line])
    command = ['gcc', '-CC', '-P', '-undef', '-nostdinc', '-DRL_MATRIX_TYPE',
               '-DRL_QUATERNION_TYPE','-DRL_VECTOR4_TYPE','-DRL_VECTOR3_TYPE','-DRL_VECTOR2_TYPE',
               '-DRLAPI=', '-DPHYSACDEF=', '-DRAYGUIDEF=','-DRMAPI=',
               '-dDI', '-E', '-']
    filetext = subprocess.run(command, text=True, input=filetext, stdout=subprocess.PIPE).stdout
    filetext = filetext.replace("va_list", "void *")
    if remove_function_bodies:
        filetext = re.sub('\n{\n(.|\n)*?\n}\n', ';', filetext)
    filetext = "\n".join([line for line in filetext.splitlines() if not line.startswith("#")])
    file = open("raylib/"+os.path.basename(filename)+".modified", "w")
    file.write(filetext)
    # print(r)
    return filetext


def check_header_exists(file):
    if not os.path.isfile(file):
        print("\n\n*************** WARNING ***************\n\n")
        print(
            file + " not found.  Build will not contain these extra functions.\n\nPlease copy file from src/extras to " + file + " if you want them.\n\n")
        print("**************************************\n\n")
        time.sleep(1)
        return False
    return True


# def mangle(file):
#     result = ""
#     skip = False
#     for line in open(file):
#         line = line.strip().replace("va_list", "void *") + "\n"
#         if skip:
#             if line.startswith("#endif"):
#                 skip = False
#             continue
#         if line.startswith("#if defined(__cplusplus)"):
#             skip = True
#             continue
#         if line.startswith("#endif // RAYGUI_H"):
#             break
#         if line.startswith("#"):
#             continue
#         if line.startswith("RLAPI"):
#             line = line.replace('RLAPI ', '')
#         if line.startswith("RAYGUIDEF"):
#             line = line.replace('RAYGUIDEF ', '')
#         if line.startswith("PHYSACDEF"):
#             line = line.replace('PHYSACDEF ', '')
#         result += line
#         # print(line)
#     return result


def build_unix():
    if not check_raylib_installed():
        raise Exception("ERROR: raylib not found by pkg-config.  Please install pkg-config and Raylib.")

    if RAYLIB_PLATFORM=="SDL" and not check_SDL_installed():
        raise Exception("ERROR: SDL2 not found by pkg-config.  Please install pkg-config and SDL2.")

    raylib_h = get_the_include_path() + "/raylib.h"
    rlgl_h = get_the_include_path() + "/rlgl.h"
    raymath_h = get_the_include_path() + "/raymath.h"

    if not os.path.isfile(raylib_h):
        raise Exception("ERROR: " + raylib_h + " not found.  Please install Raylib.")

    if not os.path.isfile(rlgl_h):
        raise Exception("ERROR: " + rlgl_h + " not found.  Please install Raylib.")

    if not os.path.isfile(raymath_h):
        raise Exception("ERROR: " + raylib_h + " not found.  Please install Raylib.")

    ffi_includes = """
    #include "raylib.h"
    #include "rlgl.h"
    #include "raymath.h"
    """

    glfw3_h = get_the_include_path() + "/GLFW/glfw3.h"
    if RAYLIB_PLATFORM=="Desktop" and check_header_exists(glfw3_h):
        ffi_includes += """
        #include "GLFW/glfw3.h"
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

    ffibuilder.cdef(pre_process_header(raylib_h))
    ffibuilder.cdef(pre_process_header(rlgl_h))
    ffibuilder.cdef(pre_process_header(raymath_h, True))

    if os.path.isfile(raygui_h):
        ffibuilder.cdef(pre_process_header(raygui_h))
    if os.path.isfile(physac_h):
        ffibuilder.cdef(pre_process_header(physac_h))
    if RAYLIB_PLATFORM=="Desktop" and os.path.isfile(glfw3_h):
        ffibuilder.cdef(pre_process_header(glfw3_h))


    if platform.system() == "Darwin":
        print("BUILDING FOR MAC")
        extra_link_args = [get_the_lib_path() + '/libraylib.a', '-framework', 'OpenGL', '-framework', 'Cocoa',
                           '-framework', 'IOKit', '-framework', 'CoreFoundation', '-framework',
                           'CoreVideo']
        if RAYLIB_PLATFORM=="SDL":
            extra_link_args += ['/usr/local/lib/libSDL2.a', '-framework', 'CoreHaptics', '-framework', 'ForceFeedback',
            '-framework', 'GameController']
        libraries = []
        extra_compile_args = ["-Wno-error=incompatible-function-pointer-types", "-D_CFFI_NO_LIMITED_API"]
    else:  #platform.system() == "Linux":
        print("BUILDING FOR LINUX")
        extra_link_args = get_lib_flags() + [ '-lm', '-lpthread', '-lGL',
                                              '-lrt', '-lm', '-ldl', '-lpthread', '-latomic']
        if RAYLIB_PLATFORM=="SDL":
            extra_link_args += ['-lX11','-lSDL2']
        elif RAYLIB_PLATFORM=="DRM":
            extra_link_args += ['-lEGL', '-lgbm']
        else:
            extra_link_args += ['-lX11']
        extra_compile_args = ["-Wno-incompatible-pointer-types", "-D_CFFI_NO_LIMITED_API"]
        libraries = [] # Not sure why but we put them in extra_link_args instead so *shouldnt* be needed here


    print("extra_link_args: "+str(extra_link_args))
    print("extra_compile_args: "+str(extra_compile_args))
    print("libraries: "+str(libraries))
    ffibuilder.set_source("raylib._raylib_cffi",
                          ffi_includes,
                          py_limited_api=False,
                          include_dirs=[get_the_include_path()],
                          extra_link_args=extra_link_args,
                          extra_compile_args=extra_compile_args,
                          libraries=libraries)


def build_windows():
    print("BUILDING FOR WINDOWS")
    ffibuilder.cdef(open("raylib/raylib.h.modified").read())
    if RAYLIB_PLATFORM=="Desktop":
        ffibuilder.cdef(open("raylib/glfw3.h.modified").read())
    ffibuilder.cdef(open("raylib/rlgl.h.modified").read())
    ffibuilder.cdef(open("raylib/raygui.h.modified").read())
    ffibuilder.cdef(open("raylib/physac.h.modified").read())
    ffibuilder.cdef(open("raylib/raymath.h.modified").read())

    ffi_includes = """
    #include "raylib.h"
    #include "rlgl.h"
    #include "raymath.h"
    """

    if RAYLIB_PLATFORM=="Desktop":
        ffi_includes += """
        #include "GLFW/glfw3.h"
        """

    ffi_includes += """
    #define RAYGUI_IMPLEMENTATION
    #define RAYGUI_SUPPORT_RICONS
    #include "raygui.h"
    #define PHYSAC_IMPLEMENTATION
    #include "physac.h"
    """
    libraries = ['raylib', 'gdi32', 'shell32', 'user32', 'OpenGL32', 'winmm']
    if RAYLIB_PLATFORM=="SDL":
        libraries += ['SDL2']

    print("libraries: "+str(libraries))
    ffibuilder.set_source("raylib._raylib_cffi", ffi_includes,
                          extra_link_args=['/NODEFAULTLIB:MSVCRTD'],
                          extra_compile_args=["/D_CFFI_NO_LIMITED_API"],
                          py_limited_api=False,
                          libraries=libraries,
                          include_dirs=['D:\\a\\raylib-python-cffi\\raylib-python-cffi\\raylib-c\\src',
                                        'D:\\a\\raylib-python-cffi\\raylib-python-cffi\\raylib-c\\src\\external\\glfw\\include',
                                        'D:\\a\\raylib-python-cffi\\raylib-python-cffi\\raygui\\src',
                                        'D:\\a\\raylib-python-cffi\\raylib-python-cffi\\physac\\src'],
                          )


ffibuilder = FFI()

if platform.system() == "Windows":
    build_windows()
else:
    print("not windows, trying Unix build")
    build_unix()


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
