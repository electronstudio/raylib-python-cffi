# Linux build assumes raylib, GL, etc are all already installed as system libraries.  We dont distribute them.
# Raylib must be installed the compiled with:  cmake -DWITH_PIC=ON -DSHARED=ON -DSTATIC=ON ..

from cffi import FFI
import os
import platform
ffibuilder = FFI()


ffibuilder.cdef(open("../raylib_modified.h").read().replace('RLAPI ', ''))


ffibuilder.set_source("_raylib_cffi",
                      """
                           #include "../raylib.h"   
                      """,
                      extra_link_args=['/usr/local/lib/libraylib.a','-lm', '-lpthread', '-lGLU', '-lGL',  '-lrt', '-lm', '-ldl', '-lX11', '-lpthread'],
                      libraries=['GL','m','pthread', 'dl', 'rt', 'X11']
                      )


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

