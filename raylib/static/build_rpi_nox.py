# Raspberry Pi native (non-X) build assumes the GPU libraries are installed in /opt/vc, as per Raspbian.
# Raylib must be installed the compiled with:  cmake -DWITH_PIC=ON -DSHARED=ON -DSTATIC=ON -DPLATFORM='Raspberry Pi' ..

from cffi import FFI
import os
import platform
ffibuilder = FFI()


ffibuilder.cdef(open("../raylib_modified.h").read().replace('RLAPI ', ''))


ffibuilder.set_source("_raylib_cffi",
                      """
                           #include "../raylib.h"
                      """,
                      extra_link_args=['/usr/local/lib/libraylib.a',
                                       '/opt/vc/lib/libEGL_static.a', '/opt/vc/lib/libGLESv2_static.a',
                                       '-L/opt/vc/lib', '-lvcos', '-lbcm_host', '-lbrcmEGL', '-lbrcmGLESv2',
                                       '-lm', '-lpthread', '-lrt'],
                      )


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

