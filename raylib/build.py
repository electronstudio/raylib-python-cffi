from cffi import FFI
import os
ffibuilder = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef(open("raylib_modified.h").read().replace('RLAPI ', ''))

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_raylib_cffi",
                      """
                           #include "raylib.h"   // the C header of the library
                      """,
                      #library_dirs=['/Volumes/Home/rich/raylib-latest/src'],
#                      extra_link_args=['-Wl,-rpath,.'],
                      #extra_link_args=["/usr/local/lib/libraylib.a","-framework OpenGL"]# -F/System/Library/Frameworks -framework OpenGL -framework Cocoa -framework IOKit -framework CoreFoundation -framework CoreVideo"]
#                     library_dirs=[os.path.dirname(__file__)+"/../lib"],
                      #libraries=['raylib']
                      )

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
    os.system("clang -bundle -undefined dynamic_lookup ./_raylib_cffi.o -L/usr/local/lib -L/usr/local/opt/openssl/lib -L/usr/local/opt/sqlite/lib libraylib.a -F/System/Library/Frameworks -framework OpenGL -framework Cocoa -framework IOKit -framework CoreFoundation -framework CoreVideo -o ./_raylib_cffi.cpython-37m-darwin.so")
