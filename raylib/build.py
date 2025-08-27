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


import re
from cffi import FFI
import os
import platform
import subprocess
import time
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
REPO_ROOT = THIS_DIR.parent

# TODO: I think the customisation is making this file overly complex and probably isn't used
# by many/any users, see discussion at https://github.com/electronstudio/raylib-python-cffi/pull/172
#
# Environment variables you can set before build
#
# RAYLIB_PLATFORM: Any one of: Desktop, SDL, DRM, PLATFORM_COMMA
# RAYLIB_LINK_ARGS: Arguments to pass to the linker rather than getting them from pkg-config.
#    e.g.: -L/usr/local/lib -lraylib
# RAYLIB_INCLUDE_PATH: Directory to find raylib.h rather than getting from pkg-config.
#    e.g.: /usr/local/include
# RAYGUI_INCLUDE_PATH: Directory to find raygui.h
#    e.g.: /usr/local/include
# GLFW_INCLUDE_PATH: Directory to find glfw3.h
#    e.g.: /usr/local/include/GLFW
# PHYSAC_INCLUDE_PATH: Directory to find physac.h
#    e.g.: /usr/local/include
# LIBFFI_INCLUDE_PATH:
#    e.g.: /usr/local/include
#
# PKG_CONFIG_LIB_raylib: the package to request from pkg-config for raylib include files, default 'raylib'
# PKG_CONFIG_LIB_raygui: the package to request from pkg-config for raygui include files
#   set to 'raygui' if you have a separate raygui package, else unset for default 'raylib'
# PKG_CONFIG_LIB_physac: the package to request from pkg-config for physac indlude files
#   set to 'physac' if you have a separate raygui physac, else unset for default 'raylib'
# PKG_CONFIG_LIB_glfw3: the package to request from pkg-config for glfw3 include files
#   set to 'glfw3' if you have a separate glfw3 package, else unset for default 'raylib'
# PKG_CONFIG_LIB_libffi: the package to request from pkg-config for libffi include files

RAYLIB_PLATFORM = os.getenv("RAYLIB_PLATFORM", "Desktop")

def check_raylib_pkgconfig_installed():
    # this should be 'pkg-config --exists raylib' but result is non-deterministic on old versions of pkg-config!
    return subprocess.run(['pkg-config', '--libs', 'raylib'], text=True, stdout=subprocess.PIPE).returncode == 0

def check_sdl_pkgconfig_installed():
    # this should be 'pkg-config --exists sdl2' but result is non-deterministic on old versions of pkg-config!
    return subprocess.run(['pkg-config', '--libs', 'sdl2'], text=True, stdout=subprocess.PIPE).returncode == 0


def get_the_include_path_from_pkgconfig(libname):
    return subprocess.run(
        ['pkg-config', '--variable=includedir', os.environ.get("PKG_CONFIG_LIB_" + libname, 'raylib')], text=True,
        stdout=subprocess.PIPE).stdout.strip()


def get_the_lib_path_from_pkgconfig():
    return subprocess.run(['pkg-config', '--variable=libdir', 'raylib'], text=True,
                          stdout=subprocess.PIPE).stdout.strip()

