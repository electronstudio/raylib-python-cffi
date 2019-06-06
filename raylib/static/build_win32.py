# Windows build assumes raylib, OpenGL32, etc are all already installed as system libraries.  We dont distribute them.

from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef(open("../raylib_modified.h").read().replace('RLAPI ', ''))
ffibuilder.set_source("_raylib_cffi",
	"""
	#include "../raylib.h"   
	""",
	extra_link_args=['/NODEFAULTLIB:MSVCRTD'],
	libraries=['raylib_static', 'gdi32', 'shell32', 'user32','OpenGL32', 'winmm'],
)


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
