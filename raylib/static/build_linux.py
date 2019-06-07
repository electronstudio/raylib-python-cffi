# Linux build assumes raylib, GL, etc are all already installed as system libraries.  We dont distribute them.

from cffi import FFI
import os
import platform
ffibuilder = FFI()


ffibuilder.cdef(open("../raylib_modified.h").read().replace('RLAPI ', ''))


ffibuilder.set_source("_raylib_cffi",
                      """
                           #include "../raylib.h"   // the C header, installed in the system include dir we assume
                      """,
                      extra_link_args=['../../linux_libs/core.o', '../../linux_libs/models.o', '../../linux_libs/raudio.o', '../../linux_libs/rglfw.o','../../linux_libs/shapes.o','../../linux_libs/text.o','../../linux_libs/textures.o','../../linux_libs/utils.o','-lm', '-lpthread', '-lGLU', '-lGL',  '-lrt', '-lm', '-ldl', '-lX11', '-lpthread'],
                      libraries=['GL','m','pthread', 'dl', 'rt', 'X11']
                      )


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

