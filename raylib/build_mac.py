from cffi import FFI
import os
import platform
ffibuilder = FFI()


ffibuilder.cdef(open("raylib_modified.h").read().replace('RLAPI ', ''))


ffibuilder.set_source("_raylib_cffi",
                      """
                           #include "raylib.h"   // the C header of the library
                      """
                      )

# Hack to produce static linked lib
command = "clang -bundle -undefined dynamic_lookup ./_raylib_cffi.o -L/usr/local/lib -L/usr/local/opt/openssl/lib -L/usr/local/opt/sqlite/lib libraylib.a -F/System/Library/Frameworks -framework OpenGL -framework Cocoa -framework IOKit -framework CoreFoundation -framework CoreVideo -o ./_raylib_cffi.cpython-37m-darwin.so"

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
    if platform.system()=="Darwin":
        print(command)
        os.system(command)
