"""
This is an attempt at a CFFI dynamic (ABI) binding.  However, it fails to work in the exactly same place the ctypes binding fails, accessing
materials of a model.
"""


import pathlib
MODULE = pathlib.Path(__file__).parent.parent

from cffi import FFI
ffi = FFI()
ffi.cdef(open(MODULE / "raylib_modified.h").read().replace('RLAPI ', ''))

raylib = ffi.dlopen(str(MODULE)+"/dynamic_binding/libraylib.2.dylib")

