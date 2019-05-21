from ._raylib_cffi import ffi

def Vector3(x, y, z):
    return ffi.new("struct Vector3 *", [x, y, z])[0]