def get_lib_flags_from_pkgconfig():
    return subprocess.run(['pkg-config', '--libs', 'raylib'], text=True,
                          stdout=subprocess.PIPE).stdout.strip()

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
    if os.getenv("RAYLIB_LINK_ARGS") is None and not check_raylib_pkgconfig_installed():
        print("PKG_CONFIG_PATH is set to: "+os.getenv("PKG_CONFIG_PATH"))
        raise Exception("ERROR: raylib not found by pkg-config.  Please install pkg-config and Raylib"
                        "or else set RAYLIB_LINK_ARGS env variable.")

    if RAYLIB_PLATFORM=="SDL" and os.getenv("RAYLIB_LINK_ARGS") is None and not check_sdl_pkgconfig_installed():
        print("PKG_CONFIG_PATH is set to: "+os.getenv("PKG_CONFIG_PATH"))
        raise Exception("ERROR: SDL2 not found by pkg-config.  Please install pkg-config and SDL2."
                        "or else set RAYLIB_LINK_ARGS env variable.")

    raylib_include_path = os.getenv("RAYLIB_INCLUDE_PATH")
    if raylib_include_path is None:
        raylib_include_path = get_the_include_path_from_pkgconfig("raylib")
    raylib_h = raylib_include_path + "/raylib.h"
    rlgl_h = raylib_include_path + "/rlgl.h"
    raymath_h = raylib_include_path + "/raymath.h"

    if not os.path.isfile(raylib_h):
        raise Exception("ERROR: " + raylib_h + " not found.  Please install Raylib or set RAYLIB_INCLUDE_PATH.")

    if not os.path.isfile(rlgl_h):
        raise Exception("ERROR: " + rlgl_h + " not found.  Please install Raylib or set RAYLIB_INCLUDE_PATH.")

    if not os.path.isfile(raymath_h):
        raise Exception("ERROR: " + raylib_h + " not found.  Please install Raylib or set RAYLIB_INCLUDE_PATH.")

    ffi_includes = """
    #include "raylib.h"
    #include "rlgl.h"
    #include "raymath.h"
    """

    glfw_include_path = os.getenv("GLFW_INCLUDE_PATH")
    if glfw_include_path is None:
        glfw_include_path = get_the_include_path_from_pkgconfig("glfw3")
    glfw3_h = glfw_include_path + "/GLFW/glfw3.h"
    if RAYLIB_PLATFORM=="Desktop" and check_header_exists(glfw3_h):
        ffi_includes += """
        #include "GLFW/glfw3.h"
        """

    raygui_include_path = os.getenv("RAYGUI_INCLUDE_PATH")
    if raygui_include_path is None:
        raygui_include_path = get_the_include_path_from_pkgconfig("raygui")
    raygui_h = raygui_include_path + "/raygui.h"
    if check_header_exists(raygui_h):
        ffi_includes += """
        #define RAYGUI_IMPLEMENTATION
        #define RAYGUI_SUPPORT_RICONS
        #include "raygui.h"
        """

    physac_include_path = os.getenv("PHYSAC_INCLUDE_PATH")
    if physac_include_path is None:
        physac_include_path = get_the_include_path_from_pkgconfig("physac")
    physac_h = physac_include_path + "/physac.h"
    if check_header_exists(physac_h):
        ffi_includes += """
        #define PHYSAC_IMPLEMENTATION
        #include "physac.h"
        """

    libffi_include_path = os.getenv("LIBFFI_INCLUDE_PATH")
    if libffi_include_path is None:
        libffi_include_path = get_the_include_path_from_pkgconfig("libffi")

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
        flags = os.getenv("RAYLIB_LINK_ARGS")
        if flags is None:
            flags = get_the_lib_path_from_pkgconfig() + '/libraylib.a'
        # We use /usr/local/lib/libraylib.a to ensure we link to static version
        extra_link_args = flags.split() + ['-framework', 'OpenGL', '-framework', 'Cocoa',
                           '-framework', 'IOKit', '-framework', 'CoreFoundation', '-framework',
                           'CoreVideo']
        if RAYLIB_PLATFORM=="SDL":
            extra_link_args += ['/usr/local/lib/libSDL2.a', '-framework', 'CoreHaptics', '-framework', 'ForceFeedback',
            '-framework', 'GameController']
        libraries = []
        extra_compile_args = ["-Wno-error=incompatible-function-pointer-types", "-D_CFFI_NO_LIMITED_API"]
    else:  #platform.system() == "Linux":
        print("BUILDING FOR LINUX")
        flags = os.getenv("RAYLIB_LINK_ARGS")
        if flags is None:
            flags = get_lib_flags_from_pkgconfig()
        extra_link_args = flags.split() + [ '-lm', '-lpthread', '-lGL',
                                              '-lrt', '-lm', '-ldl', '-lpthread', '-latomic']
        if RAYLIB_PLATFORM=="SDL":
            extra_link_args += ['-lX11','-lSDL2']
        elif RAYLIB_PLATFORM=="DRM":
            extra_link_args += ['-lEGL', '-lgbm']
        elif RAYLIB_PLATFORM=="PLATFORM_COMMA":
            extra_link_args.remove('-lGL')
            extra_link_args += ['-lGLESv2', '-lEGL', '-lwayland-client', '-lwayland-egl']
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
                          include_dirs=[raylib_include_path, raygui_include_path, physac_include_path, glfw_include_path,
                                        libffi_include_path],
                          extra_link_args=extra_link_args,
                          extra_compile_args=extra_compile_args,
                          libraries=libraries)


def build_windows():
    print("BUILDING FOR WINDOWS")
    ffibuilder.cdef((THIS_DIR / "raylib.h.modified").read_text())
    if RAYLIB_PLATFORM=="Desktop":
        ffibuilder.cdef((THIS_DIR / "glfw3.h.modified").read_text())
    ffibuilder.cdef((THIS_DIR / "rlgl.h.modified").read_text())
    ffibuilder.cdef((THIS_DIR / "raygui.h.modified").read_text())
    ffibuilder.cdef((THIS_DIR / "physac.h.modified").read_text())
    ffibuilder.cdef((THIS_DIR / "raymath.h.modified").read_text())

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
    #define PHYSAC_NO_THREADS
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
                          include_dirs=[str(REPO_ROOT / 'raylib-c/src'),
                                        str(REPO_ROOT / 'raylib-c/src/external/glfw/include'),
                                        str(REPO_ROOT / 'raygui/src'),
                                        str(REPO_ROOT / 'physac/src')],
                          )


ffibuilder = FFI()

if platform.system() == "Windows":
    build_windows()
else:
    print("not windows, trying Unix build")
    build_unix()


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
