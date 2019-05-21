# Linux build assumes raylib, GL, etc are all already installed as system libraries.  We dont distribute them.

from cffi import FFI
import os
import platform
ffibuilder = FFI()


ffibuilder.cdef(open("raylib_modified.h").read().replace('RLAPI ', ''))


ffibuilder.set_source("_raylib_cffi",
                      """
                           #include "raylib.h"   // the C header of the library
                      """,
                      #library_dirs=['/Volumes/Home/rich/raylib-latest/src'],
#                      extra_link_args=['-Wl,-rpath,.'],
                      #extra_link_args=["/usr/local/lib/libraylib.a","-framework OpenGL"]# -F/System/Library/Frameworks -framework OpenGL -framework Cocoa -framework IOKit -framework CoreFoundation -framework CoreVideo"]
#                     library_dirs=[os.path.dirname(__file__)+"/../lib"],
                      libraries=['raylib','GL','m','pthread', 'dl', 'rt', 'X11']
                      )


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

