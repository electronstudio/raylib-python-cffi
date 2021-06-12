# Assumes raylib, GL, etc are all already installed as system libraries.  We dont distribute them.
# Raylib must be installed and compiled with:  cmake -DWITH_PIC=ON -DSHARED=ON -DSTATIC=ON ..

from cffi import FFI
import os
import platform
import sys

ffibuilder = FFI()

def build_linux():
    print("BUILDING FOR LINUX")
    ffibuilder.cdef(open("raylib/raylib_modified.h").read().replace('RLAPI ', ''))
    ffibuilder.set_source("raylib.static._raylib_cffi",
                          """
                               #include "../../raylib/raylib.h"
                          """,
                          extra_link_args=['/usr/local/lib/libraylib.a','-lm', '-lpthread', '-lGLU', '-lGL',  '-lrt', '-lm', '-ldl', '-lX11', '-lpthread'],
                          libraries=['GL','m','pthread', 'dl', 'rt', 'X11']
                          )
    if __name__ == "__main__":
        ffibuilder.compile(verbose=True)

def build_windows():
    print("BUILDING FOR WINDOWS")
    ffibuilder.cdef(open("raylib/raylib_modified.h").read().replace('RLAPI ', '').replace('bool','int'))
    ffibuilder.set_source("raylib.static._raylib_cffi",
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
    ffibuilder.set_source("raylib.static._raylib_cffi",
                          """
                               #include "./../raylib/raylib.h"   // the C header of the library, supplied by us here
                          """
                          )
    # Hack to produce static linked lib using static librarylib.a supplied by us
    version = sys.implementation.cache_tag
    if version == 'cpython-36' or version == 'cpython-37':
        version += 'm'
    command = "clang -bundle -undefined dynamic_lookup ./_raylib_cffi.o -L/usr/local/lib -L/usr/local/opt/openssl/lib -L/usr/local/opt/sqlite/lib ../../libraylib_mac.a -F/System/Library/Frameworks -framework OpenGL -framework Cocoa -framework IOKit -framework CoreFoundation -framework CoreVideo -o ./_raylib_cffi."+version+"-darwin.so"

    if __name__ == "__main__":
        ffibuilder.compile(verbose=True)
        if platform.system()=="Darwin":
            print(command)
            os.system(command)

def build_rpi_nox():
    print("BUILDING FOR RASPBERRY PI")
    ffibuilder.cdef(open("raylib/raylib_modified.h").read().replace('RLAPI ', ''))
    ffibuilder.set_source("raylib.static._raylib_cffi",
                          """
                               #include "./../raylib/raylib.h"
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